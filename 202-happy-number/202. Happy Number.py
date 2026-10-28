class Solution:
    def isHappy(self, n: int) -> bool:
        a=set()
        while n!=1:
            if n in a:
                return False
            a.add(n)
            total=0
            for i in str(n):
                total+=int(i)**2
            n=total
        return True

        