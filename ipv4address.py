import conversions as conv
class InvalidOctetsNumber(Exception):
    	pass
class InvalidOctetValue(Exception):
    pass
class NetmaskDiscontinuous(Exception):
	pass
class IPv4Address():

	def __init__(self, address):
		self.address = self._IPv4AddressToDec(address)
		
		pass

	def __ToList(self, IPv4AddressDotDec):
		list = IPv4AddressDotDec.split(".")
		list2 = []
		for element in list:
			try:
				list2.append(int(element))
			except ValueError as ve:
				#print("Podana wartość nie jest liczbą. Przyjęto 0. Kod:", ve.args)
				list2.append(0)
				raise InvalidOctetValue("Oktet zawiera niedozwolone znaki: " + element,0,0)
		
		return list2
	
	def __ToDotDec(self, list):
		str2 = ""
		for i in range(len(list)):
			str2 += str(list[i])
			if i < len(list)-1:
				str2+="."
		return str2

	#funkcja walidująca podany na wejście adres IPv4
	def _ValidateIPv4Address(self, IPv4Address):
		#jeżeli podano adres IPv4 w postaci kropkowo-dziesiętnej
		octets = []
		if type(IPv4Address) == str: 
			octets = self.__ToList(IPv4Address)
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
	def _IPv4AddressToDec(self, IPv4Address):
		if self._ValidateIPv4Address(IPv4Address):
			if type(IPv4Address) == str: 
				listOfOctets = self.__ToList(IPv4Address)
			elif type(IPv4Address) == list:
				listOfOctets = IPv4Address
			elif type (IPv4Address) == int: 
				return IPv4Address & conv.AnyToDec(32*"1",2)			
			IPv4AddressDec = 0
			for i in range(len(listOfOctets)):
				IPv4AddressDec <<= 8
				IPv4AddressDec += listOfOctets[i]			
			return IPv4AddressDec
	
	#zwraca reprezentację dziesiętną adresu
	def GetDec(self):
		return self.address
	
	#zamiana adresu IPv4 na liczbę binarną
	def GetBin(self):
		return conv.DecToAny(self.address, 2, 32)		
		

	#funkcja przekształca adres IPv4 w postaci dziesiętnej na listę oktetów
	def GetList(self):			
		octets = []
		ipv4AddressDec = self.address
		for i in range(4):
			
			#zapisywanie ostatnich 8 bitów do zmiennej octet i dodanie jej do listy
			octet = ipv4AddressDec & 255
			octets.insert(0, octet)
			#przesuwanie liczby ipv4AddressDec o 8 bitów w prawo
			ipv4AddressDec >>= 8
		
		return octets
	
	

	# funkcja przekształca adres IPv4 na format kropkowo-dziesiętny
	def GetDotDec(self):
		return self.__ToDotDec(self.GetList())
	
	#reprezentacja łańcuchowa
	def __str__(self):
		return f"{self.GetDotDec()}"
		
	



