"""Create 'list'-like object, but index starts from 1 and index of 0 raises error.
Тобто це повинен бути клас, який буде поводити себе так, як list (маючи основні методи),
але індексація повинна починатись із 1"""


class CustomList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(args, **kwargs)

    def __getitem__(self, index):
        if index < 1:
            raise IndexError("Index must be greater than or equal to 1")
        return super().__getitem__(index - 1)

    def __setitem__(self, index, value):
        if index < 1:
            raise IndexError("Index must be greater than or equal to 1")
        while len(self) < index:
            self.append(None)
        super().__setitem__(index - 1, value)


if __name__ == "__main__":
    list_1 = CustomList(10, 15, 20, 12, 15)
    list_1[0] = 5
    print(list_1)
