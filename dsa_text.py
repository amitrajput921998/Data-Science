def mySqrt(x):
    if x == 0:
        return 0

    left = 1
    right = x

    while left <= right:
        mid = left + (right - left) // 2

        if mid * mid == x:
            return mid
        elif mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1

    return right


x = int(input("Enter a non-negative integer: "))
result = mySqrt(x)
print("The square root of", x, "rounded down to the nearest integer is:", result)

