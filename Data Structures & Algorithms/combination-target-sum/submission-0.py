class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, remaining: int, current: List[int]) -> None:
            if remaining == 0:
                result.append(current.copy())
                return

            for i in range(start, len(nums)):
                num = nums[i]

                if num > remaining:
                    break

                current.append(num)
                backtrack(i, remaining - num, current)
                current.pop()

        nums.sort()
        backtrack(0, target, [])
        return result