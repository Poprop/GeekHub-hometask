"""Написати функцію <bank> , яка працює за наступною логікою: користувач робить вклад у розмірі <a>
одиниць строком на <years> років під <percents> відсотків (кожен рік сума вкладу збільшується на цей відсоток,
ці гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки). Параметр <percents>
є необов`язковим і має значенняпо замовчуванню <10> (10%). Функція повинна принтануть суму, яка буде на
рахунку, а також її повернути (але округлену до копійок)."""


def bank(amount, years, percents=0.1) -> int:
    result: int = amount
    while years > 0:
        years -= 1
        result += result * (percents / 100)
    return round(result, 2)


if __name__ == "__main__":
    print(
        bank(int(input("Enter start capital: ")), int(input("Enter period: ")), int(input("Enter custom percents: "))))
