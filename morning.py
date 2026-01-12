def greet(toria):
    """
    Returns a greeting message for the given name.
    """
    return f"Hello, {toria}!"
from datetime import date

def say_date():
    today = date.today()
    print(today.strftime("Today is %A, %B %d, %Y."))

# def calculate_cart_total(cart):
#     """
#     Calculate the total price of all items in the shopping cart.

#     Args:
#         cart (list of dict): Each dict has keys 'name' and 'price' (float or int).

#     Returns:
#         float: Total sum of all item prices.
#     """
#     total = 0.0
#     # for item in cart:
#     #     price = item.get("price", 0)
#     #     total += price
#     # return total
#     for item in cart:
#         price = item["price"]
#         total += price

#     return total

# if __name__ == "__main__":
#     shopping_cart = [
#         {"name": "Apple", "price": 1.50},
#         {"name": "Banana", "price": 0.75},
#         {"name": "Milk", "price": 2.25}
#     ]

#     total_price = calculate_cart_total(shopping_cart)
#     print(f"Total cart price: ${total_price:.2f}") 

# def word_count(words):
#     """
#     Count how many times each word appears in the list.

#     Args:
#         words (list of str): List of words (case-sensitive).

#     Returns:
#         dict: Mapping each word to its frequency.
#     """
#     counts = {}
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
#     return counts

# def word_count(words):
#     return {w: words.count(w) for w in set(words)}

# def wordcount(*args):
#     counter ={}
#     for word in args:

#      if word in counter :
#         counter [word] +=1
#     else:
#         counter [word]=1

#         print(counter)

        

        # word_Count("ELLA, ELLA ,CHIDERA,DAVID")

       


# keys = ["oakely", "oakely", "jenny", "emma", "ella", "jenny", "jenny","ella"]

# counts = {}
# for item in keys:
#     if item in counts:
#         counts[item] += 1
#     else:
#         counts[item] = 1

# highest = 0
# list_of_highest_word = []
# for key, count in counts.items():
#     if count > highest:
#         highest = count
#         list_of_highest_word = []

#     if count == highest:
#         list_of_highest_word.append(key)
# if len(list_of_highest_word) > 1:
#     print("-".join(list_of_highest_word), f"--> Occuring {highest} time each")
# else:
#     print(list_of_highest_word[0], f"--> Occuring {highest} time")
    





        