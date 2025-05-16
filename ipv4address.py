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
            if type(address) == str: 
                octets = ToList(address)
        #jeżeli podano adres IPv4 w postaci listy oktetów
            elif type(address) == list:
                octets = address
            elif type(address) == int:
                if address <= conv.AnyToDec(32*"1",2): return True
                else: raise ValueError("Nieprawidłowa wartość dziesiętna adresu IPv4")    
            try:
            #sprawdzamy, czy liczba oktetów jest prawidłowa
                if len(octets) < 4:
                    raise InvalidOctetsNumber("Za mało oktetów", len(octets))
                if len(octets) > 4:
                    raise InvalidOctetsNumber("Za dużo oktetów", len(octets))
            #sprawdzamy, czy każdy oktet ma prawidłową wartość (między 0 a 255)
                for i in range(len(octets)):
                    if octets[i] < 0 or octets[i] > 255:
                        raise InvalidOctetValue("Nieprawidłowa wartość oktetu", (i + 1), octets[i])
            return True

    def __ToList(self, IPv4AddressDotDec):
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
    def __ToDotDec(self, list):
        pass
    #zamienia na 32-bitową liczbę dziesiętną 
    def _IPv4AddressToDec(self, IPv4Address):
        pass
    #zwraca reprezentację dziesiętną adresu
    def GetDec(self):
        pass
    #zamiana adresu IPv4 na liczbę binarną
    def GetBin(self):
	    return conv.DecToAny(IPv4AddressToDec(IPv4Address), 2, 32)		
    #funkcja przekształca adres IPv4 w postaci dziesiętnej na listę oktetów
    def GetList(self):			
        pass
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
    # funkcja przekształca adres IPv4 na format kropkowo-dziesiętny
    def GetDotDec(self):
        pass
    #reprezentacja łańcuchowa
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
		print("Podana wartość wejściowa zawiera cyfry nie występujące w {} systemie liczbowym.".format(srcBase))
		return None
IPv4Address("192.168.0.1")

print ('jsjsjs')
