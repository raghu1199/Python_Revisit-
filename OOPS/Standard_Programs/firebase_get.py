from firebase import firebase
Firebase=firebase.FirebaseApplication("https://basic-99cca-default-rtdb.firebaseio.com/",None)
res=Firebase.get("basic-99cca-default-rtdb/Employee","")
print(res)