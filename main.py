"""Best buy/sell days using divide-and-conquer maximum subarray."""
import csv
from pathlib import Path

SAMPLE = Path(__file__).resolve().parent / "sample_prices.csv"


def max_crossing_sum(differences, low, mid, high):
    total = 0
    best_left_sum = float("-inf")
    best_left = mid
    for i in range(mid, low - 1, -1):
        total += differences[i]
        if total > best_left_sum:
            best_left_sum = total
            best_left = i

    total = 0
    best_right_sum = float("-inf")
    best_right = mid + 1
    for i in range(mid + 1, high + 1):
        total += differences[i]
        if total > best_right_sum:
            best_right_sum = total
            best_right = i
    return best_left, best_right, best_left_sum + best_right_sum


def max_subarray(differences, low, high):
    if low == high:
        return low, high, differences[low]
    mid = (low + high) // 2
    options = [
        max_subarray(differences, low, mid),
        max_subarray(differences, mid + 1, high),
        max_crossing_sum(differences, low, mid, high),
    ]
    return max(options, key=lambda item: item[2])


def find_profit_divide_conquer(prices):
    if len(prices) < 2:
        return None, None, 0
    differences = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]
    start, end, profit = max_subarray(differences, 0, len(differences) - 1)
    if profit <= 0:
        return None, None, 0
    return start, end + 1, profit


def find_profit_linear(prices):
    if len(prices) < 2:
        return None, None, 0
    lowest_price = prices[0]
    lowest_day = 0
    best = (None, None, 0)
    for sell_day in range(1, len(prices)):
        profit = prices[sell_day] - lowest_price
        if profit > best[2]:
            best = (lowest_day, sell_day, profit)
        if prices[sell_day] < lowest_price:
            lowest_price, lowest_day = prices[sell_day], sell_day
    return best


def load_prices(filename):
    days, prices = [], []
    with open(filename, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            days.append(row["day"])
            prices.append(float(row["price"]))
    return days, prices


if __name__ == "__main__":
    import sys
    filename = sys.argv[1] if len(sys.argv) > 1 else SAMPLE
    days, prices = load_prices(filename)
    dc = find_profit_divide_conquer(prices)
    linear = find_profit_linear(prices)
    assert abs(dc[2] - linear[2]) < 1e-8, "Different profit results!"
    if dc[0] is None:
        print("No profitable trade found.")
    else:
        print("Divide and Conquer:")
        print(f"  Buy:  {days[dc[0]]} (${prices[dc[0]]:.2f})")
        print(f"  Sell: {days[dc[1]]} (${prices[dc[1]]:.2f})")
        print(f"  Maximum profit: ${dc[2]:.2f}")
    print(f"Linear scan maximum profit: ${linear[2]:.2f}")
