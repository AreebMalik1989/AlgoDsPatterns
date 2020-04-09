"""
Interpreter design pattern implemenation

Intent:

    Interpreter design pattern is used to define a problem in simple language and resolving it through interpreting its
    simple sentences.

Structure:

1.  AbstractExpression class: Provides interface Interpret().

2.  TerminalExpression class: Represents the terminal symbol in grammar and implements method Interpret().

3.  NonTerminalExpression class: Represents rule in the grammar and will be there for every rule. This implements
    Interpret() method and interprets every rule considering other rules.

4.  Context class: Has the context information and will be used while interpretation of Terminal and Non Terminal
    expressions.

5.  Client: Has the representation of simple sentences of language with defined grammar. This is in form of terminal and
    Non terminal expressions.
"""


from abc import ABC, abstractmethod


class AbstractExpression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass


class TerminalExpression(AbstractExpression):

    def __init__(self, data):
        self._data = data

    def interpret(self, context):
        if context.contains(self._data):
            return True
        return False


class OrExpression(AbstractExpression):

    def __init__(self, expression1: AbstractExpression, expression2: AbstractExpression):
        self._expression1 = expression1
        self._expression2 = expression2

    def interpret(self, context):
        return self._expression1.interpret(context) or self._expression2.interpret(context)


class AndExpression(AbstractExpression):

    def __init__(self, expression1: AbstractExpression, expression2: AbstractExpression):
        self._expression1 = expression1
        self._expression2 = expression2

    def interpret(self, context):
        return self._expression1.interpret(context) and self._expression2.interpret(context)


class Context:

    def __init__(self, data: str):
        self._data: str = data

    def contains(self, sub_data):
        return self._data.find(sub_data) != -1


def get_male_expression():
    robert = TerminalExpression("Robert")
    john = TerminalExpression("John")
    return OrExpression(robert, john)


def get_married_women_expression():
    julie = TerminalExpression("Julie")
    married = TerminalExpression("Married")
    return AndExpression(julie, married)


if __name__ == "__main__":

    is_male = get_male_expression()
    is_married_women = get_married_women_expression()

    john = Context("John")
    married_julie = Context("Married Julie")

    print(f"Is John male? {is_male.interpret(john)}")
    print(f"Is Julie a married woman? {is_married_women.interpret(married_julie)}")
