class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1 2 3 4
        # 3
        # 1, go look for 2 by binary search
        # bounds 1 3
        # 1+3//2 = 2
        # 3 > 2, therefore the bounds get rewritten to 1 and 2-1 = 1
        # 2 is found, we are done
        # if number you need to look for is lower won't happen
        # start from middle of remaining array
        # if number at middle <, go to the middle of the right
        # if number at middle >, go to the middle of the left
        
        # or do two pointer
        # since array is sorted
        for i, number in enumerate(numbers):
            find = target - number
            l = i + 1
            r = len(numbers) - 1

            while l <= r:
                middle = l + int((r-l)//2)
                if numbers[middle] == find:
                    return [i+1, middle+1]
                elif numbers[middle] < find:
                    # go right
                    l = middle + 1
                else:
                    # go left
                    r = middle - 1



