def naive():
    ans = 0
    # 1 - 10
    one_to_nine = [3, 3, 5, 4, 4, 3, 5, 5, 4]
    ans += sum(one_to_nine) + len('ten')
    # 11 - 19
    eleven_to_nineteen = [6, 6, 8, 8, 7, 7, 9, 8, 8]
    ans += sum(eleven_to_nineteen)
    # 20 - 99
    mult_of_ten = [6, 6, 5, 5, 5, 7, 6, 6] # [twenty, thirty, forty..., ninety]
    for i in mult_of_ten:
        ans += sum(one_to_nine) + 10*i

    one_99 = ans

    # 100 - 999
    repeat_100  = 900
    repeat_1_99 = 10
    repeat_and  = repeat_100 - 9  # all hundreds except 100, 200, .., 900

    ans = repeat_1_99 * one_99 + repeat_100 * len('hundred') + repeat_and * len('and') + sum([100 * i for i in one_to_nine]) + len('onethousand')

    print(ans)

naive()



