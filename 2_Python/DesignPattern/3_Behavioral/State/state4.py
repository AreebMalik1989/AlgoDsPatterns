class State:
    """Base state class"""
    def __init__(self, stations=None, pos=0, name=""):

        if stations is None:
            stations = []

        self._stations = stations
        self._pos = pos
        self._name = name

    def scan(self):

        # Scan the dial to the next station
        self._pos += 1

        # Check for last station
        if self._pos == len(self._stations):
            self._pos = 0
        print(f"Visiting station is {self._stations[self._pos]}  {self._name}")


class AmState(State):

    def __init__(self, radio):
        super().__init__(stations=["1250", "1380", "1510"], pos=0, name="AM")
        self._radio = radio

    def toggle_fm_am(self):
        print("Switching to FM")
        self._radio.state = self._radio.fm_state


class FmState(State):

    def __init__(self, radio):
        super().__init__(stations=["81.3", "89.1", "103.9"], pos=0, name="FM")
        self._radio = radio

    def toggle_fm_am(self):
        print("Switching to AM")
        self._radio.state = self._radio.am_state


class Radio:
    """It has a scan button and FM/AM toggle switch"""
    def __init__(self):
        self._fm_state = FmState(self)
        self._am_state = AmState(self)
        self._state = self._am_state

    @property
    def am_state(self):
        return self._am_state

    @property
    def fm_state(self):
        return self._fm_state

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    # Method to toggle the switch
    def toggle_fm_am(self):
        self._state.toggle_fm_am()

    # Method to scan
    def scan(self):
        self._state.scan()


if __name__ == "__main__":

    radio = Radio()
    actions = [radio.scan] * 3 + [radio.toggle_fm_am] + [radio.scan] * 3
    actions *= 2

    for action in actions:
        action()
