def is_palindr(word):
    if len(word) == 1:
        return True
    else:
        if(word[0] == word[-1]):
            return is_palindr(word[1:-1])
        else:
            return False
        


# Example usage:
print(is_palindr("abac"))  # Output: False
print(is_palindr("aba"))   # Output: True
print(is_palindr("racecar"))  # Output: True
print(is_palindr("a"))     # Output: True
