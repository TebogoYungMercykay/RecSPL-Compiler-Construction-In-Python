from utilities.nfa_to_dfa import convert_nfa_to_dfa


def convert_to_dfa(dfa_filepath):
    print("---- Converting an NFA to DFA ----")
    print("----------------------------------")

    convert_nfa_to_dfa(dfa_filepath)

    print("----------------------------------\n\n")
