# Problem 1:

print("""*********************
Mükemmel Sayıyı Bulma Programı    
********************* """)

sayi = int(input("Bir Sayı Giriniz: "))
toplam = 0  
list1 = list(range(1,sayi)) # 1'den girilen sayıya kadar olan sayıların listesini çıkarıyoruz.
if(sayi != 0): # 0 sayısı girilirse mükemmel sayı olmadığını kodluyoruz.
  for i in list1: # 1'den girilen sayıya kadar olan sayıların içerisinde geziniyoruz.

    if (sayi % i == 0): # Yukarıdaki gezintiyi koşula bağlayarak girilen sayıların çarpanlarını buluyoruz.
      toplam += i # Bulduğumuz çarpanları topluyoruz. Aşağıda bu toplamı girilen sayı ile karşılaştıracağız.
      
  if (toplam == sayi): # Girilen sayı ile çarpanlarının toplamı eşitse mükemmel sayıyı bulmuş oluyoruz.
    print(sayi, "Mükemmel Bir Sayıdır.")
    
  else:
    print(sayi, "Mükemmel Bir Sayı Değildir.")
    
else:
    print(sayi, "Mükemmel Bir Sayı Değildir.")
