"""Bridge design pattern implementation"""


from abc import ABC, abstractmethod


class Device:
    """
    The Device defines the interface for all the device classes. It doesn't
    have to match the Remote's interface. In fact, the two interfaces can be
    entirely different. Typically the Device interface provides only
    primitive operations, while the Remote defines higher-level operations
    based on those primitives.
    """
    @abstractmethod
    def is_enabled(self) -> bool:
        pass

    @abstractmethod
    def enable(self) -> None:
        pass

    @abstractmethod
    def disable(self) -> None:
        pass

    @abstractmethod
    def get_volume(self) -> int:
        pass

    @abstractmethod
    def set_volume(self, volume: int) -> None:
        pass


"""
Each concrete implementation corresponds to a specific platform and implements
the Device interface using that platform's API.
"""


class Radio(Device):

    def __init__(self) -> None:
        self.on = False
        self.volume = 30

    def is_enabled(self) -> bool:
        return self.on

    def enable(self) -> None:
        print("Turning radio on.")
        self.on = True

    def disable(self) -> None:
        print("Turning radio off")
        self.on = False

    def get_volume(self) -> int:
        return self.volume

    def set_volume(self, volume: int) -> None:
        if self.volume > 100:
            self.volume = 100
        elif self.volume < 0:
            self.volume = 0
        else:
            self.volume = volume
        print(f"Set Radio volume {self.volume}")


class Television(Device):

    def __init__(self) -> None:
        self.on = False
        self.volume = 20

    def is_enabled(self) -> bool:
        return self.on

    def enable(self) -> None:
        print("Turning Television on.")
        self.on = True

    def disable(self) -> None:
        print("Turning Television off")
        self.on = False

    def get_volume(self) -> int:
        return self.volume

    def set_volume(self, volume: int) -> None:
        if self.volume > 100:
            self.volume = 100
        elif self.volume < 0:
            self.volume = 0
        else:
            self.volume = volume
        print(f"Set Radio volume {self.volume}")


class Remote(ABC):
    """
    The Remote defines the interface for the 'control' part of the two
    hierarchies. It maintains a reference to an object of the Device hierarchy
    and delegates all of the real work to this object.
    """
    def __init__(self, device: Device) -> None:
        self.device = device

    @abstractmethod
    def power(self) -> None:
        pass

    @abstractmethod
    def volume_up(self) -> None:
        pass

    @abstractmethod
    def volume_down(self) -> None:
        pass


class BasicRemote(Remote):

    def __init__(self, device) -> None:
        super().__init__(device)

    def power(self) -> None:
        print("Remote: power toggle")
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()

    def volume_up(self) -> None:
        print("Remote: volume up")
        self.device.set_volume(self.device.get_volume() + 10)

    def volume_down(self) -> None:
        print("Remote: volume down")
        self.device.set_volume(self.device.get_volume() - 10)


class AdvancedRemote(BasicRemote):
    """
    AdvancedRemote have all the functionalities of BasicRemote and additionally
    have the functionality to mute the device.
    """

    def __init__(self, device) -> None:
        super().__init__(device)

    def mute(self) -> None:
        self.device.set_volume(0)


def client_code(remote: Remote):
    """
    Except for the initialization phase, where an Remote object gets
    linked with specific Device object, the client code should only
    depend on the Remote class. This way client code can support any
    remote-device combination.
    """
    remote.power()
    remote.volume_up()
    remote.volume_down()


if __name__ == "__main__":
    """
    The client code should work with any pre-configured remote-device
    configuration.
    """
    print("Client code with radio & basic remote:")
    radio = Radio()
    remote = BasicRemote(radio)
    client_code(remote)

    print("Client code with television & advanced remote:")
    tv = Television()
    advancedRemote = AdvancedRemote(tv)
    client_code(advancedRemote)

    print("Using advanced remote mute functionality")
    advancedRemote.mute()
