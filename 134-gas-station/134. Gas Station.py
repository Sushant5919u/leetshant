class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If total gas is less than total cost, a solution is impossible
        if sum(gas) < sum(cost):
            return -1

        total_tank = 0
        start_index = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]

            # If the car runs out of gas at this station
            if total_tank < 0:
                # Reset the start station to the next station
                start_index = i + 1
                # Reset our current tank
                total_tank = 0

        return start_index