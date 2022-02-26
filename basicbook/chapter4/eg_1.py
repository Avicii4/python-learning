import string
import random


# 生成建议密码
def generate_password(size):
    str_pool = string.digits + string.ascii_letters + string.punctuation
    pwd1 = ''.join(random.choice(str_pool) for _ in range(size))
    print(pwd1)
    pwd2 = ''.join(random.sample(str_pool, size))
    print(pwd2)


if __name__ == '__main__':
    generate_password(16)
