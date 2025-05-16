import conversions as conv
#funkcje obliczające parametry adresowe dla podanego adresu IPv4 hosta i maski podsieci
#parametry: 
# 1. adres sieci
# 2. adres rozgłoszeniowy
# 3. adresy uzyteczne hostów
# 4. liczba hostów w sieci
# 5. długość prefixu (liczba 1 w masce podsieci)
# program powinien zwracać te dane w postaci słownika
class InvalidOctetsNumber(Exception):
	pass
class InvalidOctetValue(Exception):
    pass
class NetmaskDiscontinuous(Exception):
	pass

def ToList(IPv4Address:str) -> list:
    #"192.168.10.15" -> [192,168,10,15]
    list = IPv4Address.split('.')
    list2 = []
    for octet in list:
        try:
            list2.append(int(octet))
        except ValueError as ve:
            list2.append(0)
            raise InvalidOctetValue("Oktet zawiera nieprawidłowe znaki: ", octet)
    return list2


def ToDotDec(list: list) -> str:
    str2 = ""
    for i in range(len(list)):
        str2 += str(list[i])
        if i < len(list)-1:
            str2 += "."
    return str2
    #192.168.10.15

def ValidateIPv4Address(IPv4Address: int|str|list) -> bool:
    #rozpoznawanie typu przekazanego argumetu
    #int - liczba 32-bit, spr czy <= 2**32
    #str - dot dec - zamienić na listę
    #list - walidujemy listę:
    #sprawdzamy, czy zawiera dokładnie 4 oktety
    #sprawdzamy czy każdy oktet zawiera wartości od 0 do 255
    
    #jeżeli podano adres IPv4 w postaci kropkowo-dziesiętnej
	octets = []
	if type(IPv4Address) == str: 
		octets = ToList(IPv4Address)
	#jeżeli podano adres IPv4 w postaci listy oktetów
	elif type(IPv4Address) == list:
		octets = IPv4Address
	elif type(IPv4Address) == int:
		if IPv4Address <= conv.AnyToDec(32*"1",2): return True
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
	finally:
		pass

#zamienia na 32-bitową liczbę dziesiętną 
def IPv4AddressToDec(IPv4Address):
	if ValidateIPv4Address(IPv4Address):
		if type(IPv4Address) == str: 
			listOfOctets = ToList(IPv4Address)
		elif type(IPv4Address) == list:
			listOfOctets = IPv4Address
		elif type (IPv4Address) == int: 
			return IPv4Address & conv.AnyToDec(32*"1",2)

		IPv4AddressDec = 0
		for i in range(len(listOfOctets)):			
			IPv4AddressDec += listOfOctets[i]
			if i < 3: 
				IPv4AddressDec <<= 8
		return IPv4AddressDec

#zamiana adresu IPv4 na liczbę binarną
def IPv4AddressToBin(IPv4Address):
	if ValidateIPv4Address(IPv4Address):
		return conv.DecToAny(IPv4AddressToDec(IPv4Address), 2, 32)		
	else:
		return 32*"0"

#funkcja przekształca adres IPv4 w postaci dziesiętnej na listę oktetów
def IPv4AddressToList(ipv4Address):
	#sprawdzamy, czy podany adres IPv4 już jest listą
	if type(ipv4Address) == list:
		if ValidateIPv4Address(ipv4Address):
			return ipv4Address
	
	ipv4AddressDec = IPv4AddressToDec(ipv4Address)
	
	octets = []
	for i in range(4):
		#zapisywanie ostatnich 8 bitów do zmiennej octet i dodanie jej do listy
		octet = ipv4AddressDec & 255
		octets.insert(0, octet)
		#przesuwanie liczby ipv4AddressDec o 8 bitów w prawo
		ipv4AddressDec >>= 8
	
	return octets

# funkcja przekształca adres IPv4 na format kropkowo-dziesiętny
def GetIPv4AddressDotDec(IPv4Address):
	return ToDotDec(IPv4AddressToList(IPv4Address))

# Walidacja maski podsieci
def ValidateIPv4Netmask(IPv4Netmask):
	if ValidateIPv4Address(IPv4Netmask):
		#walidacja ciągłości maski podsieci. 
		#Maska podsieci składa się z sekwencji binarnych jedynek i następujących po nich zer.
		#jeśli w masce wystąpi sekwencja 01, maska jest nieciągła
		netmaskBin = IPv4AddressToBin(IPv4Netmask)
		
		try:
			#znajdź sekwencję 01 w masce podsieci
			#jeśli sekwencja 01 zostanie znaleziona, rzuć wyjątek NetmaskDiscontinuous
			#jeśli sekwencja 01 nie zostanie znaleziona, metoda index() rzuca wyjątek ValueError
			#przechwytujemy ten wyjątek i zwracamy True, co oznacza, że maska jest prawidłowa
			index = netmaskBin.index("01")
			
			if index >= 0:
				raise NetmaskDiscontinuous("Brak ciągłości maski na bicie", index + 1)
		except ValueError as ve:
			if ve.args[0] == "substring not found":
				return True
		#return True

# Obliczanie długości prefixu (liczba binarnych 1 w masce)
def GetIPv4NetmaskPrefixLength(IPv4Netmask: str|list|int) -> int:
	if ValidateIPv4Netmask(IPv4Netmask):
		netmaskDec = IPv4AddressToDec(IPv4Netmask)
		
		bit=0
		prefixLength = 32		
		while bit == 0:
			bit = netmaskDec & 1
			if bit == 0:
				prefixLength -= 1
			netmaskDec >>= 1
		return prefixLength
	
def GetIPv4NetmaskFromPrefixLength(prefixLength: int) -> int:
	if prefixLength >0 and prefixLength <=32:
		netmaskBin = prefixLength*"1" + (32 - prefixLength)*"0"
		return conv.AnyToDec(netmaskBin, 2)
	else:
		raise ValueError("Nieprawidłowa długość prefixu maski podsieci")
		

# Funkcja zwraca informacje na temat adresacji IPv4 sieci, do której należy podany adres i maska podsieci
def NetworkInfo(IPv4Address: str|list|int, IPv4Netmask: str|list|int) -> dict:	
	
	addressDec = IPv4AddressToDec(IPv4Address)
	netmaskDec = IPv4AddressToDec(IPv4Netmask)

	# obliczanie adresu sieci jako iloczynu logicznego adresu IP i maski podsieci
	networkAddressDec = addressDec & netmaskDec
	
	broadcastAddressDec = int(networkAddressDec | (~netmaskDec + (1 << 32)))
	
	firstHostAddressDec = networkAddressDec + 1
	lastHostAddressDec = broadcastAddressDec - 1
	
	# Obliczanie długości prefixu (liczba binarnych 1 w masce)
	
	prefixLength = GetIPv4NetmaskPrefixLength(IPv4Netmask)
			
		
	# budowanie słownika
	network = {}
	network['networkAddress'] = IPv4AddressToList(networkAddressDec)
	network['netmask'] = IPv4AddressToList(netmaskDec)
	network['prefixLength'] = prefixLength
	network['firstAddress'] = IPv4AddressToList(firstHostAddressDec)
	network['lastAddress'] = IPv4AddressToList(lastHostAddressDec)
	network['broadcastAddress'] = IPv4AddressToList(broadcastAddressDec)
	network['hostsNumber'] = (broadcastAddressDec - networkAddressDec - 1)

	return network


print(NetworkInfo('192.168.15.10','255.255.255.0'))