# Udemy 43.Ders Ödev-2

## Kullanıcıdan Girilen Sayı Armstrong Sayı Mıdır Değil Midir?

<b>-Biraz uzun bir açıklama olacak-</b>

* İlk önce kullanıcıdan bir sayı girmesini istiyoruz.
* Armstrong Sayıya Örnek: 153 yani (1 * 1 * 1) + (5 * 5 * 5) + (3 * 3 * 3) = 153 yani 1 üzeri 3 + 5 üzeri 3 + 3 üzeri 3 = 153
* Yani girilen sayının basamağı üs rakamımızı belirliyor, sonra her basamağı bu belirlenen üs rakamıyla üssünü alıyoruz ve çıkan sonuçları topladığımızda toplam girilen sayıya eşit oluyor.
* Gelelim kod yapımıza; aslında daha kısa versiyonları da var ancak şimdilik başlangıç seviyesinde olduğum için kendim anladığım şekilde yazmaya çalıştım kodları yoksa listte append fonksiyonunu kullanabiliriz ve list comprehension metodunu kullanabiliriz vs.

* ilk önce kullanıcıdan bir sayı girildi.
* Bu sayıyı, geçici bir sayıya atadık.(Sebebi: sayı ile ayrıca işlemimiz olduğundan sayıyı etkilememek için geçici sayıyla işimizi göreceğiz.)
* Daha sonra toplam diye bir değişken oluşturduk ve 0 değerini verdik.
* while döngüsüne aldık bunun nedeni sayıyı basamaklarına göre azaltacağız, yani örn: 153, 3 basamaklı bir sayıyı 10 böldüğümüzde geriye 15 kalıyor(yani 2 basamak), tekrar 10 bölüyoruz geriye 1 kalıyor (yani 1 basamak) vs.
* Geçici sayı için de benzer ancak burda kalanı işimize yarayacak 153'ü 10'a böldüğümüzde kalan 3.
* <b>Burada araya girerek:</b> sayıyı stringe çevirdim, sonra liste çevirdim ve list1 değişkenine atadım. Çünkü toplama kalan sayıyı yani 3'ü sayının uzunluğu kadar çarpacağım. Sonra 5'i sayının uzunluğu kadar çarpacağım, sonra 1'i sayının uzunluğu kadar çarpacağım. Sonra bunlar hep toplam değişkenine eklenecek.
* <b>Tada!</b> Sayımızın üssünü rakamlarına aldırıp toplayıp toplam sayımızı elde ettik, en sonunda da girinti olarak bir geriye gelip bunları karşılaştırdık, while döngüsünün içinde kalsaydı bu if-else koşulu program doğru çalışmazdı.