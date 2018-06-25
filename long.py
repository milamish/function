def longest(astring):

	comparison_list = astring.split(' ')

	longest = comparison_list[0]

	for word in comparison_list:

		if len(word) > len(longest):

			longest = word

	return longest

if __name__ == '__main__':
	
        print(longest('i am a dreamer'))
