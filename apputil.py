# Exercise 1: Checks if a string reads the same backwards (ignores spaces/punctuation)
def palindrome(word):
    cleaned = ""
    for char in word:
        # use python build in function to check if the character is alphanumeric
        # and change the character to lower case
        if char.isalnum():
            cleaned += char.lower() 
    # check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]


# Exercise 2: Checks if opening and closing parentheses in a sequence are balanced
def parentheses(sequence):
    count = 0
    # count the number of opening parentheses
    for char in sequence:
        if char =="(":
            count += 1
        if char ==")":
            count -= 1
            # if the count is negative, it means there is an closing parenthesis
            # that is not opened, so return False
            if count < 0:
                return False
    # if the count is 0, it means all the parentheses are balanced, so return True
    return count == 0
