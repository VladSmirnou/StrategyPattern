from abc import ABC, abstractmethod
from typing import Union


class LoanCalculator:

    __loan_calculator: Union['CalculatorAlgorithm', None] = None

    def calculate(self) -> None:
        # Actually it is pretty strange that this pattern doesn't
        # say anything about the default algorithm, so that invoking
        # this attribute while it is not set will raise an exception
        # at runtime. I guess it is on me to choose if I want to 
        # check for 'None' or introduce a dependency on that default
        # algorithm.
        self.__loan_calculator.calculate_loan()

    def set_loan_calculator(self, calculator: 'CalculatorAlgorithm') -> None:
        self.__loan_calculator = calculator

    loan_calculator: property = property(fset=set_loan_calculator)


class CalculatorAlgorithm(ABC):
    @abstractmethod
    def calculate_loan(self) -> None: ...


class CalculatorAlgorithmOne(CalculatorAlgorithm):
    def calculate_loan(self) -> None:
        print('Calculating loan using algorithm one')


class CalculatorAlgorithmTwo(CalculatorAlgorithm):
    def calculate_loan(self) -> None:
        print('Calculating loan using algorithm two')
    

def main() -> None:
    obj: LoanCalculator = LoanCalculator()

    obj.loan_calculator = CalculatorAlgorithmOne()
    obj.calculate()

    obj.loan_calculator = CalculatorAlgorithmTwo()
    obj.calculate()


main()
