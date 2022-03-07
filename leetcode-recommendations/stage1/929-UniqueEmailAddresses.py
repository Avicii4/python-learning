from typing import List


class Solution:
    def num_unique_emails(self, emails: List[str]) -> int:
        def generate(email: str) -> str:
            [local, domain] = email.split('@')
            idx = local.find('+')
            if idx==-1:
                idx = len(local)
            local = ''.join(local[:idx].split('.'))
            return local + '@' + domain

        for i in range(len(emails)):
            emails[i] = generate(emails[i])
        return len(set(emails))


if __name__ == '__main__':
    sol = Solution()
    arr = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
    print(sol.num_unique_emails(arr))
