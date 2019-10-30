from _3aransia.algorithms import *


# Test function
def run_tests():
    moroccan_words = pd.read_csv(BASE_DIR + DATA_DIR + OPEN_DICTIONARY)
    moroccan_words_str = moroccan_words["LDM"].to_string(index=False)
    print(moroccan_to_arabic(moroccan_words_str))
    
