def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

# 示例输入
num1 = int(input("请输入第一个正整数: "))
num2 = int(input("请输入第二个正整数: "))

# 计算最大公约数和最小公倍数
gcd_result = gcd(num1, num2)
lcm_result = lcm(num1, num2)

# 输出结果
print(f"{num1} 和 {num2} 的最大公约数是: {gcd_result}")
print(f"{num1} 和 {num2} 的最小公倍数是: {lcm_result}")
