class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def __str__(self):
        self.lines = ''
        title = self.name.center(30, '*')
        self.lines += f"{title}\n"
        for item in range(len(self.ledger)):
            desc = self.ledger[item].get('description')[:23]
            amt = self.ledger[item].get('amount')
            self.lines += f"{desc:23}{amt:>7.2f}\n"
        self.lines += f"Total: {self.balance:6.2f}"
        return self.lines

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        self.balance += amount
        return self.balance

    def withdraw(self, amount, description=''):
        if self.check_funds(amount) is True:
            self.ledger.append({'amount': -amount, 'description': description})
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount) is True:
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False

def create_spend_chart(categories):
    lines = ''
    lines += "Percentage spent by category\n"

    total_spent = []
    for cat in categories:
        spent = 0
        for led in cat.ledger:
            if led['amount'] < 0:
                spent += abs(led['amount'])
        total_spent.append(spent)
        total = 0
        for i in total_spent:
            total += i
    
    circles = []
    for i in range(len(categories)):
        circle = round(total_spent[i]/total*100)/10
        circles.append(circle)
    
    for i in range(10,-1,-1):
        if i == 10:
            lines += f'{i*10}| '
        elif i < 10 and i > 0:
            lines += f' {i*10}| '
        else:
            lines += f'  {i}| '
    
        for circle in circles:
            if circle >= i:
                lines += 'o  '
            else:
                lines += '   '
        lines += '\n'
    
    lines += f"    {'-'*3*len(categories)}-\n"
    max_length = 0
    for cat in categories:
        current = cat.name
        if len(current) > max_length:
            max_length = len(current)
            maxx = current
        else:
            max_length = max_length
            maxx = maxx

    for i in range(0, max_length):
        lines += '     '
        for cat in categories:
            if len(cat.name) > i:
                lines += f'{cat.name[i]}  '
            else:
                lines += '   '
        lines += '\n'
    return lines.rstrip('\n')



snacks = Category('Snacks')
clothing = Category('Clothing')
auto = Category('Auto')
enter = Category('Hiburan')

snacks.deposit(1000, 'initial deposit')
auto.deposit(500)
enter.deposit(350)
auto.withdraw(134.40)
auto.withdraw(50)
enter.withdraw(200.15)
snacks.withdraw(10.15, 'groceries')
snacks.withdraw(15.89, 'restaurant and more food for desert')
snacks.transfer(50, clothing)
clothing.withdraw(25)

categories = [auto, enter, snacks, clothing]
print(snacks)

print(create_spend_chart(categories))

