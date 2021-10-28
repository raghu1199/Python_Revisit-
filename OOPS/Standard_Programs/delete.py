from firebase import firebase
Firebase=firebase.FirebaseApplication("https://basic-99cca-default-rtdb.firebaseio.com/",None)
res=Firebase.delete("basic-99cca-default-rtdb/Employee/","-MVopukoo2xt69Mqk6YO")
print("Deleted success")