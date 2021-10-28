from firebase import firebase
Firebase=firebase.FirebaseApplication("https://basic-99cca-default-rtdb.firebaseio.com/",None)
data={
'Time': ['5646','76576'],
}
rfid='234567'
res=Firebase.post(f"basic-99cca-default-rtdb/Employee/{rfid}",data)
print(res)