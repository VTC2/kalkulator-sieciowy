import ipv4address as maddr
import ipv4netmask as mmask

class IPv4Network():
	
	def __init__(self, address, netmask):
		self.address = maddr.IPv4Address(address)		
		self.netmask = mmask.IPv4Netmask(netmask)
		#obliczenie adresu sieci, na wypadek, gdyby podano adres hosta
		self.address.address &= self.netmask.address
		
	def __str__(self):
		return f"{self.address}/{self.netmask.GetPrefixLength()}"
	# Funkcja zwraca informacje na temat adresacji IPv4 sieci, do której należy podany adres i maska podsieci
	def GetNetworkInfo(self) -> dict:	
		
		
		# obliczanie adresu sieci jako iloczynu logicznego adresu IP i maski podsieci
		networkAddress = maddr.IPv4Address(self.address.GetDec() & self.netmask.GetDec())
		
		broadcastAddress = maddr.IPv4Address(int(networkAddress.GetDec() | (~self.netmask.GetDec() + (1 << 32))))
		
		firstHostAddress = maddr.IPv4Address(networkAddress.GetDec() + 1)
		lastHostAddress = maddr.IPv4Address(broadcastAddress.GetDec() - 1)
		
		# Obliczanie długości prefixu (liczba binarnych 1 w masce)
		prefixLength = self.netmask.GetPrefixLength()		
		# budowanie słownika
		network = {}
		network['networkAddress'] = networkAddress.GetList()
		network['netmask'] = self.netmask.GetList()
		network['prefixLength'] = prefixLength
		network['firstAddress'] = firstHostAddress.GetList()
		network['lastAddress'] = lastHostAddress.GetList()
		network['broadcastAddress'] = broadcastAddress.GetList()
		network['hostsNumber'] = (broadcastAddress.GetDec() - networkAddress.GetDec() - 1)

		return network
	
if __name__ == '__main__':
	net = IPv4Network('192.168.15.10','255.255.252.0')
	print(net)
	print(net.GetNetworkInfo())
