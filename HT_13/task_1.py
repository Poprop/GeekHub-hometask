"""Напишіть програму, де клас «геометричні фігури» (Figure) містить властивість color з
початковим значенням white і метод для зміни кольору фігури, а його підкласи «овал»
(Oval) і «квадрат» (Square) містять методи __init__ для
завдання початкових розмірів об'єктів при їх створенні."""


class Figure:
    def __init__(self, color="white"):
        self.color = color

    def change_color(self, new_color):
        self.color = new_color


class Oval(Figure):
    def __init__(self, width, height, color="white"):
        super().__init__(color)
        self.width = width
        self.height = height


class Square(Figure):
    def __init__(self, side, color="white"):
        super().__init__(color)
        self.side = side


if __name__ == "__main__":
    oval = Oval(width=5, height=10, color="red")
    print(oval.__dict__)
    oval.change_color(new_color="blue")
    print(oval.__dict__)
