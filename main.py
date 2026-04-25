# main.py
import sys

def remove_duplicates(words):
    return list(dict.fromkeys(words))

def sort_list(words, reverse=False, remove_duplicates_enabled=False):
    if remove_duplicates_enabled:
        words = remove_duplicates(words)
    return sorted(words, reverse=reverse)

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as f:
        words = [line.strip() for line in f]
    remove_duplicates_enabled = "--unique" in sys.argv
    result = sort_list(words, remove_duplicates_enabled=remove_duplicates_enabled)
    print(result)