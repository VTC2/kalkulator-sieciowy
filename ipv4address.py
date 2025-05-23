import conversions as conv
class InvalidOctetsNumber(Exception):
        pass
class InvalidOctetValue(Exception):
    pass
class NetmaskDiscontinuous(Exception):
    pass
class IPv4Address():
    address = 0

    #konstruktor
    def __init__(self, address):
    
        if self.__ValidateIPv4Address():
            self.address = address
            print("git")
    #metoda
    def __ValidateIPv4Address(address):
        #rozpoznawanie typu przekazanego argumetu
        #int - liczba 32-bit, spr czy <= 2**32
        #str - dot dec - zamienić na listę
        #list - walidujemy listę:
        #sprawdzamy, czy zawiera dokładnie 4 oktety
        #sprawdzamy czy każdy oktet zawiera wartości od 0 do 255
        pass
        #sjeżeli podano adres IPv4 w postaci kropkowo-dziesiętnej
        octets = []

    def GetDotDec(self):
        temp = self.ToList()
        return str(temp[0]) + "." + str(temp[1]) + "." + str(temp[2]) + "." + str(temp[3])

    #zamienia na 32-bitową liczbę dziesiętną 
    def _IPv4AddressToDec(self, IPv4Address):
        pass
    #1 zwraca reprezentację dziesiętną adresu
    #2 funkcja przekształca adres IPv4 na format kropkowo-dziesiętny
    #nie wiem czy to sie rozni (po co nam jakas ogrmona miliardowa lliczba dziesietna)
    def GetDec(self):
        return self._IPv4AddressToDec(self.address)
   
   
   
   
    #zamiana adresu IPv4 na liczbę binarną
    def GetBin(self):
        return conv.DecToAny(self.IPv4AddressToDec(IPv4Address), 2, 32)  
        
    
   
   
   
   
   
   
   
    #funkcja przekształca adres IPv4 w postaci dziesiętnej na listę oktetów      
    def ToList(self):
        try:
            parts =  self.address.split('.')
            if len(parts) != 4:
                raise InvalidOctetsNumber("Adres musi zawierać dokładnie 4 oktety")
            
            octets = []
            for part in parts:
                val = int(part)
                if not (0 <= val <= 255):
                    raise InvalidOctetValue("za duzo")
                octets.append(val)
            return octets

        except ValueError:
            raise InvalidOctetValue("ktos to wpisal cos czego nie pownny tu byc")

   
    #reprezentacja łańcuchowa  #nie wiem co to znaczy
    # def __str__(self):
      #  pass

    #zwraca adres w postaci łańcucha, address/prefix-length, np.
    def AnyToDec(strVal, srcBase):
        #sprawdzenie, czy wartość wejściowa = None
        if strVal == None:
            print("Nie podano wartości wejściowej.")
            return None
        #sprawdzenie, czy podana wartość zawiera dozwolone cyfry w podanym systemie liczbowym
        #w przeciwnym wypadku zwraca None
#jeżeli dima lub abdul tu byli to usuną ten napis
        for i in range(len(strVal)):
            if strVal[i].isdigit():
                dec += int(strVal[i]) * srcBase ** (len(strVal) - i - 1)
            elif ord('A') <= ord(strVal[i]) <= ord('Z'):
                dec += int(ord(strVal[i]) - ord('A') + 10) * srcBase ** (len(strVal) - i - 1)
            return dec
        else:
            print("Podana wartość wejściowa zawiera cyfry nie występujące w tym systemie liczbowym.")
            return None
ip = IPv4Address("192.168.0.1")

print(ip.GetDotDec())
print(ip.ToList())



print ('jsjsjs')