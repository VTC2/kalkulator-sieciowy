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
    
        if self.__ValidateIPv4Address(address):
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

        #jeżeli podano adres IPv4 w postaci kropkowo-dziesiętnej
        octets = []

    def ToList(self, IPv4AddressDotDec):
        #"192.168.10.15" -> [192,168,10,15]
        list = self.address.split('.')
        list2 = []
        for octet in list:
            try:
                list2.append(int(octet))
            except ValueError as ve:
                list2.append(0)
                raise InvalidOctetValue("Oktet zawiera nieprawidłowe znaki: ", octet)
        return list2
    def GetDotDec(self, lista):
        return str(lista[0]) + "." + str(lista[1]) + "." + str(lista[2]) + "." + str(lista[3])

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
    def ToList(self, IPv4AddressDotDec):
        try:
            parts = IPv4AddressDotDec.split('.')
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
    def __str__(self):
        pass

    #zwraca adres w postaci łańcucha, address/prefix-length, np.
    def AnyToDec(strVal, srcBase):
        #sprawdzenie, czy wartość wejściowa = None
        if strVal == None:
            print("Nie podano wartości wejściowej.")
            return None
        #sprawdzenie, czy podana wartość zawiera dozwolone cyfry w podanym systemie liczbowym
        #w przeciwnym wypadku zwraca None

        for i in range(len(strVal)):
            if strVal[i].isdigit():
                dec += int(strVal[i]) * srcBase ** (len(strVal) - i - 1)
            elif ord('A') <= ord(strVal[i]) <= ord('Z'):
                dec += int(ord(strVal[i]) - ord('A') + 10) * srcBase ** (len(strVal) - i - 1)
            return dec
        else:
            print("Podana wartość wejściowa zawiera cyfry nie występujące w tym systemie liczbowym.")
            return None
IPv4Address("192.168.0.1")

print ('jsjsjs')
