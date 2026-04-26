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


import argparse

def read_file(filename):
    with open(filename, 'r') as f:
        words = [line.strip() for line in f.readlines()]
    return words

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, help='Archivo con palabras')
    parser.add_argument('words', nargs='*')

    args = parser.parse_args()

    if args.file:
        try:
            words = read_file(args.file)
        except FileNotFoundError:
            print("Error: archivo no encontrado")
            return
    else:
        words = args.words

    words.sort()
    print(words)

if __name__ == "__main__":
    main()