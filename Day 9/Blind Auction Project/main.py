from art import logo
print(logo)
bids = {}
are_there_more_bidders = True

while are_there_more_bidders:
    # TODO-1: Ask the user for input
    name = input("What is your name? ")
    price = int(input("What's your bid?: $"))
    # TODO-2: Save data into dictionary {name: price}
    bids[name] = price
    # TODO-3: Whether if new bids need to be added
    more_bidders = input("Are there any oter bidders? Type 'yes' or 'no'").lower()
    print("\n" * 100)
    if more_bidders == 'no':
        are_there_more_bidders = False

# TODO-4: Compare bids in dictionary
max_bid = max(bids, key=bids.get)
print(f"The winner is {max_bid} with a bid of ${bids[max_bid]}")

