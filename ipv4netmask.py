import ipv4address as addr

class IPv4Netmask(addr.IPv4Address):

    def __init__(self, netmask):
        if self.__ValidateIPv4Netmask(netmask):
            super().__init__(netmask)
    
    # Walidacja maski podsieci
    def __ValidateIPv4Netmask(self, IPv4Netmask):
        pass

    # Obliczanie długości prefixu (liczba binarnych 1 w masce)
    def GetPrefixLength(self) -> int:
        pass

    def SetIPv4NetmaskFromPrefixLength(self, prefixLength: int) -> int:
        pass