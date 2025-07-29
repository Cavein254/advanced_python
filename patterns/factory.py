from abc import ABC, abstractmethod

class Country:
    pass

class USA(Country):
    pass

class Spain(Country):
    pass

class Japan(Country):
    pass


class CurrencyFactory(ABC):
    @abstractmethod
    def currecy_factory(self, country)-> str:
        pass


class FiatCurrecyFactory(CurrencyFactory):
    def currecy_factory(self, country)->str:
        if country is USA:
            return "USD"
        elif country is Spain:
            return "Euro"
        else:
            return "JYP"


class VirtualCurrecyFactory(CurrencyFactory):
    def currecy_factory(self, country)->str:
        if country is USA:
            return "Bitcoin"
        elif country is Spain:
            return "Etherium"
        else:
            return "Dogecoin"


if __name__=="__main__":
    f1=FiatCurrecyFactory()
    f2=VirtualCurrecyFactory()


    print(f1.currecy_factory(USA))
    print(f1.currecy_factory(Spain))
    print(f1.currecy_factory(Japan))



    print(f2.currecy_factory(USA))
    print(f2.currecy_factory(Spain))
    print(f2.currecy_factory(Japan))
