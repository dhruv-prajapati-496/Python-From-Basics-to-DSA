# WAF to give INR value of a USD value
def USD_to_INR(money):
    return money*91.93

money = float(input("Enter USD Value: "))
print(USD_to_INR(money))