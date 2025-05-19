import conversions as conv
import ipv4address as addr

class NetmaskDiscontinuous(Exception):
	pass

class IPv4Netmask(addr.IPv4Address):
	
	def __init__(self, netmask):
		if self.__ValidateIPv4Netmask(netmask):
			super().__init__(netmask)


	# Walidacja maski podsieci
	def __ValidateIPv4Netmask(self, IPv4Netmask):
		if super()._ValidateIPv4Address(IPv4Netmask):
			#walidacja ciągłości maski podsieci. 
			#Maska podsieci składa się z sekwencji binarnych jedynek i następujących po nich zer.
			#jeśli w masce wystąpi sekwencja 01, maska jest nieciągła
			netmaskBin = conv.DecToAny(super()._IPv4AddressToDec(IPv4Netmask), 2, 32)
			
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
			

	# Obliczanie długości prefixu (liczba binarnych 1 w masce)
	def GetPrefixLength(self) -> int:
		
		netmaskDec = self.address		
		bit=0
		prefixLength = 32		
		while bit == 0:
			bit = netmaskDec & 1
			if bit == 0:
				prefixLength -= 1
			netmaskDec >>= 1
		return prefixLength
	
	def SetIPv4NetmaskFromPrefixLength(self, prefixLength: int) -> int:
		if prefixLength > 0 and prefixLength <= 32:
			netmaskBin = prefixLength*"1" + (32 - prefixLength)*"0"
			self.address = conv.AnyToDec(netmaskBin, 2)
		else:
			raise ValueError("Nieprawidłowa długość prefixu maski podsieci")