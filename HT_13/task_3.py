"""Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів."""


class ClassWithCounter:
    counter = 0

    def __init__(self):
        ClassWithCounter.counter += 1

    @classmethod
    def get_class_instance_count(cls):
        return ClassWithCounter.counter


if __name__ == "__main__":
    clone1 = ClassWithCounter()
    print(ClassWithCounter.get_class_instance_count())
    clone2 = ClassWithCounter()
    clone3 = ClassWithCounter()
    clone4 = ClassWithCounter()
    print(ClassWithCounter.get_class_instance_count())
