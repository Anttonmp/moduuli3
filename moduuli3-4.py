vuosi = int(input("Anna vuosi "))
if vuosi % 4 == 0 and (vuosi % 100 == 0 or vuosi % 400 != 0):
    print("Annettu vuosi on karkausvuosi. ")
elif vuosi % 3 == 0 and (vuosi % 100 == 0 or vuosi % 300 != 0):
    print("Annettu vuosi ei ole karkausvuosi. ")
elif vuosi % 2 == 0 and (vuosi % 100 == 0 or vuosi % 200 != 0):
    print("Annettu vuosi ei ole karkausvuosi. ")
elif vuosi % 1 == 0 and (vuosi % 100 == 0 or vuosi % 100 != 0):
    print("Annettu vuosi ei ole karkausvuosi. ")
else:
    print("Annettu vuosi ei ole karkausvuosi. ")








