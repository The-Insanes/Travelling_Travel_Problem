class Item():
    def __init__(self, weight: int, profit: int) -> None:
        self.__weight = int(weight)
        self.__profit = int(profit)

    def get_weight(self) -> int:
        return self.__weight
    
    def get_profit(self) -> int:
        return self.__profit