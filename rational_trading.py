def get_new_price(original_price: float, pct_change:float) -> float:
    return original_price * (1 + pct_change/100)

def ifunsure(user_input:float) -> bool:
    if user_input == 0:
        return True
    
def ideal_rise_likelyhood_pct(current_price: float, buy_stop_price: float, sell_stop_price: float) -> float:
    # [1] rise likelyhood + drop likelyhood = 100%
    # [2] buy stop price * rise likelyhood + sell stop price * likelyhood = current price
    return (current_price - sell_stop_price)/(buy_stop_price - sell_stop_price) * 100

def ideal_sell_stop_price(current_price: float, buy_stop_price: float, rise_likelyhood_pct: float) -> float:
    # [1] rise likelyhood + drop likelyhood = 100%
    # [2] buy stop price * rise likelyhood + sell stop price * likelyhood = current price
    return (current_price - buy_stop_price * rise_likelyhood_pct)/(1 - rise_likelyhood_pct)

def gen_report(unsure_rise_likelyhood: bool, current_price: float, buy_stop_pct: float, buy_stop_price: float, sell_stop_pct:float, sell_stop_price:float, rise_likelyhood_pct: float):
    print()
    print("Thanks for your inputs!")
    print("Your current stock price: {:.2f}".format(current_price))
    print("1. Since your target percentage growth is {:.2f}%, your buy-stop price is {:.2f}.".format(buy_stop_pct, buy_stop_price))
    
    sell_stop_pct *= -1

    if unsure_rise_likelyhood:
        print("2. Since you plan to sell the stock if the price drops {:.2f}% to {:.2f},\n\
you should ensure that the chance the current price reaching the buy-stop price({:.2f}) is AT LEAST {:2f :2g}%,\n\
and should ensure that the chance the current price reaching the sell-stop price({:.2f}) is AT MOST {:2f}%."\
.format(sell_stop_pct, sell_stop_price, buy_stop_price, rise_likelyhood_pct, sell_stop_price, 100 - rise_likelyhood_pct))
    return

# Main body of codes begins here 
print()
print("Please answer the questions below about the stock. If unsure, enter '0'.")
current_price = float(input("Current price: "))
buy_stop_pct = float(input("Buy-stop if the current price rises (%): "))
buy_stop_price = get_new_price(current_price, buy_stop_pct)

rise_likelyhood_pct = float(input("How likely the current price can hit buy_stop (%): "))
if ifunsure(rise_likelyhood_pct):
    sell_stop_pct = float(input("Sell-stop if the current price drops (%): ")) * -1
    sell_stop_price = get_new_price(current_price, sell_stop_pct)
    rise_likelyhood_pct = ideal_rise_likelyhood_pct(current_price, buy_stop_price, sell_stop_price)
    gen_report(True, current_price, buy_stop_pct, buy_stop_price, sell_stop_pct, sell_stop_price, rise_likelyhood_pct)
else:
    sell_stop_price = ideal_sell_stop_price(current_price, buy_stop_price, rise_likelyhood_pct)




