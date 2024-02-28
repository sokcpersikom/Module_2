if __name__ == "__main__":
    # Write your solution here
    pass
# Базовый класс: "Фрукт"

class Fruit:
    """
    Базовый класс, представляющий фрукт.

    Атрибуты:
    - name (str): название фрукта
    - color (str): цвет фрукта
    """

    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color

    def __str__(self) -> str:
        return f'{self.name}'

    def __repr__(self) -> str:
        return f"Fruit(name='{self.name}', color='{self.color}')"

# Дочерний класс: "Яблоко"

class Apple(Fruit):
    """
    Дочерний класс, представляющий яблоко.

    Дополнительные атрибуты:
    - variety (str): сорт яблока
    - taste (str): вкус яблока
    """

    def __init__(self, name: str, color: str, variety: str, taste: str):
        super().__init__(name, color)
        self.variety = variety
        self.taste = taste

    def __str__(self) -> str:
        return f'{self.variety}'

    def __repr__(self) -> str:
        return f"Apple(name='{self.name}', color='{self.color}', variety='{self.variety}', taste='{self.taste}')"

    def is_delicious(self) -> bool:
        """
        Метод для проверки вкусности яблока.

        Возвращает True, если вкус яблока считается вкусным, и False в противном случае.
        """
        if self.taste == 'сладкий' or self.taste == 'кислый':
            return True
        else:
            return False

    def ripen(self, days: int) -> str:
        """
        Метод для симуляции процесса созревания яблока.

        Аргументы:
        - days (int): количество дней для созревания

        Возвращает строку о том, что яблоко созрело через указанное количество дней.
        """
        return f'{self.variety} стало спелым через {days} дней'
