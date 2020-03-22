"""
MVC design pattern implementation

Some points to mention...

The model knows nothing about the view or the controller.
The view knows nothing about the model or the controller.
The controller understands both the model and the view.

The model uses observables, essentially when important data is changed,
any interested listener get notified through a callback mechanism.

The following opens up two windows, one that reports how much money you have,
and one that has two buttons, one to add money and one to remove money.

The important this is that the controller is set up to monitor changes in the
model. In this case the controller notices that you clicked a button and
modifies the money in the model which then sends out a message that it has
changed. The controller notices this and updates the widgets.

The cool thin is anything modifying the model will notify the controller. In
this case it is controller modifying the model, but it could be anything else,
even another controller off in the distance looking at something else.

The main idea is that you give a controller the model and view that it needs,
but model's can be shared between controllers so that when model is updated,
all associated views are updated. -Brian Kelley

Following is Tkinter approximation of the original example.

python --version
Python 2.7.16
"""


import tkinter as tk
from typing import Any


class Observable:
    
    def __init__(self, initial_value=None) -> None:
        self.data = initial_value
        self.callbacks = {}

    def add_callback(self, func) -> None:
        self.callbacks[func] = 1

    def del_callback(self, func) -> None:
        del self.callbacks[func]

    def _do_callbacks(self) -> None:
        for func in self.callbacks:
            func(self.data)

    def set(self, data) -> None:
        self.data = data
        self._do_callbacks()

    def get(self) -> Any:
        return self.data

    def unset(self) -> None:
        self.data = None


class Model:

    def __init__(self) -> None:
        self.money: Observable = Observable(0)

    def add_money(self, value) -> None:
        self.money.set(self.money.get() + value)

    def remove_money(self, value) -> None:
        self.money.set(self.money.get() - value)


class View(tk.Toplevel):

    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)
        tk.Label(self, text='My money').pack(side='left')
        self.moneyCtrl = tk.Entry(self, width=8)
        self.moneyCtrl.pack(side='left')

    def set_money(self, money):
        self.moneyCtrl.delete(0, 'end')
        self.moneyCtrl.insert('end', str(money))


class ChangerWidget(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.add_button = tk.Button(self, text='Add', width=8)
        self.add_button.pack(side='left')
        self.remove_button = tk.Button(self, text='Remove', width=8)
        self.remove_button.pack(side='left')


class Controller:
    
    def __init__(self, model: Model, view1: View, view2: ChangerWidget) -> None:
        self.model = model
        self.view1 = view1
        self.view2 = view2

        # Add callback in model
        self.model.money.add_callback(self.money_changed)

        self.view2.add_button.config(command=self.add_money)
        self.view2.remove_button.config(command=self.remove_money)

        self.money_changed(self.model.money.get())

    def add_money(self) -> None:
        self.model.add_money(10)

    def remove_money(self) -> None:
        self.model.remove_money(10)

    def money_changed(self, money) -> None:
        self.view1.set_money(money)


if __name__ == '__main__':

    model = Model()

    root = tk.Tk()
    root.withdraw()
    view1 = View(root)
    view2 = ChangerWidget(view1)

    app = Controller(model, view1, view2)
    root.mainloop()
