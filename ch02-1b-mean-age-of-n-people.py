# 2.1b
def mean_age(n):
    """This function returns the mean age of n people."""
    s_age = 0
    for i in range(n):
        p_age = eval(input("Age of person {}: ".format(i + 1)))
        s_age = s_age + p_age
    m_age = s_age / 3
    return m_age

n = eval(input("How many people?: "))
print(mean_age(n))
