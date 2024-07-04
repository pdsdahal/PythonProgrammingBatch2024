class Balance:
    def __init__(self, apple_income, google_income):
        self.apple_income = apple_income
        self.google_income = google_income

# To overload the + operator, we will need to implement __add__() function in the class.
    def __add__(self, other):
        a1 = self.apple_income + other.apple_income
        g1 = self.google_income + other.google_income

        balance_3 = Balance(a1, g1)
        return balance_3


balance_1 = Balance(10, 20)
balance_2 = Balance(20, 40)


total_balance = balance_1 + balance_2

print(f"Apple Income : {total_balance.apple_income}")
print(f"Google Income : {total_balance.google_income}")
