import random

while True:
    a = input("tas , kagit, makas ? Hangisi:")
    b=["tas","kagit","makas"]
    select=random.choice(b)
    print("Benim Secimim", select)
    if a=="tas" and select=="makas":
        print("Tas Makasi siker atar")
        break
    elif  a=="makas" and select=="kagit":
        print("Makas Kagidi keser")
        break
    elif  a == "kagit" and select == "tas":
        print("Kagit tasi Sarar")
        break
    print("Kaybettin!")



