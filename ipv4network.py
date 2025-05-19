import ipv4address as maddr
import ipv4netmask as mmask

def __init__(self, address, netmask):
		self.address = maddr.IPv4Address(address)		
		self.netmask = mmask.IPv4Netmask(netmask)
		#obliczenie adresu sieci, na wypadek, gdyby podano adres hosta
		self.address.address &= self.netmask.address

def __str__(self):
	#zwraca adres w postaci łańcucha, address/prefix-length, np. 192.168.10.0/24

# Funkcja zwraca informacje na temat adresacji IPv4 sieci, do której należy podany adres i maska podsieci
	def GetNetworkInfo(self) -> dict:	
		pass