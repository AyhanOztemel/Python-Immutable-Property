from immutableDecarator import immutable_property

class Circle:
    def __init__(self, radius):
        self.__radius = radius
        
    
    @property
    def radius(self):
        """Dairenin yarıçapını döndürür."""
        return self.__radius
    
    @radius.setter
    @immutable_property 
    def radius(self, value):
        #Dairenin yarıçapını ayarlar.
        if value <= 0:
            raise ValueError("Yarıçap sıfırdan büyük olmalıdır.")
        self.__radius = value

    @property
    def diameter(self):
        """Dairenin çapını döndürür."""
        return 2 * self.__radius
    
    @property
    def circle(self):
        """Dairenin çapını döndürür."""
        return 2 * self.__radius * 3.14

    @property
    def area(self):
        """Dairenin alanını hesaplar."""
        return 3.14 * self.__radius ** 2

# Örnek kullanım
c = Circle(8)
    
print("Yarıçap:", c.radius)
print("Çap:", c.diameter)
print("çevresi:", c.circle)
print("Alan:", c.area)
print("--------------------------")

try:
    c.radius = 5    # !!!HATA VERİR  @immutable_property
except Exception as e:
    e="Hata!!! immutable_property"
    print(e)

c = Circle(10)
print("--------------------------")
print("Yeni yarıçap:", c.radius)
print("Yeni çap:", c.diameter)
print("Yeni çevresi:", c.circle)
print("Yeni alan:", c.area)
