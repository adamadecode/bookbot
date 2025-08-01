def get_book_contents(path):
	with open(path) as f:
		return f.read() 

def main():
	num_words= words_counter(get_book_contents("books/frankenstein.txt"))
	print(num_words)

def words_counter(book_contents):
	num_words= len(book_contents.split())
	return f"{num_words} words found in the document"
main()
