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
from utils.shame_messages import get_random_shame_message

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
    # Extra hint (shame) feature
    if 'extra_hint_clicks' not in st.session_state:
        st.session_state.extra_hint_clicks = {}  # {question_id: click_count}
    if 'show_extra_hint' not in st.session_state:
        st.session_state.show_extra_hint = {}  # {question_id: bool}
    if 'current_shame_message' not in st.session_state:
        st.session_state.current_shame_message = None


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


def analyze_query_concepts(query: str) -> dict:
    """Analyze a SQL query to identify key concepts and structure."""
    query_upper = query.upper()
    query_clean = ' '.join(query.split())  # Normalize whitespace

    concepts = {
        'tables': [],
        'joins': [],
        'has_subquery': 'SELECT' in query_upper[query_upper.find('FROM'):] if 'FROM' in query_upper else False,
        'has_correlated_subquery': False,
        'has_group_by': 'GROUP BY' in query_upper,
        'has_having': 'HAVING' in query_upper,
        'has_order_by': 'ORDER BY' in query_upper,
        'has_distinct': 'DISTINCT' in query_upper,
        'has_not_exists': 'NOT EXISTS' in query_upper,
        'has_double_not_exists': query_upper.count('NOT EXISTS') >= 2,
        'aggregates': [],
        'is_division': False,
    }

    # Detect aggregates
    for agg in ['COUNT', 'SUM', 'AVG', 'MAX', 'MIN']:
        if agg + '(' in query_upper:
            concepts['aggregates'].append(agg)

    # Detect tables (simple extraction from FROM and JOIN)
    import re
    # Find tables after FROM
    from_match = re.search(r'FROM\s+(\w+)', query, re.IGNORECASE)
    if from_match:
        concepts['tables'].append(from_match.group(1))

    # Find JOIN tables
    join_matches = re.findall(r'JOIN\s+(\w+)', query, re.IGNORECASE)
    concepts['tables'].extend(join_matches)
    concepts['joins'] = join_matches

    # Detect SQL Division pattern
    if concepts['has_double_not_exists']:
        concepts['is_division'] = True

    # Detect correlated subquery
    if concepts['has_subquery'] and re.search(r'WHERE\s+\w+\.\w+\s*=\s*\w+\.\w+', query, re.IGNORECASE):
        concepts['has_correlated_subquery'] = True

    return concepts


def get_hint_level_1(question: dict) -> str:
    """Level 1: Explain the problem and approach (conceptual)."""
    query = question['expected_query']
    concepts = analyze_query_concepts(query)

    hints = ["**🧠 Ανάλυση Προβλήματος:**\n"]

    # Explain the general approach
    if concepts['is_division']:
        hints.append("• Αυτό είναι πρόβλημα **SQL Division** - ψάχνεις οντότητες που σχετίζονται με ΟΛΕΣ τις οντότητες μιας άλλης ομάδας.")
        hints.append("• Σκέψου το ως: «δεν υπάρχει X που να μην το έχει κάνει»")
        hints.append("• Τεχνική: Διπλό NOT EXISTS")
    elif concepts['has_not_exists']:
        hints.append("• Χρειάζεσαι **NOT EXISTS** για να ελέγξεις ότι κάτι ΔΕΝ υπάρχει")
        hints.append("• Σκέψου: ποια συνθήκη πρέπει να ΜΗΝ ισχύει;")
    elif concepts['has_correlated_subquery']:
        hints.append("• Χρειάζεσαι **correlated subquery** - υποερώτημα που αναφέρεται στο εξωτερικό query")
        hints.append("• Το εσωτερικό query εξαρτάται από κάθε γραμμή του εξωτερικού")

    if concepts['has_group_by'] and concepts['has_having']:
        hints.append("• Χρειάζεσαι **GROUP BY + HAVING** για φιλτράρισμα ομάδων")
        hints.append("• WHERE φιλτράρει γραμμές ΠΡΙΝ την ομαδοποίηση, HAVING ΜΕΤΑ")

    if len(concepts['joins']) > 0:
        hints.append(f"• Χρειάζεσαι **{len(concepts['joins'])} JOIN(s)** για να συνδέσεις τους πίνακες")

    if concepts['aggregates']:
        hints.append(f"• Θα χρησιμοποιήσεις: **{', '.join(concepts['aggregates'])}**")

    if concepts['has_subquery'] and not concepts['has_not_exists']:
        hints.append("• Χρειάζεσαι **υποερώτημα (subquery)** για ενδιάμεσο υπολογισμό")

    return '\n'.join(hints)


def get_hint_level_2(question: dict) -> str:
    """Level 2: Show structure and tables involved."""
    query = question['expected_query']
    concepts = analyze_query_concepts(query)

    hints = ["**🔧 Δομή Λύσης:**\n"]

    # Show tables involved
    if concepts['tables']:
        hints.append(f"**Πίνακες:** {', '.join(set(concepts['tables']))}")

    # Show structure based on query type
    if concepts['is_division']:
        hints.append("""
**Πρότυπο SQL Division:**
```sql
SELECT ...
FROM TableA a
WHERE NOT EXISTS (
    SELECT ...
    FROM TableB b
    WHERE [συνθήκη για B]
    AND NOT EXISTS (
        SELECT 1
        FROM RelationTable r
        WHERE r.a_id = a.id AND r.b_id = b.id
    )
)
```""")
    elif concepts['has_not_exists']:
        hints.append("""
**Πρότυπο NOT EXISTS:**
```sql
SELECT ...
FROM Table1
WHERE NOT EXISTS (
    SELECT 1
    FROM Table2
    WHERE [συνθήκη σύνδεσης]
    AND [επιπλέον συνθήκη]
)
```""")
    elif concepts['has_group_by'] and concepts['has_having']:
        aggs = concepts['aggregates'] if concepts['aggregates'] else ['COUNT/SUM/AVG']
        hints.append(f"""
**Πρότυπο GROUP BY + HAVING:**
```sql
SELECT column, {aggs[0]}(...)
FROM Table1
[JOIN Table2 ON ...]
GROUP BY column
HAVING {aggs[0]}(...) [συνθήκη]
```""")
    elif concepts['joins']:
        hints.append(f"""
**Πρότυπο με JOINs:**
```sql
SELECT ...
FROM {concepts['tables'][0] if concepts['tables'] else 'Table1'}
JOIN {concepts['joins'][0] if concepts['joins'] else 'Table2'} ON [συνθήκη]
{'JOIN ... ON [συνθήκη]' if len(concepts['joins']) > 1 else ''}
WHERE [φίλτρα]
```""")

    return '\n'.join(hints)


def get_hint_level_3(question: dict) -> str:
    """Level 3: Show significant portion of actual solution."""
    query = question['expected_query']
    lines = [line.strip() for line in query.strip().split('\n') if line.strip()]

    hints = ["**💀 Μεγάλο μέρος της λύσης:**\n"]

    # Show ~70% of the query with some parts masked
    total_lines = len(lines)
    show_count = max(total_lines - 1, int(total_lines * 0.7))

    shown_lines = []
    for i, line in enumerate(lines[:show_count]):
        # Mask some specific values but keep structure
        import re
        # Keep the line mostly intact but maybe mask literal values
        masked = re.sub(r"'[^']*'", "'???'", line)  # Mask string literals
        masked = re.sub(r'\b\d+\b', 'N', masked)  # Mask numbers
        shown_lines.append(masked)

    if show_count < total_lines:
        shown_lines.append("    -- ... (συνέχεια)")

    hints.append("```sql")
    hints.append('\n'.join(shown_lines))
    hints.append("```")

    # Add a final tip
    hints.append("\n**💡 Tip:** Αντικατάστησε τα `'???'` με τις σωστές τιμές και το `N` με τους σωστούς αριθμούς.")

    return '\n'.join(hints)


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

    # Extra Hint Button (με ντροπή)
    q_id = question['id']
    clicks = st.session_state.extra_hint_clicks.get(q_id, 0)

    with col2:
        if clicks < 3:
            button_labels = [
                "🆘 Extra Hint 1/3 (για τους αδύναμους)",
                "🆘 Extra Hint 2/3 (ακόμα;)",
                "🆘 Extra Hint 3/3 (τελευταία ευκαιρία)"
            ]
            if st.button(button_labels[clicks], key=f"extra_hint_{q_id}"):
                clicks += 1
                st.session_state.extra_hint_clicks[q_id] = clicks
                st.session_state.current_shame_message = get_random_shame_message()
                st.rerun()

    # Show shame message after each click
    if clicks > 0 and st.session_state.current_shame_message:
        st.warning(f"😈 {st.session_state.current_shame_message}")
        if clicks < 3:
            remaining = 3 - clicks
            st.caption(f"Απομένουν {remaining} επίπεδα hints...")

    # Show progressive hints based on click count
    if clicks >= 1:
        with st.expander("📖 Hint Level 1: Ανάλυση Προβλήματος", expanded=(clicks == 1)):
            st.markdown(get_hint_level_1(question))

    if clicks >= 2:
        with st.expander("🔧 Hint Level 2: Δομή Λύσης", expanded=(clicks == 2)):
            st.markdown(get_hint_level_2(question))

    if clicks >= 3:
        with st.expander("💀 Hint Level 3: Μεγάλο Μέρος Λύσης", expanded=True):
            st.error("🏳️ Παραδόθηκες πλήρως...")
            st.markdown(get_hint_level_3(question))

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
