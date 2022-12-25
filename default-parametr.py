def selamlama(isim, mesaj):
    print(f"{isim} {mesaj}")

selamlama("ibo","günaydın")
#burda bir fonksiyona parametre tanımladık 
#tanımladığımız parametre için karşılıkları yazdık
#eğer bir parametre için karşılık yazmazsak hata alırız


def selam(isim, message="Günaydın"):
    print(f"{isim} {message}")

selam("ibo")

#burda bir default parametre tanımladık biz bir parametreye değer
#yazmadığımızda default parametreye girdiğimiz değer dönecektir
#biz farklı bir değer atamayana kadar böyle devam eder

def toplam(a,b):
    return a+b

def cikarma(a,b):
    return a-b

def islem(a,b,fn=toplam):
    return fn(a,b)

sonuc = islem(3,4)

print(sonuc)

#burda bir fonksiyonu başka bir foonksiyona parametre olarak gönderebileceğimizi gösterdik