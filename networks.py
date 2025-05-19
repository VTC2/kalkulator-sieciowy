import conversions as conv

class InvalidOctetsNumber(Exception):
	pass
class InvalidOctetValue(Exception):
	pass
class NetmaskDiscontinuous(Exception):
	pass

class Network:

	def __init__(self, IPv4Address, IPv4Netmask):
		
		self.addressDec = self.IPv4AddressToDec(IPv4Address)
		self.netmaskDec = self.IPv4AddressToDec(IPv4Netmask)
		
		self.networkAddressDec = self.addressDec & self.netmaskDec
		
		self.broadcastAddressDec = int(self.networkAddressDec | (~self.netmaskDec + (1 << 32)))
		
		self.firstHostAddressDec = self.networkAddressDec + 1
		self.lastHostAddressDec = self.broadcastAddressDec - 1
		
		self.prefixLength = self.GetIPv4NetmaskPrefixLength(self.netmaskDec)

	@staticmethod
	def ToList(IPv4Address:str) -> list:
		list = IPv4Address.split('.')
		list2 = []
		for octet in list:
			try:
				list2.append(int(octet))
			except ValueError as ve:
				list2.append(0)
				raise InvalidOctetValue("Oktet zawiera nieprawidłowe znaki: ", octet)
		return list2

	@staticmethod
	def ToDotDec(list: list) -> str:
		str2 = ""
		for i in range(len(list)):
			str2 += str(list[i])
			if i < len(list)-1:
				str2 += "."
		return str2

	@staticmethod
	def ValidateIPv4Address(IPv4Address: int|str|list) -> bool:
		octets = []
		if type(IPv4Address) == str:
			octets = Network.ToList(IPv4Address)
		elif type(IPv4Address) == list:
			octets = IPv4Address
		elif type(IPv4Address) == int:
			if IPv4Address <= conv.AnyToDec(32*"1",2): return True
			else: raise ValueError("Nieprawidłowa wartość dziesiętna adresu IPv4")

		try:
			if len(octets) < 4:
				raise InvalidOctetsNumber("Za mało oktetów", len(octets))
			if len(octets) > 4:
				raise InvalidOctetsNumber("Za dużo oktetów", len(octets))
			for i in range(len(octets)):
				if octets[i] < 0 or octets[i] > 255:
					raise InvalidOctetValue("Nieprawidłowa wartość oktetu", (i + 1), octets[i])

			return True
		finally:
			pass

	@staticmethod
	def IPv4AddressToDec(IPv4Address):
		if Network.ValidateIPv4Address(IPv4Address):
			if type(IPv4Address) == str:
				listOfOctets = Network.ToList(IPv4Address)
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

	@staticmethod
	def IPv4AddressToBin(IPv4Address):
		if Network.ValidateIPv4Address(IPv4Address):
			return conv.DecToAny(Network.IPv4AddressToDec(IPv4Address), 2, 32)
		else:
			return 32*"0"

	@staticmethod
	def IPv4AddressToList(ipv4Address):
		if type(ipv4Address) == list:
			if Network.ValidateIPv4Address(ipv4Address):
				return ipv4Address

		ipv4AddressDec = Network.IPv4AddressToDec(ipv4Address)

		octets = []
		for i in range(4):
			octet = ipv4AddressDec & 255
			octets.insert(0, octet)
			ipv4AddressDec >>= 8

		return octets

	@staticmethod
	def GetIPv4AddressDotDec(IPv4Address):
		return Network.ToDotDec(Network.IPv4AddressToList(IPv4Address))

	@staticmethod
	def ValidateIPv4Netmask(IPv4Netmask):
		if Network.ValidateIPv4Address(IPv4Netmask):
			netmaskBin = Network.IPv4AddressToBin(IPv4Netmask)

			try:
				index = netmaskBin.index("01")

				if index >= 0:
					raise NetmaskDiscontinuous("Brak ciągłości maski na bicie", index + 1)
			except ValueError as ve:
				if ve.args[0] == "substring not found":
					return True

	@staticmethod
	def GetIPv4NetmaskPrefixLength(IPv4Netmask: str|list|int) -> int:
		if Network.ValidateIPv4Netmask(IPv4Netmask):
			netmaskDec = Network.IPv4AddressToDec(IPv4Netmask)

			bit=0
			prefixLength = 32
			while bit == 0:
				bit = netmaskDec & 1
				if bit == 0:
					prefixLength -= 1
				netmaskDec >>= 1
			return prefixLength

	@staticmethod
	def GetIPv4NetmaskFromPrefixLength(prefixLength: int) -> int:
		if prefixLength >0 and prefixLength <=32:
			netmaskBin = prefixLength*"1" + (32 - prefixLength)*"0"
			return conv.AnyToDec(netmaskBin, 2)
		else:
			raise ValueError("Nieprawidłowa długość prefixu maski podsieci")

	def get_info(self) -> dict:
		network = {}
		network['networkAddress'] = self.IPv4AddressToList(self.networkAddressDec)
		network['netmask'] = self.IPv4AddressToList(self.netmaskDec)
		network['prefixLength'] = self.prefixLength
		network['firstAddress'] = self.IPv4AddressToList(self.firstHostAddressDec)
		network['lastAddress'] = self.IPv4AddressToList(self.lastHostAddressDec)
		network['broadcastAddress'] = self.IPv4AddressToList(self.broadcastAddressDec)
		network['hostsNumber'] = (self.broadcastAddressDec - self.networkAddressDec - 1)

		return network


print(Network('192.168.15.10','255.255.255.0').get_info())