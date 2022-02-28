class Solution:
    def hamming_distance(self, x: int, y: int) -> int:
        # 此题就是异或的定义
        return bin(x ^ y).count('1')


if __name__ == '__main__':
    sol = Solution()
    while True:
        a, b = map(int, input('请输入两个整数：').split())
        print(sol.hamming_distance(a, b))
