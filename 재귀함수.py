def f(k):#def=함수정의 / 함수명(변수)
    if k==0:
        return
    else:
        f(k-1)
    print(k)

a=int(input())
f(a)#f 함수 k=a
