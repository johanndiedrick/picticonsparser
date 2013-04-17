import sys

#words to picticons

picticons_dictionary = {'I':'o<', 'know':'(.%.)', 'sunny':':O:'}

for line in sys.stdin:
	new_line = list()
	line = line.strip()
	line_words = line.split(" ")
	for word in line_words:
		if word in picticons_dictionary:
			word = picticons_dictionary[word]
		new_line.append(word)
	print " ".join(new_line)

