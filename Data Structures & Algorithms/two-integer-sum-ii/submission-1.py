class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
         in1=0
         in2=len(numbers)-1
         while in1<in2:
            if numbers[in1]+numbers[in2]>target:
                in2-=1
            elif numbers[in1]+numbers[in2]<target:
                in1+=1
            else:
                a=in1+1
                b=in2+1
                break
         return [a,b]



        