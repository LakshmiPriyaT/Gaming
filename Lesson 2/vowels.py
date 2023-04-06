"""
word = input("Enter a sentence!!")
vowels = "AEIOUaeiou"
def Check_Vow(word, vowels):
    final = [each for each in word if each in vowels]
    print(len(final))
    print(final)
Check_Vow(word, vowels)

"""
def Check_Vow(string, vowels):
     
    # casefold has been used to ignore cases
    string = string.casefold()
     
    # Forms a dictionary with key as a vowel
    # and the value as 0
    #count = {}.fromkeys(vowels, 0)
    count = {"a":0,"e":0,"i":0,"o":0,"u":0}
     
    # To count the vowels
    for character in string:
        if character in count:
            count[character] += 1   
    return count
     
# Driver Code
vowels = 'aeiou'
string = input("Enter a sentence")
print (Check_Vow(string, vowels))