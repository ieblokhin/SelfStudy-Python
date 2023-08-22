import os
import sys


# The function looks through all subdirectories to find txt files
def search(directory):
    for address, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt') and '$' not in file:
                yield os.path.join(address, file)


# The function takes a file path and a search word (opens the file, and reads each line of the file to find the desired word)
def read_from_path_txt(path, word_to_search):
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as r:
            for line in r:
                if word_to_search in line:
                    return True
    except PermissionError:
        pass  # Ignore permission errors
    return False


# The main part of the script to run the script as the main program
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python search_text.py <directory_path> <word_to_search>")
    else:
        directory_path = sys.argv[1]
        word_to_search = sys.argv[2]

        if not os.path.exists(directory_path):
            print("Directory does not exist.")
        else:
            files_with_word = []

            for file_path in search(directory_path):
                if read_from_path_txt(file_path, word_to_search):
                    files_with_word.append(file_path)

            if files_with_word:
                print("Files where specified word is found:")
                for file_path in files_with_word:
                    print(file_path)
            else:
                print("No files with the specified word found.")