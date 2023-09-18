class Solution:
     def search(self, nums: list[int], target: int) -> int:
          
          # Start with two pointers, one at the beginning (low) and one at the end (high) of the list.
          low: int=0
          high: int=len(nums) - 1


          # Keep searching until the low pointer is less than or equal to the high pointer.
          while low <= high:
               
               # Find the middle index between low and high.
               mid: int = (high + low) // 2
               # Check if the middle element is greater than the target.

               if nums[mid] > target:
                    # If yes, move the high pointer to the element just before mid.
                    high = mid - 1
        
               # Check if the middle element is less than the target.
               elif  nums[mid] < target:
                    # If yes, move the low pointer to the element just after mid.
                    low = mid + 1

               # If neither greater nor less, we've found the target.
               else:
                    return mid
               
          # If the target is not found in the list, return -1.
          return -1


