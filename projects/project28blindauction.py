from click import clear

dict = {}


def asking(a):
    user_name = input("Enter Your Name-")
    bid = float(input("Enter Your Bid-"))
    a[user_name] = bid


asking(dict)
request = input("Your Friends also wants to join(Y/N)?")
while request == "Y":
    clear()
    asking(dict)
    request = input("Your Friends also wants to join(Y/N)?")
highest_bid = 0
bidder_name = ""
for key, value in dict.items():
    if value > highest_bid:
        highest_bid = value
        bidder_name = key
print("winner is", bidder_name, "with a bid of ", highest_bid)
