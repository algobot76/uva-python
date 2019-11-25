while True:
    s = input()
    if s == '0 0 0 0':
        break

    nums = [int(n) for n in s.split()]
    ans = 1080


    def inc(a, b):
        return (a - b + 40) % 40 * 9


    ans += inc(nums[0], nums[1])
    ans += inc(nums[2], nums[1])
    ans += inc(nums[2], nums[3])
    print(ans)
