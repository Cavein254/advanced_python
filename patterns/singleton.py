class Singleton(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            instance = super().__call__(*args, **kwargs)
            self._instances[self] = instance
        return self._instances[self]


class NetworkDriver(metaclass=Singleton):
    def log(self):
        print(f"{self}\n")


def create_singleton():
    singleton = NetworkDriver()
    singleton.log()
    return singleton

if __name__=='__main__':
    for i in range(10):
        create_singleton()
