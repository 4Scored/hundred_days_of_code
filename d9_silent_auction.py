# silent auction

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

def find_highest_bidder(bid_dict): # could also use max(...)
    highest_bidder = ''
    largest_bid = 0
    for bid in bid_dict:
        bid_amt = bid_dict[bid]
        if bid_amt > largest_bid:            
            largest_bid = bid_amt
            highest_bidder = bid
    print('\n'*100) # 
    print(f"The winner is {highest_bidder} with a bid of {largest_bid}.")

bids = {}
print(f"{logo}\nWelcome to the secret auction program.")
name = input("What is your name?: ")
n_bid = int(input("What's your bid?: "))
bids[name] = n_bid
more_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n")

while more_bids == 'yes':
    print('\n'*100)
    name = input("What is your name?: ")
    n_bid = int(input("What's your bid?: "))
    bids[name] = n_bid
    more_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n")

find_highest_bidder(bids)