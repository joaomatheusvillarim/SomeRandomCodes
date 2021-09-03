#divs, mmc, mdc

def divisores(num):
    num, div_list = int(num), []
    for x in range(1, 1+num):
        if num%x==0:
            div_list.append(x)
    return div_list

def mdc(num1, num2):
    common_divs = sorted(list(set(divisores(num1)).intersection(divisores(num2))))
    return common_divs[-1]

def mmc(num1, num2):
    return int((num1*num2)/mdc(num1, num2))

num_list = list(map(int, input().split()))
for num in num_list:
    print("The divisors of {} are {}".format(num, divisores(num)))

a, b = num_list[0], num_list[0]
for x in num_list:
    a, b = mdc(a, x), mmc(b, x)
print("For the numbers inserted, the GCD is {} and the LCM is {}".format(a, b))