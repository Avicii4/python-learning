if __name__ == '__main__':
    a, da, b, db = input().split()
    num_a, num_b = a.count(da), b.count(db)
    pa = eval('1' * num_a + '*' + da) if num_a != 0 else 0
    pb = eval('1' * num_b + '*' + db) if num_b != 0 else 0
    print(pa + pb)
