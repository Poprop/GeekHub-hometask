"""Написати функцію <bank> , яка працює за наступною логікою: користувач робить вклад у розмірі <a>
одиниць строком на <years> років під <percents> відсотків (кожен рік сума вкладу збільшується на цей відсоток,
ці гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки). Параметр <percents>
є необов`язковим і має значенняпо замовчуванню <10> (10%). Функція повинна принтануть суму, яка буде на
рахунку, а також її повернути (але округлену до копійок)."""


def bank(amount, years, percents=0.1) -> str:
    result: int = amount
    while years > 0:
        years -= 1
        result += result * (percents / 100)
    return f"You will get {round(result, 2)}"


if __name__ == "__main__":
    try:
        amount: int = int(input("Enter amount of money "))
        years: int = int(input("Enter period of time "))
        percents: int = int(input("Enter percents for deposit "))
        print(bank(amount, years, percents))
    except Exception as e:
        print(f"Ooops smth go wrong in your input :"
              f"{e} \ntry enter valid information next time ")
