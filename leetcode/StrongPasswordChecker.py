'''
420. Strong Password Checker
Hard

586

1417

Add to List

Share
A password is considered strong if the below conditions are all met:

It has at least 6 characters and at most 20 characters.
It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
It does not contain three repeating characters in a row (i.e., "...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.

In one step, you can:

Insert one character to password,
Delete one character from password, or
Replace one character of password with another character.
 

Example 1:

Input: password = "a"
Output: 5
Example 2:

Input: password = "aA1"
Output: 3
Example 3:

Input: password = "1337C0d3"
Output: 0
 

Constraints:

1 <= password.length <= 50
password consists of letters, digits, dot '.' or exclamation mark '!'.
'''



class Solution:

    def hasLowerCase(s):
        for i in s:
            if i >= 'a' and i <= 'z':
                return True
        return False

    def hasUpperCase(s):
        for i in s:
            if i >= 'A' and i <= 'Z':
                return True
        return False
    
    def hasDigit(s):
        for i in s:
            if i >= '0' and i <= '9':
                return True
        return False

    def consecutiveLetters(s):
        consecutive=1
        res=oneDel=twoDel=0
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                consecutive+=1
            else:
                if(consecutive > 2):
                    res+=(consecutive)//3
                    if consecutive%3==0:
                        oneDel+=1
                    elif consecutive %3 ==1:
                        twoDel+=1                  
                consecutive=1
        if(consecutive > 2):
            res+=(consecutive)//3
            if consecutive%3==0:
                oneDel+=1
            elif consecutive %3 ==1:
                twoDel+=1
        return res ,oneDel,twoDel
            

    def strongPasswordChecker(self, password: str) -> int:
        errorCount=0
        if not Solution.hasLowerCase(password):
            errorCount+=1
        if not Solution.hasUpperCase(password):
            errorCount+=1  
        if not Solution.hasDigit(password):
            errorCount+=1
        consecutivesDel,oneDel,twoDel=Solution.consecutiveLetters(password)
        # print(errorCount,consecutivesDel)
        l=len(password)
        res=max(errorCount,consecutivesDel)
        if l<=20 and l >=6:
            return res
        elif l > 20:
            # print(f'l={l} res={res}')
            totalDeletes=l-20
            consecutivesDel -= min(totalDeletes, oneDel)
            consecutivesDel -= min(max(totalDeletes - oneDel, 0), twoDel * 2) // 2
            consecutivesDel -= max(totalDeletes - oneDel - 2 * twoDel, 0) // 3
            return totalDeletes + max(errorCount,consecutivesDel)
        else:
            return max(6-len(password),res)

s=input()
print(Solution.strongPasswordChecker(Solution,s))