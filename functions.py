import numpy as np

OPTIONS = ("Marketing Simulator",
           "Random Walk Simulator")


#funckja zwracająca wektor zysku
def ad_calc_profit(price_item, cost_item, ad_budget):

    profit_item = []
    break_even_cnt = 0

    # pętla zliczająca zysk dla każdego przypadku ceny i kosztu
    for i in range(len(price_item)):

        # główne zmienne
        unit_price = price_item[i]
        unit_cost = cost_item[i]
        sales_expense = 37000
        unit_sold = ad_budget*1000*0.7

        # łączny zysk
        profit = unit_sold * (unit_price - unit_cost) - sales_expense
        print("------")
        print(f"unit sold: {unit_sold}")
        print(unit_price, unit_cost, profit)

        profit_item.append(profit)

        if profit >= 0.0:
            break_even_cnt += 1

    #prawdopodobieństo wyjścia na +
    prob_profit = break_even_cnt / len(profit_item)

    return profit_item, prob_profit


def get_items_ad_triangular(unit_price, unit_cost, N):

    price_item = np.random.triangular(size=N, left=unit_price-25.0, right=unit_price+10.0, mode=unit_price)
    cost_item = np.random.triangular(size=N, left=unit_cost-5.0, right=unit_cost+10.0, mode=unit_cost)

    return price_item, cost_item


