#!/usr/bin/python
import copy


class Originator(object):

    def __init__(self, state=None):
        self._state = state

    class Memento(object):
        def __init__(self, state):
            self._state = state

        def rollback_state(self):
            return self._state

    def set_state(self, state):
        print('Originator: setup state to: {0}'.format(state))
        self._state = state

    def get_state(self):
        print('Originator: reading state to: {0}'.format(self._state))

    def save_state(self):
        print('Originator: saving state')
        return self.Memento(copy.deepcopy(self))

    def rollback_state(self, memento):
        self = memento.rollback_state()
        print('Originator: rollback to state: {0}'.format(self._state))


if __name__ == '__main__':
    orig = Originator()
    orig.set_state('State 1')
    orig.get_state()
    orig.set_state('State 2')
    orig.get_state()
    saved_state = orig.save_state()
    orig.set_state('State 3')
    orig.get_state()
    orig.rollback_state(saved_state)
