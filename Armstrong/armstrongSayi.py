# Problem 2:

print("""*******************************
Armstrong Sayıyı Bulma Programı    
*******************************""")

sayi = int(input("Bir Sayı Giriniz: "))

toplam = 0

geciciSayi = sayi

list1 = []

while (geciciSayi > 0 ):
  
  kalan = geciciSayi % 10
  
  list1 = list(str(sayi))
  
  toplam += kalan ** len(list1)
  
  geciciSayi //= 10
  
if (toplam == sayi):
    
  print("{} Armstrong Bir Sayıdır.".format(sayi))
    
else:
  print("{} Armstrong Bir Sayı Değildir.".format(sayi))


