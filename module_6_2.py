from colorama import init, Fore


init(autoreset=True)


class Vehicle:
    __COLOR_VARIANTS = ['white', 'blue', 'red', 'black']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        if __color in Vehicle.__COLOR_VARIANTS:
            self.__color = __color

    def get_model(self):
        return Fore.BLUE + f'Модель: {self.__model}'

    def get_horsepower(self):
        return Fore.BLUE + f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return Fore.BLUE + f'Цвет: {self.__color}'

    def print_info(self):
        print(f'{self.get_model()}')
        print(f'{self.get_horsepower()}')
        print(f'{self.get_color()}')
        print(Fore.BLUE + f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color in Vehicle.__COLOR_VARIANTS:
            self.__color = Fore.GREEN + new_color.upper()
        else:
            print(Fore.RED + f'Невозможно покрасить в {new_color}')


class Sedan(Vehicle):

    def __init__(self, owner, __model, __engine_power, __color):
        super().__init__(owner, __model, __engine_power, __color)
        self.__PASSENGERS_LIMIT = 5


v1 = Sedan('Дмитрий', 'Geely Tugella', 211, 'black')

v1.print_info()

v1.set_color(Fore.RED + 'green')
v1.set_color('white')
v1.owner = (Fore.GREEN + 'Лиана')

v1.print_info()
