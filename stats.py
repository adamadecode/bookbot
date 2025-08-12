def words_counter(book_contents):
	num_words= len(book_contents.split())
	return num_words

def ch_counter(text):
	counts={}
	text= text.lower()
	for ch in text:
		if ch not in counts:
			counts[ch]= 1
		else:
			counts[ch] += 1
	return counts

def sort_dicts(dict):
	dicts_list=[]
	for ch in dict:
		dicts_list.append({"char":ch, "num":dict[ch]})

	def sort_on(dicts_list):
		return dicts_list["num"]
	dicts_list.sort(reverse= True, key=sort_on)
	return dicts_list

