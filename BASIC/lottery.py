
lottery={13,26,14,15,21,16}

players=[
    {'name':'Raghu',
    'numbers':{13,56,78,15,21} 
    },
     {'name':'Rahul',
    'numbers':{12,56,78,15,21} 
    },
     {'name':'Ashu',
    'numbers':{13,56,21,15,14} 
    },
]
print(lottery)
print()
d=0
winner=""
for item in players:
    player=item['name']
    nums=item['numbers']
    rnums=nums.intersection(lottery)
    print("right nums:",rnums)
    print("player {} got {} numbers right".format(player,len(rnums)))
    if len(rnums)>d:
        d=len(rnums)
        winner=player
    
    print()

print("Lucky draw winner is {} and his got {} numbers right matched".format(winner,d) )

