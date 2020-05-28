def censor_string(string, lst, char):
 modified_string=string.split()
 for word in modified_string:
     if word in lst:
        cypto_word = char*len(word)
        modified_string[modified_string.index(word)] = cypto_word
 print (' '.join(modified_string))


censor_string("Today is a Wednesday!", ["Today", "a"], "-")
censor_string("The cow jumped over the moon.", ["cow", "over"], "*")
censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*")
