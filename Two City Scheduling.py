#leetcode 1029
#approach to sort the list base on the people where difference between travelling city a and city b is larger
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        counta=0
        costs.sort(key=lambda x: abs(x[0] - x[1]), reverse=True)
        print(costs)
        countb=0
        sum=0
        size=len(costs)
        
        for i in range(size):
            if(costs[i][0]<costs[i][1]):
                if counta<size//2:
                    sum=sum+costs[i][0]
                    counta+=1
                else:
                    sum=sum+costs[i][1]
                    countb+=1
            elif(costs[i][0]>=costs[i][1]):       
                if countb<size//2:
                    sum=sum+costs[i][1]
                    countb+=1
                else:
                    sum=sum+costs[i][0]
                    counta+=1
                
            print(sum)
        return sum        
