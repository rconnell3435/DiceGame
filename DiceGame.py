###QUESTION###
#If I have m dice, and you have n dice, whats the chance I throw higher than you?

def waystothrow(n, x):
    #Calculates ways to throw x with n dice
    sum = 0
    if n == 1:
        if 1 <= x and x <= 6:
            return 1
        else:
            return 0
    for i in range(x-6,x):
        sum = sum + waystothrow(n-1,i)
    return sum;

def playthegame(m,n):
    sum = 0.0
    for k in range(n, 6*n+1):
        for i in range(k+1, 6*m+1):
            sum = sum + waystothrow(n,k)*waystothrow(m,i)
    sum = sum/(6**(m+n))
    return sum


print(playthegame(3,5))



