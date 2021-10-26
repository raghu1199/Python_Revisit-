import random
lottery_numbers=set(random.sample(range(1,30),6))
print("lottery nums:",lottery_numbers)

players=[
    {'name':'Raghu','numbers':{23,5,26,29,28,16}},
      {'name':'Abhijit','numbers':{13,5,16,19,8,16}},
        {'name':'Mukul','numbers':{11,15,26,20,3,6}},
]

prev_matched_nums=len(lottery_numbers.intersection(players[0]['numbers']))
prev_name=players[0]['name']
print(prev_matched_nums,",",prev_name)

for player in players:
    matched_nums=len(lottery_numbers.intersection(player['numbers']))
    if matched_nums>prev_matched_nums:
        prev_name=player['name']
        prev_matched_nums=matched_nums

print(f"{prev_name} wins the lottery with {prev_matched_nums} correct hits")
