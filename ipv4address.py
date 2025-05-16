import conversions as conv

class IPv4Address():
    address = 0
    
    #konstruktor
    def __init__(self, address):
        
        if self.__ValidateIPv4Address(address):
            self.address = address
    #metoda
    def __ValidateIPv4Address(self, IPv4Address):
        pass

    def __ToList(self, IPv4AddressDotDec):

    def __ToDotDec(self, list):
    #funkcja walidująca podany na wejście adres IPv4
	def _ValidateIPv4Address(self, IPv4Address):
    
    #zamienia na 32-bitową liczbę dziesiętną 
	def _IPv4AddressToDec(self, IPv4Address):
    
    #zwraca reprezentację dziesiętną adresu
	def GetDec(self):
    
    #zamiana adresu IPv4 na liczbę binarną
	def GetBin(self):
    
    #funkcja przekształca adres IPv4 w postaci dziesiętnej na listę oktetów
	def GetList(self):			
    
    # funkcja przekształca adres IPv4 na format kropkowo-dziesiętny
	def GetDotDec(self):
    
    #reprezentacja łańcuchowa
	def __str__(self):