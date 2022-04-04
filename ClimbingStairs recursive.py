def climbingStairs(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    return climbingStairs(n-1)+climbingStairs(n-2)


if __name__ == "__main__":
    n = int(input())
    print(climbingStairs(n))
