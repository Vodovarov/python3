"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
 (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_occupation(self):
        return self.position

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('wage') // self._income.get('bonus')

'''Bonus - must be set up just in percent!'''
if __name__ == '__main__':
    try:
        ''' "bonus" - must be set up in percent! '''
        posit = Position('Robert', 'Smith', 'carpenter', 38400, 10)
        print(posit.get_total_income())
        print(posit.get_full_name())
        print(f'Employee\'s occupation is {posit.get_occupation()}.')
    except TypeError:
        print('Данные введены неверно')
