word=str(input("enter the word: "))

is_palindrome=True


for i,c in enumerate(word):
    if c!=word[len(word)-1-i]:
        is_palindrome=False
        break
        

if is_palindrome:
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.") 
        