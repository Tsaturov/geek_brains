prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90, 70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78,
          48.29, 8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]

# Задание A
for idx in prices:
    dd = str(idx).split('.')
    if len(dd) < 2:
        dd.append('00')

    print(f'{dd[0]} руб. {dd[1]} коп.', end=', ')


# Задание B
print(id(prices))
prices.sort()
print(prices, '\n', id(prices))

# Задание C
print(id(prices))
revers_prices = sorted(prices, reverse=True)
print(revers_prices, '\n', id(revers_prices))

# Задание D
top_five = sorted(prices, reverse=True)[:5]
top_five.reverse()
print(top_five)
