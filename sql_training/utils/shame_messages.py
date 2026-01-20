"""
Shame messages for the Extra Hint feature.
Ντροπιαστικά μηνύματα για όσους ζητούν extra βοήθεια.
"""
import random

SHAME_MESSAGES = [
    # Classic shame
    "Σοβαρά τώρα; Δεν μπορείς να το λύσεις μόνος σου;",
    "Ο καθηγητής σου θα ήταν τόσο απογοητευμένος...",
    "Αυτό το κουμπί είναι για τους αδύναμους. Είσαι αδύναμος;",
    "Μήπως να διαβάσεις λίγο θεωρία πρώτα;",
    "Ακόμα και η γιαγιά μου θα το έλυνε...",

    # Tech-themed
    "ChatGPT prompter detected 🤖",
    "Ctrl+C, Ctrl+V ζωή...",
    "SELECT shame FROM your_soul WHERE effort = 0",
    "Ο Codd δεν πέθανε για αυτό...",
    "Loading ντροπή... 99%",
    "DROP TABLE dignity;",
    "Error 404: Προσπάθεια not found",
    "git commit -m 'gave up'",

    # Motivational (sarcastic)
    "Η SQL δεν είναι τόσο δύσκολη... για κάποιους.",
    "Μια μέρα θα τα καταφέρεις. Προφανώς όχι σήμερα.",
    "Believe in yourself! ...ή μην το κάνεις, whatever.",
    "Κάποιοι άνθρωποι γεννιούνται DBAs. Εσύ όχι.",

    # Philosophical
    "Η ντροπή είναι προσωρινή, η άγνοια είναι μόνιμη... ή και τα δύο;",
    "Αν δεν προσπαθήσεις, δεν αποτυγχάνεις τεχνικά...",
    "I think, therefore I... need extra hints?",

    # Pop culture
    "You shall not pass... the exam like this",
    "May the SQL be with you... γιατί εσύ δεν είσαι",
    "Winter is coming, και εσύ ακόμα δεν ξέρεις JOINs",

    # University life
    "Αυτό θα φανεί στο βαθμό σου... oh wait",
    "Τουλάχιστον προσπάθησες... για 5 δευτερόλεπτα",
    "Η μαμά σου πληρώνει δίδακτρα για αυτό;",
    "Κάποιος θα κοπεί στις εξετάσεις...",

    # Self-aware
    "Ξέρω ότι είμαι μόνο ένα app, αλλά και εγώ ντρέπομαι",
    "Το κουμπί αυτό έχει πατηθεί πολλές φορές. Όχι τόσο νωρίς όμως.",
    "*sad database noises*",
    "Αυτό το hint δεν θα σε βοηθήσει στην εξέταση btw",
]


def get_random_shame_message() -> str:
    """Return a random shame message to discourage cheating."""
    return random.choice(SHAME_MESSAGES)
