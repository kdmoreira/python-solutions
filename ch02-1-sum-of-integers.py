# 2.1
def add(x):
    """This function sums the first integers up to n."""
    sum = 0
    for i in range(x+1):
        sum += i
    return sum

n = eval(input("How many numbers?: "))
print(add(n))
