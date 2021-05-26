''' what is difference between bottom-up and top-down approch?
The main difference is thart in bottom up approch we build the
solution space of subproblem while going towards our end result. 
In case of the top-down approch we are calling recursively 
the function and storing it in the call stack and then we are returning appropriatly 
if the certain conditions meet '''
# for top down approch
d = [-1 for i in range(100)]


def factorial_top_down(n):
    if n == 0:
        return 1
    if d[n] != -1:
        return d[n]
    else:
        d[n] = n*factorial_top_down(n-1)
        return d[n]


# print(factorial_top_down())

# for bottom-up approch
def factorial_bot_up(n):
    d = [-1 for i in range(100)]
    d[0] = 1
    for i in range(1, n):
        d[i] = i*d[i-1]
    return d[n-1]*n


print(factorial_bot_up(5))
