import sys
from stats import words_counter
from stats import ch_counter
from stats import sort_dicts

if len(sys.argv) < 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

def get_book_contents(path):
	with open(path) as f:
		return f.read()

def main():
	path= sys.argv[1]
	print("========= BOOKBOT ==========")
	print(f"Analyzing book found at {path}...")
	text= get_book_contents(path)
	num_words= words_counter(text)
	print("------- Word Count -------")
	print(f"Found {num_words} total words")
	print("------- Character Count -------")
	ch_stats= ch_counter(get_book_contents(path))
	sorted_dicts= sort_dicts(ch_stats)
	for ch in sorted_dicts:
		if ch["char"].isalpha():
			print(f"{ch["char"]}: {ch["num"]}")

	print("------- END -------")

main()
