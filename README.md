# rational_trader
Don't lie to yourself that you are a long term investor when you are just too late to sell in a bear market. 

[Version 1.0] First Launch
- input currrent stock price, expected buy-stop and sell-stop, to check the rational value of the likelihood that the stock will reach the buy-stop
- Math: expected value = current stock price. For example: 
  - If current stock price is 100, your buy-stop price is 300 and sell-stop price is 80, the program will advice:
    - The chance that the price reaching buy-stop is at least 9%
    - The chance that the price dropping to sell-stop is no more than 91%
    - So that the expected return is at least >= current price

Future Oppurtunity:
- Scrapping financial data online
- more data analysis like PE ratio etc.
- Connect to a SQL database
- Have a user interface

Disclaimer:
1. I am not a professional trader. You are more than welcome if you could advice on my math and logic. 
2. I am still learning how to write better code, and please also feel free to advice. 
