class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        a={5:0,10:0}
        for i in bills:
            if i==5:
                a[5]+=1
            if i==10:
                a[10]+=1
                if a[5]==0:
                    return False
                elif a[5]>0:
                    a[5]-=1
            if i==20:
                if (a[10]>=1 and a[5]>=1):
                    a[10]-=1
                    a[5]-=1
                elif a[5]>=3:
                    a[5]-=3
                else:
                    return False
        return True
        