class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        curr=0
        start=0
        total=0
        for i in range(len(gas)):
            d=gas[i]-cost[i]
            total+=d
            curr+=d
            if curr<0:
                start=i+1
                curr=0
        if total<0:
            return -1
        return start