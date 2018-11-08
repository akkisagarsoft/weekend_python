str1 = input("Enter first string \n")
str2 = input("Enter second string \n")

if(sorted(str1) == sorted(str2)):
    print("Strings are anagram")
else:
    print("not anagrams")