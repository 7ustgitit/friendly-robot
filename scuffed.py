import tokenize
from tokenize import String

class encrypt:
    def make_hash(chars: list, x: int) -> String:
        replacer = "F"
        text = chars[x]
        lengthOfCharacters = len(chars[x])
        while lengthOfCharacters:
            text = replacer
            if text == text:
                hashed = text
                print(hashed)
                if hashed == text:
                    break
                else:
                    return False
        return hashed
    
    def make_salt(hashed) -> String:
        salt_replacer = "@" # how the heck am i gonna recover from hash and salt?
        return salt_replacer