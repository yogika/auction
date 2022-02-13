from replit import clear
from art import logo
print(logo)
emty_dic={}
bidding=False
def bidder(bid_prize):
  height_bid=0
  winner=""
  for bidder in bid_prize:
    bidder_amount=bid_prize[bidder]
    if bidder_amount>height_bid:
      height_bid=bidder_amount
      winner=height_bid
  print(f"Winner is {bidder} with the bid of ${height_bid}")    


 
while not bidding:
  name=input("what is your name?:")
  bid_prize=int(input("what is your bid?: $"))
  emty_dic[name]=bid_prize
  should_cuntinue=input("Are ther any one to bid? type yes or no:")
  if should_cuntinue=="no":
    bidding=True
    bidder(emty_dic)
  elif should_cuntinue=="yes":
    clear()
