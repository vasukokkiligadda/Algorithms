class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a="({["
        b=")]}"
        ans=[]
        d={')':'(',']':'[','}':'{'}
        for i in s:
            if i in a:
                ans.append(i)
            else:
                if len(ans)!=0:
                    if ans[-1]==d[i]:
                        ans=ans[:-1]
                    else:
                        return False
                else:
                    return False
        if len(ans)==0:
            return True
        else:
            return False