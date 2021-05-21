"""
The bonus paid by company is based on the profit commission. When the profit (I) is less than or equal to 100000 yuan, the bonus can be 10% of profit; When the profit is higher than 100000 yuan and lower than 200000 yuan, the part below 100000 yuan will be charged with 10% commission,
and the part above 100000 yuan will be charged with 7.5% commission;When the amount is between 200000 and 400000 yuan, the portion higher than 200000 yuan can be deducted by 5%; If it is between 400000 yuan and 600000 yuan, the commission will be 3% for the part above 400000 yuan;
In the range of 600000 to 1 million yuan, 1.5% of the commission can be levied on the part of more than 600000 yuan, and 1% of the commission can be levied on the part of more than 1 million yuan when more than 1 million yuan;
Input the monthly profit(I) from the keyboard and output the total amount of bonus.
"""
profit = float(input("Please input the profit: "))
if profit <= 100000:
    bonus = 0.1*profit
elif 100000 < profit <200000:
    bonus = 0.1*100000+0.075*(profit-100000)
elif 200000 <= profit < 400000:
    bonus = 0.1*100000+0.075*(200000-100000)+0.05*(profit-200000)
elif 400000 <= profit < 600000:
    bonus = 0.1*100000+0.075*(200000-100000)+0.05*(400000-200000)+0.03*(profit-400000)
elif 600000 <= profit <1000000:
    bonus = 0.1*100000+0.075*(200000-100000)+0.05*(400000-200000)+0.03*(600000-40000)+0.015*(profit-600000)
else:
    bonus = 0.1*100000+0.075*(200000-100000)+0.05*(400000-200000)+0.03*(600000-40000)+0.015*(1000000-600000)+0.01*(profit-1000000)
print(bonus)