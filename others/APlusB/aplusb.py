# coding: utf8

'''

给出两个整数a和b, 求他们的和, 但不能使用 + 等数学运算符。

'''

# 通过异或运算和与运算可以代替加号进行求解, 异或相当于是求和当时不进位, 那么通过与运算就可以知道哪些位需要进位, 从而进行求和

# 递归
def aplusb(a, b):
    if b == 0:
        return a
    c = a ^ b
    d = (a & b) << 1
    return aplusb(c, d)

# 迭代

def aplusb2(a, b):
    while b != 0:
        temp = a ^ b
        b = (a & b) << 1
        a = temp
    return a


if __name__ == '__main__':
    print(aplusb(37, 40))
    print(aplusb2(37, 40))
