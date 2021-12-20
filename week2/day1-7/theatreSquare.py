def theatreSquare():
    m, n, a = map(int, input().split())

    num1 = m // a if m%a == 0 else m //a + 1
    num2 = n // a if n%a == 0 else n //a + 1

    result = num1*num2
    
    print(result)

theatreSquare()
