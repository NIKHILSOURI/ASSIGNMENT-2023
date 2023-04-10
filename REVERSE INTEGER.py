class Solution:
    def reverse(self, f) :
        r = 0
        x = 0
        h = False
        if f<0:
            x = abs(f)
            h = True
        else:
            x = f
        while x>0:
            i = x%10
            r = r*10+i
            x//=10
        +if -2147483648 <=r  and r<= 2147483647:
            if h:
                return -r
            else:
                return r
        else:
            return 0


obj=Solution()
print(obj.reverse())
