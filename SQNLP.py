

def forward_longest_match(text, dic):
    word_lst = []
    i = 0
    while i < len(text):
        longest_word = text[i]
        for j in range(i+1,len(text)+1):
            word = text[i:j]
            if word in dic:
                if len(word) > len(longest_word):
                    longest_word = word
        word_lst.append(longest_word)
        i+=len(longest_word)
    return word_lst


def backwards_longest_match(text, dic):
	word_lst = []
	i = len(text) - 1
	while i >= 0:
		longest_word = text[i]
		for j in range(0, i):
			word = text[j: i + 1]
			if word in dic:
				if len(word) > len(longest_word):
					longest_word = word
					break
		word_lst.insert(0,longest_word)
		i -= len(longest_word)
	return word_lst


def cnt_single_char(word_lst):
    return sum(1 for word in word_lst if len(word) == 1)


def bi_match(text,dic):
    f = forward_longest_match(text, dic)
    b = backwards_longest_match(text, dic)
    if len(f) < len(b):
        return f
    elif len(f) > len(b):
        return b
    else:
        return f if cnt_single_char(f) < cnt_single_char(b) else b


