from stats import num_words, num_chars, dic_sort
import sys
if len(sys.argv) != 2:
   print("Usage: python3 main.py <path_to_book>")
   sys.exit(1)
def get_book_text(f):
    with open(f) as f:
        f_str = f.read()
        return f_str
def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    book_str = get_book_text(sys.argv[1])
    wrds_number = num_words(book_str)
    print("----------- Word Count ----------")
    print(f"Found {wrds_number} total words")
    chars_number = num_chars(book_str)
    sorted_list = dic_sort(chars_number)
    print("--------- Character Count -------")
    for dics in sorted_list:
        print(f"{dics["char"]}: {dics["num"]}")
    print("============= END ===============")
main()
