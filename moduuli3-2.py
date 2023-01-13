hytti = input("Mikä on hyttiluokkasi?: ")
lux = "lux"
a = "a"
b = "b"
c = "c"

if hytti == lux:
    print("lux on parvekkeellinen hytti yläkannella. ")
elif hytti == a:
    print("Ikkunallinen hytti autokannen yläpuolella. ")
elif hytti == b:
    print("luokkaikkunaton hytti autokannen yläpuolella. ")
elif hytti == c:
    print("c on ikkunaton hytti autokannen alapuolella. ")
else:
    print("Virheellinen hyttiluokka. ")