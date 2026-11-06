# Max Profit Finder

**Category:** Divide and Conquer  
**Language:** Python 3 (standard library only)

## Idea
Given a list of prices for successive days, find the best day to buy, then a later day to sell, to make the maximum profit. This is a small educational example, not financial advice.

## How it works
1. Convert the price list into daily price differences.
2. Use divide-and-conquer maximum subarray to locate the largest positive sum.
3. Convert those indices back to buy and sell days.
4. Check the maximum profit against a linear-scan solution.

## Run
```bash
python main.py
python main.py sample_prices.csv
python -m unittest -v
```

Input CSV: two columns called `day` and `price`.

## Complexity
- Divide and Conquer: **O(n log n)** time for the maximum subarray, **O(n)** space for differences and recursion-related storage.
- Linear scan: **O(n)** time and **O(1)** extra space.

If no positive profit exists, the program reports no profitable trade.
