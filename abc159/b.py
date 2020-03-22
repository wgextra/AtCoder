s = input()
def is_palindrome(s):
    return s == s[::-1]

s_len = len(s)
if is_palindrome(s) and is_palindrome(s[:(s_len-1)//2]) and is_palindrome(s[(s_len+3)//2-1:]):
    print("Yes")
else:
    print("No")
