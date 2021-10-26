def over_age(data,getter):
    return getter(data)>=18

user={'name':'raghu','age':15}

print(over_age(user,lambda data:int(data['age'])))