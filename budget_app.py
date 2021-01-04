class Category:
    
    def __init__(self, category):
        self.category = category
        self.ledger = []


    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    
    def withdraw(self, amount, description=""):
        current_funds = self.check_funds(amount)
        
        if current_funds == True:
            self.ledger.append({"amount": -amount, "description": description})
            return True

        return False
    
    def transfer(self, amount, other_category):
        current_balance = self.check_funds(amount)
        if current_balance == False:
            return False

        self.withdraw(amount, f"Transfer to {other_category.category}")
        other_category.deposit(amount, f"Transfer from {self.category}")
        return True

    def check_funds(self, amount):
        current_balance = self.get_balance()
        if amount > current_balance:
            return False
        
        return True
    
    def get_balance(self):
        current_balance = 0
        for item in self.ledger:
            current_balance += item["amount"]

        return current_balance


    def __str__(self):
        total = self.get_balance()
        category_length = len(str(self.category))
        final_output = "*"*int((30-category_length)/2) + str(self.category) + "*"*int((30-category_length)/2)


        for item in self.ledger:
            description = "\n" + f"{item['description'][0:23]}"
            amount = item['amount']
            formated_amount = '{:.2f}'.format(amount)
            final_output += description + " " + formated_amount.rjust(30-len(description))

        final_output += ("\n" + "Total: " + f'{total}')
        
        
        return final_output



def create_spend_chart(categories_list):
    spent_by_category = []
    number_of_categories = len(categories_list)
    for item in categories_list:
        total = 0
        for operation in item.ledger:
            if operation["amount"] < 0:
                total += abs(operation["amount"])

        spent_by_category.append(total)
    total_spent = sum(spent_by_category)

    spent_in_percentage = []
    for num in range(number_of_categories):
        category_subtotal_in_percentage = spent_by_category[num] * 100 / total_spent
        rounded_down = round(category_subtotal_in_percentage) - (round(category_subtotal_in_percentage) % 10)
        spent_in_percentage.append(rounded_down)
    string_by_ten = [str(i)+"|" for i in list(range(0,101,10))]
    string_by_ten.reverse()
    
    final_string = "Percentage spent by category"

    empty_strings_list = {0: " ",1: " ",2: " "}

    for item in string_by_ten:
        for num in range(len(spent_in_percentage)):
            if int(item[:-1]) == spent_in_percentage[num]:
                empty_strings_list[num] = "o"
        final_string += "\n" + (item.rjust(4) + f" {empty_strings_list[0]}  {empty_strings_list[1]}  {empty_strings_list[2]}  ")

    final_string += ("\n" + "    " + "-" * 10)

    categories_extracted = [i.category for i in categories_list]
    max_length = 0
    for i in categories_extracted:
        if len(i) > max_length:
            max_length = len(i)
 
    final_string += "\n" + "     "
    for num in range(max_length):
        for num2 in range(len(categories_extracted)):
            
            try:
                final_string += (categories_extracted[num2][num] + "  ")
            
            except:
                final_string += "   "
        final_string += "\n" + "     "
    final_string = final_string.rstrip()
    final_string += "  "
  
    return final_string
