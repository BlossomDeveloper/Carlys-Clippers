
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# calculate all prices
total_price = 0

for total_price in prices:
    print(total_price)

# find the average price
average_price = total_price / len(prices)
print("Average Haircut Price: ", average_price)

# reduce the prices to be less 5 than what was initially
new_prices = []
for elem in prices:
    new_prices.append(elem - 5)
    print(new_prices)

# calculate total_revenue
total_revenue = 0

for i in range(len(hairstyles)):
    print(i)

for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
    print("Total Revenue: ", total_revenue)

# calculate average daily revenue
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

# only show cuts under 30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices) - 1) if new_prices[i] < 30]
print(cuts_under_30)