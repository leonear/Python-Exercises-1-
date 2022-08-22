voo = input()
pessoas = int (input())

if (voo == "D") and (pessoas <=50.00 ):
    totalapagar =(pessoas * 200.00)

if (voo == "D") and (pessoas >50.00 ):
    totalapagar =(pessoas * 120.00)

if (voo == "N") and (pessoas <=50.00 ):
    totalapagar =(pessoas * 100.00)

if (voo == "N") and (pessoas >50.00 ):
    totalapagar = (pessoas * 80.00)

print("%.2f" % totalapagar)
    
