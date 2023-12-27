N = int(input())
Q = N / 5
R = N % 5

if R == 4:
    if N <= 9:
        if N == 4:
            print(-1)
        else:
            print(3)
    else:
        print(int(3 + (N - 9) / 5))
elif R == 3:
    if N != 3:
        print(int(1 + (N - 3) / 5))
    else:
        print(1)
elif R == 2:
    if N >= 12:
        print(int(4 + (N - 12) / 5))
    else:
        print(-1)
elif R == 1:
    if N > 6:
        print(int(2 + (N - 6) / 5))
    else:
        if N == 1:
            print(-1)
        else:
            print(2)
else:
    print(int(Q))
