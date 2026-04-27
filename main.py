# main.py
import argparse
import os
import sys

DEFAULT_FILENAME = "words.txt"

def remove_duplicates(words):
    return list(dict.fromkeys(words))

def sort_list(words, reverse=False, remove_duplicates_enabled=False):
    if remove_duplicates_enabled:
        words = remove_duplicates(words)
    return sorted(words, reverse=reverse)

def main():
    parser = argparse.ArgumentParser(description="Ordena y filtra una lista de palabras.")
    parser.add_argument('--file', type=str, default=DEFAULT_FILENAME, help='Archivo de texto con palabras a procesar')
    parser.add_argument('--desc', action='store_true', help='Orden descendente (Z-A) [Aporte Dev 1]')
    parser.add_argument('--unique', action='store_true', help='Elimina palabras duplicadas [Aporte Dev 2]')

    args = parser.parse_args()
    filename = args.file

    if not os.path.exists(filename):
        print(f"Error: El archivo '{filename}' no existe.")
        sys.exit(1)

    with open(filename, 'r') as f:
        words = [line.strip() for line in f.readlines() if line.strip()]

    result = sort_list(words, reverse=args.desc, remove_duplicates_enabled=args.unique)

    print("\n=======================================")
    print(" 📊 RESULTADOS DEL PROCESAMIENTO")
    print("=======================================")
    print(f" Archivo procesado : {filename}")
    print(f" Total de palabras : {len(result)}")
    print("---------------------------------------")
    
    for i, word in enumerate(result, 1):
        print(f" {i:02d} | {word}")
        
    print("=======================================\n")


if __name__ == "__main__":
    main()