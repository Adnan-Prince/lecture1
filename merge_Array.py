def fun(t):
    a=""
    b=""
    f=""
    s=len(t)
    m=int(s/2)
    if t[m]=='*':
        print("You entered a valid string")
        for i in range(0,m):sssss
            a=a+t[i]
            b=b+t[i+m+1]
        for i in range(0,m):
            f=f+a[i]
            f=f+b[i]
        return f
    else:
        print("you entered  invalid string")
t="1234*abcd"
f=fun(t)
