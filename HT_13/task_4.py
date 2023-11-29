"""Create 'list'-like object, but index starts from 1 and index of 0 raises error.
Тобто це повинен бути клас, який буде поводити себе так, як list (маючи основні методи),
але індексація повинна починатись із 1"""


class CustomList:
    def __init__(self, *args):
        self._data = list(args)

    def __getitem__(self, index):
        if index < 1:
            raise IndexError("Index must be greater than or equal to 1")
        return self._data[index - 1]

    def __setitem__(self, index, value):
        if index < 1:
            raise IndexError("Index must be greater than or equal to 1")
        while len(self._data) < index:
            self._data.append(None)
        self._data[index - 1] = value

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return repr(self._data)


if __name__ == "__main__":
    list_1 = CustomList(10, 15, 20, 12, 15)
    print(f"Original list {list_1}")
    print(f"{list_1[1]}")
    try:
        list_1[0] = 1
    except IndexError as _:
        print("In custom list doesnt exist 0 index")
