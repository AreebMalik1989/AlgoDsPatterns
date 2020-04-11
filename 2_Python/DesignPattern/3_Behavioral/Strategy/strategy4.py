class StrategyExample:

    def __init__(self, func=None):
        if func:
            self.execute = func

    def execute(self):
        print("Original execution")


def execute_replacement1():
    print("Strategy1")


def execute_replacement2():
    print("Strategy2")


if __name__ == "__main__":

    strat0 = StrategyExample()
    strat1 = StrategyExample(execute_replacement1)
    strat2 = StrategyExample(execute_replacement2)

    strat0.execute()
    strat1.execute()
    strat2.execute()
