class Solution:
    def maxArea(self, height: list[int]) -> int:

        reflection = height
        container = 1

        while reflection:
            first_max = max(reflection)
            print(first_max)
            reflection = reflection.remove(max(reflection))
            print(reflection)
            break
            second_max = max(reflection)
            print(second_max)
            break
            volume = first_max * second_max

            container *= volume

