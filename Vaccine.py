print("AstarZeneca >> AZ")
print("Sinovac >> SV")
print("Infection >> Y")
print("No Infection >> N")
print("Sinopharm >> SP")
print("Not Vaccine >> NV")
print("I have gotten vaccine >> Get")
print("I have not  gotten vaccine >> Not Get")

Frist = input("Frist Vaccine: ")
Second = input("Second Vaccine: ")
Third = input("Third Vaccine: ")
Infection = input("COVID - INFECTION:")
Vaccine = input("Have you get vaccine?")


if(Vaccine == "Get"):

    if(Frist == "SV" and Second == "SV" and Third == "NV"): print("GET 1 PFIZER")
    elif(Frist == "SP" and Second == "SP" and Third == "NV"): print("GET 1 PFIZER")
    elif(Frist == "SV" and Second == "NV" and Third == "NV"): print("GET 1 PFIZER")
    elif(Frist == "AZ" and Second == "NV" and Third == "NV"): print("GET 1 PFIZER")
    elif(Frist == "SP" and Second == "NV" and Third == "NV"): print("GET 1 PFIZER")
    elif(Frist == "SV" and Second == "SV" and Third == "AZ"): print("SORRY,YOU DON'T GET PFIZER")
    elif(Frist == "SV" and Second == "AZ" and Third == "NV"): print("SORRY,YOU DON'T GET PFIZER")
    elif(Frist == "AZ" and Second == "AZ" and Third == "NV"): print("SORRY,YOU DON'T GET PFIZER")
    else: print("ERROR!!")

else:
    if(Vaccine == "Not get" and Infection == "Y"): print("GET 1 PFIZER")
    elif(Vaccine == "Not get" and Infection == "N"): print("GET 2 PFIZER")
    else: print("ERROR!!!")