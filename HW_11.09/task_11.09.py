class Dog:
    def __init__(self, name, master, age: int):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print(f'{self.name}, Run!')

    def jump(self):
        print(f'{self.name}, Jump!')

    def birthday(self):
        self.age += 1
        return self.age

    def sleep(self):
        print(f'{self.name} is sleeping')

    def bark(self):
        print('Woof!')


class Cat:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print(f'{self.name}, Run!')

    def jump(self):
        print(f'{self.name}, Jump!')

    def birthday(self):
        self.age += 1
        return self.age

    def sleep(self):
        print(f'{self.name} is sleeping')

    def meow(self):
        print('Meow')


class Parrot:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print(f'{self.name}, Run!')

    def jump(self):
        print(f'{self.name}, Jump!')

    def birthday(self):
        self.age += 1
        return self.age

    def sleep(self):
        print(f'{self.name} is sleeping')

    def fly(self):
        print(f'{self.name} is flying')


dog = Dog(name='Barny', age=1, master='Ilya')
cat = Cat(name='Tima', age=3, master='Mom')
parrot = Parrot(name='Kesha', age=2, master='Alina')

dog.run()
dog.sleep()
dog.bark()

cat.meow()
print(cat.birthday())
print(cat.birthday())

parrot.birthday()
parrot.fly()