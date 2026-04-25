# main.py
import sys
import os

DEFAULT_FILENAME = "words.txt"

def remove_duplicates(words):
    return list(dict.fromkeys(words))

def sort_list(words, reverse=False, remove_duplicates_enabled=False):
    if remove_duplicates_enabled:
        words = remove_duplicates(words)
    return sorted(words, reverse=reverse)

if __name__ == "__main__":
    if len(sys.argv) > 1 and not sys.argv[1].startswith("--"):
        filename = sys.argv[1]
    else:
        filename = DEFAULT_FILENAME

    if not os.path.exists(filename):
        print(f"El archivo '{filename}' no existe.")
        sys.exit(1) 

    with open(filename) as f:
        words = [line.strip() for line in f]

    orden_descendente = "--desc" in sys.argv
    result = sort_list(words, reverse=orden_descendente)

    remove_duplicates_enabled = "--unique" in sys.argv
    result = sort_list(words, remove_duplicates_enabled=remove_duplicates_enabled)
    
    print(result)