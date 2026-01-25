#Count the occurrence of each vowel in the sentence given as input by the user.
vowels={"a":0,"e":0,"i":0,"o":0,"u":0}
sentence=input("Enter your sentence:").lower()
for character in sentence:
    if character in vowels:
        vowels[character]=vowels[character]+1
print(vowels)

#Count the occurrence of each alphabet that occurs in the sentence 
#given as input by the user.
letters={}
user=input("Enter your sentence:").lower()
for character in user:
    if character.isalpha():
        if character in letters:
            letters[character]=letters[character]+1
        else:
            letters[character]=1
print(letters)

#Find if a given number entered by the user is a pangram or not ?
#A pangram number is a number which contains at least one occurrence of each digit.
pangram=int(input("Enter your numbers:"))

        