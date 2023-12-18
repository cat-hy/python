def Check_Vow(string,vowels):
	final=[each for each in string if each in vowels]
	print("Vowels in the above string is:",final)
	print("Length is:",len(final))

string=input("Enter string:")
vowels="AEIOUaeiou"
Check_Vow(string,vowels);
