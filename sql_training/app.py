"""
Interactive SQL Training System - Streamlit Application
Σύστημα εκπαίδευσης SQL με πραγματική βάση δεδομένων
"""
import streamlit as st
import pandas as pd
from pathlib import Path

# Add parent directory to path for imports
import sys
sys.path.insert(0, str(Path(__file__).parent))

from database.schema import create_database, get_schema_description
from database.seed_data import seed_database
from questions.question_bank import (
    QUESTIONS, DIFFICULTY_LEVELS, get_question_by_id, get_question_count
)
from questions.grading import compare_results
from utils.query_executor import execute_query, get_row_counts

# Page configuration
st.set_page_config(
    page_title="SQL Training System",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .difficulty-moderate { background-color: #4CAF50; color: white; padding: 3px 8px; border-radius: 4px; }
    .difficulty-difficult { background-color: #FF9800; color: white; padding: 3px 8px; border-radius: 4px; }
    .difficulty-very_hard { background-color: #F44336; color: white; padding: 3px 8px; border-radius: 4px; }
    .stTextArea textarea { font-family: 'Courier New', monospace; }
    div[data-testid="stExpander"] details summary p { font-weight: bold; }
</style>
""", unsafe_allow_html=True)


def init_database():
    """Initialize database if it doesn't exist."""
    db_path = Path(__file__).parent / "database" / "university.db"
    if not db_path.exists():
        create_database(str(db_path))
        seed_database(str(db_path))
    return str(db_path)


def init_session_state():
    """Initialize session state variables."""
    if 'completed_questions' not in st.session_state:
        st.session_state.completed_questions = set()
    if 'current_query' not in st.session_state:
        st.session_state.current_query = ""
    if 'last_result' not in st.session_state:
        st.session_state.last_result = None
    if 'last_error' not in st.session_state:
        st.session_state.last_error = ""
    if 'show_hint' not in st.session_state:
        st.session_state.show_hint = False


def render_sidebar():
    """Render the sidebar with question navigation."""
    st.sidebar.title("📊 SQL Training")

    # Progress section
    total = len(QUESTIONS)
    completed = len(st.session_state.completed_questions)
    progress = completed / total if total > 0 else 0

    st.sidebar.markdown("### Πρόοδος")
    st.sidebar.progress(progress)
    st.sidebar.markdown(f"**{completed}/{total}** ερωτήσεις ολοκληρώθηκαν")

    st.sidebar.markdown("---")

    # Question filters
    st.sidebar.markdown("### Φίλτρα")
    difficulty_filter = st.sidebar.selectbox(
        "Δυσκολία",
        options=['Όλες', 'Μέτρια', 'Δύσκολη', 'Πολύ Δύσκολη'],
        index=0
    )

    show_completed = st.sidebar.checkbox("Εμφάνιση ολοκληρωμένων", value=True)

    st.sidebar.markdown("---")

    # Question list
    st.sidebar.markdown("### Ερωτήσεις")

    # Map filter to difficulty key
    filter_map = {
        'Όλες': None,
        'Μέτρια': 'moderate',
        'Δύσκολη': 'difficult',
        'Πολύ Δύσκολη': 'very_hard'
    }
    selected_difficulty = filter_map[difficulty_filter]

    for q in QUESTIONS:
        # Apply filters
        if selected_difficulty and q['difficulty'] != selected_difficulty:
            continue
        if not show_completed and q['id'] in st.session_state.completed_questions:
            continue

        # Question button
        is_completed = q['id'] in st.session_state.completed_questions
        prefix = "✅ " if is_completed else ""
        diff_info = DIFFICULTY_LEVELS[q['difficulty']]

        if st.sidebar.button(
            f"{prefix}{q['id']}. {q['title']}",
            key=f"q_{q['id']}",
            use_container_width=True
        ):
            st.session_state.selected_question = q['id']
            st.session_state.current_query = ""
            st.session_state.last_result = None
            st.session_state.last_error = ""
            st.session_state.show_hint = False
            st.rerun()

    st.sidebar.markdown("---")

    # Schema reference toggle
    if st.sidebar.button("📖 Δείτε το Σχήμα", use_container_width=True):
        st.session_state.show_schema = not st.session_state.get('show_schema', False)
        st.rerun()


def render_schema_reference():
    """Render the database schema reference."""
    if st.session_state.get('show_schema', False):
        with st.expander("📖 Σχήμα Βάσης Δεδομένων", expanded=True):
            st.markdown(get_schema_description())

            # Show row counts
            db_path = init_database()
            counts = get_row_counts(db_path)
            st.markdown("**Πλήθος εγγραφών:**")
            cols = st.columns(3)
            for i, (table, count) in enumerate(counts.items()):
                cols[i % 3].metric(table, count)


def render_question(question: dict, db_path: str):
    """Render a single question with query workspace."""
    # Question header
    diff_info = DIFFICULTY_LEVELS[question['difficulty']]
    st.markdown(f"""
    ### Ερώτηση {question['id']}: {question['title']}
    <span class="difficulty-{question['difficulty']}">{diff_info['label']}</span>
    """, unsafe_allow_html=True)

    # Question description
    st.markdown(f"**{question['description']}**")

    # Hint button
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("💡 Υπόδειξη"):
            st.session_state.show_hint = not st.session_state.show_hint

    if st.session_state.show_hint:
        st.info(f"💡 **Υπόδειξη:** {question['hint']}")

    st.markdown("---")

    # Query input
    st.markdown("### Γράψτε το SQL ερώτημά σας:")
    query = st.text_area(
        "SQL Query",
        value=st.session_state.current_query,
        height=150,
        placeholder="SELECT ...",
        label_visibility="collapsed"
    )
    st.session_state.current_query = query

    # Action buttons
    col1, col2, col3 = st.columns([1, 1, 4])

    with col1:
        run_clicked = st.button("▶️ Εκτέλεση", type="secondary", use_container_width=True)

    with col2:
        submit_clicked = st.button("📤 Υποβολή", type="primary", use_container_width=True)

    # Execute query (Run)
    if run_clicked and query.strip():
        result_df, error = execute_query(query, db_path)
        st.session_state.last_result = result_df
        st.session_state.last_error = error

    # Submit for grading
    if submit_clicked and query.strip():
        # Execute user query
        user_result, user_error = execute_query(query, db_path)

        if user_error:
            st.error(f"❌ {user_error}")
        else:
            # Execute expected query
            expected_result, expected_error = execute_query(
                question['expected_query'], db_path
            )

            if expected_error:
                st.error(f"Σφάλμα συστήματος: {expected_error}")
            else:
                # Compare results
                is_correct, feedback = compare_results(
                    user_result,
                    expected_result,
                    order_matters=question.get('order_matters', False),
                    check_column_names=question.get('check_column_names', False)
                )

                if is_correct:
                    st.success(f"✅ {feedback}")
                    st.session_state.completed_questions.add(question['id'])
                    st.balloons()
                else:
                    st.error(f"❌ {feedback}")

                    # Show comparison
                    with st.expander("📊 Σύγκριση αποτελεσμάτων"):
                        col1, col2 = st.columns(2)
                        with col1:
                            st.markdown("**Το δικό σας αποτέλεσμα:**")
                            if user_result is not None:
                                st.dataframe(user_result, use_container_width=True)
                            else:
                                st.write("Κενό αποτέλεσμα")
                        with col2:
                            st.markdown("**Αναμενόμενο αποτέλεσμα:**")
                            if expected_result is not None:
                                st.dataframe(expected_result, use_container_width=True)
                            else:
                                st.write("Κενό αποτέλεσμα")

        st.session_state.last_result = user_result
        st.session_state.last_error = user_error if user_error else ""

    # Display results
    st.markdown("---")
    st.markdown("### Αποτελέσματα:")

    if st.session_state.last_error:
        st.error(st.session_state.last_error)
    elif st.session_state.last_result is not None:
        st.dataframe(st.session_state.last_result, use_container_width=True)
        st.caption(f"Επιστράφηκαν {len(st.session_state.last_result)} γραμμές")
    else:
        st.info("Εκτελέστε ένα ερώτημα για να δείτε τα αποτελέσματα.")


def render_welcome():
    """Render welcome screen when no question is selected."""
    st.markdown("""
    # 📊 Καλώς ήρθατε στο SQL Training System!

    Αυτό το εργαλείο σας βοηθά να εξασκηθείτε στην SQL με πραγματική βάση δεδομένων.

    ## Πώς λειτουργεί:

    1. **Επιλέξτε μια ερώτηση** από την πλαϊνή μπάρα
    2. **Γράψτε το SQL ερώτημά σας** στον editor
    3. **Πατήστε "Εκτέλεση"** για να δείτε τα αποτελέσματα (χωρίς βαθμολόγηση)
    4. **Πατήστε "Υποβολή"** όταν είστε έτοιμοι για βαθμολόγηση

    ## Επίπεδα δυσκολίας:

    - 🟢 **Μέτρια** (10 ερωτήσεις): SELECT, WHERE, απλά JOINs, συναρτήσεις συνάθροισης
    - 🟠 **Δύσκολη** (8 ερωτήσεις): Πολλαπλά JOINs, HAVING, υποερωτήματα
    - 🔴 **Πολύ Δύσκολη** (5 ερωτήσεις): SQL Division, φωλιασμένες συναθροίσεις

    ## Βάση Δεδομένων:

    Η βάση περιέχει δεδομένα ενός πανεπιστημίου με:
    - **Students**: Φοιτητές
    - **Professors**: Καθηγητές
    - **Courses**: Μαθήματα
    - **Enrolls**: Εγγραφές φοιτητών σε μαθήματα
    - **Publications**: Δημοσιεύσεις
    - **Writes**: Συσχέτιση καθηγητών-δημοσιεύσεων

    ---

    👈 **Επιλέξτε μια ερώτηση από την πλαϊνή μπάρα για να ξεκινήσετε!**
    """)


def main():
    """Main application entry point."""
    # Initialize
    db_path = init_database()
    init_session_state()

    # Render sidebar
    render_sidebar()

    # Main content area
    if 'selected_question' not in st.session_state:
        render_welcome()
    else:
        # Render schema if enabled
        render_schema_reference()

        # Render selected question
        question = get_question_by_id(st.session_state.selected_question)
        if question:
            render_question(question, db_path)
        else:
            st.error("Η ερώτηση δεν βρέθηκε.")


if __name__ == "__main__":
    main()
