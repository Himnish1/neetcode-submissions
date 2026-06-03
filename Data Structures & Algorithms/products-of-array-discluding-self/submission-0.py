from collections import deque
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sum_prefix = deque()
        sum_postfix = deque()
        running_prefix_sum = 1
        running_post_fix_sum = 1

        for i in range(len(nums)):
            running_prefix_sum *= nums[i]
            running_post_fix_sum *= nums[-(i+1)]
            sum_prefix.append(running_prefix_sum)
            sum_postfix.appendleft(running_post_fix_sum)
        
        # print("prefix", sum_prefix)
        # print("postfix", sum_postfix)
        final_product = []
        for i in range(len(nums)):
            if i-1<0:
                prev = 1
            else:
                prev = sum_prefix[i-1]
            if i+1 > len(nums)-1:
                nexti = 1
            else:
                nexti = sum_postfix[i+1]
            # print(prev, nexti)
            final_product.append(prev*nexti)
        return final_product
        
            
            
