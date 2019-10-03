def fibo(n: int) -> list:
    if n < 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

which_num = int(input("Please enter the number of fibonacci numbers you'd like to see: "))
fibo_nums = []
while (which_num > 0):
    fibo_nums.append(fibo(which_num))
    which_num -= 1

print(fibo_nums)
