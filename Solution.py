class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mySum = 0
        #Python doesnt seem to have switch statements
        
        
        for i in range(len(s)):
            if s[i]=='I':
                if(i+1 != len(s)):
                    if(s[i+1] =='V' or s[i+1] == 'X'):
                        mySum -=1
                    else:
                        mySum+=1
                else:
                    mySum+=1
            elif s[i]=='V':
                mySum +=5
            elif s[i]=='X':
                if(i+1 != len(s)):
                    if s[i+1]=='L' or s[i+1]=='C':
                        mySum-=10
                    else:
                        mySum +=10
                else:
                    mySum +=10
            elif s[i]=='L':
                mySum+=50
            elif s[i]=='C':
                if(i+1 != len(s)):
                    if s[i+1]=='D' or s[i+1]=='M':
                        mySum-=100
                    else:
                        mySum +=100
                else:
                    mySum +=100
            elif s[i] == 'D':
                mySum +=500
            elif s[i] == 'M':
                mySum+=1000
                
                
        return mySum
