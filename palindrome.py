
def isPalindrome(x: int) -> bool:
    
    reverse = 0
    num = x
    while num > 0:
        remainder = num % 10
        reverse = reverse * 10 + remainder
        num = num // 10

    if reverse == x:
        return True
    return False



print(isPalindrome(121))