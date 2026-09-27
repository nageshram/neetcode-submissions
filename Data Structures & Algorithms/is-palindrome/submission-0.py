class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)<=0:
            return False
        rev=""
        new=""
        for i in range(len(s)):
            if s[i].isalnum():
                new=new+s[i].lower()
                rev=s[i].lower()+rev
        if new==rev:
            return True
        return False