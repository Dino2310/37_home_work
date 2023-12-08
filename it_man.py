
class it_men:
    def __init__(self, count_lang) -> None:
        self.count_lang = count_lang
        self.lang = set()

    def input_lang(self):
        """Добавляет уникальные для пользователя языки программирования"""
        while (n:=input("Введите языки программирования через пробел (для выхода нажмите 'q'): "))!='q':
            self.lang.update(n.split())

    def __add__(self, other):
        """Оператор сложения возвращает булево значение является ли первое слагаемое больше второго"""
        if not isinstance(other, it_men):
            raise "Error type"
        return len(self.lang)>len(other.lang)
    
    def __len__(self):
        """Проверяет, соотвесвует ли колличесвто введённых языков счётчику введённому изначально"""
        return len(self.lang)>=self.count_lang