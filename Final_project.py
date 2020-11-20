# Twitter Sentiment analysis(classifier) check weather a tweet is good or bad
# Sentiment Analysis is the process of ‘computationally’ determining whether a piece of writing is positive negative or neutral. It’s also known as opinion mining, deriving the opinion or attitude of a speaker.

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


def strip_punctuation(word):
    for p_char in punctuation_chars:
        word=word.replace(p_char, "")
        
    return word


positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(sentence):
    p_words_count=0
    for word in sentence.split():
        if strip_punctuation(word).lower() in positive_words:
            p_words_count+=1
    return p_words_count


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(sentence):
    n_words_count=0
    for word in sentence.split():
        if strip_punctuation(word).lower() in negative_words:
            n_words_count+=1
    return n_words_count

def get_net(sentence):
	net_score=get_pos(sentence)-get_neg(sentence)
	return net_score


with open("project_twitter_data.csv","r") as t_data:
	with open("resulting_data.csv","w") as r_data:
		r_data.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
		r_data.write("\n")

		t_data.readline()
		for line in t_data:
			word=line.strip().split(",")
			data="{},{},{},{},{}".format(word[1],word[2],get_pos(word[0]),get_neg(word[0]),get_net(word[0]))
			r_data.write(data)
			r_data.write("\n")