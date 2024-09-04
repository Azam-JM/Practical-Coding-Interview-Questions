# Grouping Similar Titles
# input titles = ["movie", "movei", "sample", "sampel", "easy", "aesy"]
# Grouped title : dict_values([['movie', 'movei'], ['sample', 'sampel'], ['easy', 'aesy']])

def group_similar_titles(sequence):
	final_result = {}
	for word in sequence:
		char_array = [0] * 26
		for letter in word:
			index = ord(letter) - ord('a')
			char_array[index] += 1
		map_key = tuple(char_array)
		if map_key in final_result:
			final_result[map_key].append(word)
		else:
			final_result[map_key] = [word]
	return final_result.values()


def main():
	input_titles = ["movie", "movei", "sample", "sampel", "easy", "aesy"]
	print(f"Grouped title : {group_similar_titles(input_titles)}")

if __name__ == '__main__':
    main()
