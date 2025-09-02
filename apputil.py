#Excercise 1

# add code below ...
#Define a function to check a string is palindrome or not 
def palindrome(word):
#convert all the characters in lowercase
    word = word.lower()
#remove blankspace and comma
    word = word.replace(" ", "")  
    punctuation = ",.'\":!-;?"
#remove all punctuation marks as defined above    
    for check in punctuation:
        word = word.replace(check,"")
#reverse the string   
    reverse_word = word[::-1]
    if(word == reverse_word):
        return True
    else:
        return False

#Excercise 2
# Excercise 2 Define function `parentheses(sequence)` to check if parentheses are balanced
def parentheses(sequence): 
    check = 0
# loop to validate if both opening and closing parenthesis are in balance
    for i in sequence:
        if i == '(':
            check =check+1
        elif i == ')':
            check =check-1
    if check == 0:
        return True
    else:
        return False

