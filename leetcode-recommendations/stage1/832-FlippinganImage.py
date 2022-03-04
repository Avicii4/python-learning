from typing import List


class Solution:
    # 让n 1变0，0变1，最简单的是1-n
    def flip_and_invert_image(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        for lst in image:
            arr = [1 - n for n in lst[::-1]]
            res.append(arr)
        return res


if __name__ == '__main__':
    sol = Solution()
    x = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    print(sol.flip_and_invert_image(x))
