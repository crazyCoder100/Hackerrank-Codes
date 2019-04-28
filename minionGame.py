'''Note::
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules:-

 =>Both players are given the same string, .
 =>Both players have to make substrings using the letters of the string .
 =>Stuart has to make words starting with consonants.
 =>Kevin has to make words starting with vowels. 
 =>The game ends when both players have made all possible substrings.

example::
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
kevin's words = A,AN,ANA,ANAN,ANANA,A,AN,ANA(total = 9)
stuart's words = B,BA,BAN,BANA,BANAN,BANANA,N,NA,NAN,NANA,N,NA(total = 12)
'''

#code

def minion_game(string):
    slen = len(string)
    vowels = 'AEIOU'
    kevin = sum((slen - i) for i in range(slen) if s[i] in vowels)
    stuart = sum((slen - i) for i in range(slen) if s[i] not in vowels)
    print("Draw" if stuart == kevin else "Stuart {}".format(stuart) if stuart > kevin else "Kevin {}".format(kevin))


if __name__ == '__main__':
    s = input()
    minion_game(s)

