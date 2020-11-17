# 2.1a
def add(n):
    """This function sums the first integers up to n."""
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum

n = eval(input("How many numbers?: "))
print(add(n))
