import sqlite3

db = sqlite3.connect("poprop.db")

c = db.cursor()

#Создание полей БД
# c.execute("""CREATE TABLE articles (
#     title text,
#     full_text text,
#     views integet,
#     avtor text
#  )""")
#Добавление в поля данных (подставление в том же порядке в котором оглашены
#столбцы таблицы
# c.execute('INSERT INTO articles VALUES ("Yandex","VK",10 , "Andrew")')
#виклик всіх елементів таблиці за рахунок *
# c.execute("SELECT * FROM articles")
# x=c.fetchall() # повертає список з кортежами в яких виводяться рядки з елементами
# рядка в таблиці
# print(*[el for el in x],sep="\n")
# #виведення тільки певних полів якщо додадти в список rowid - додатково виводить номер строки
# c.execute("SELECT title , full_text FROM articles")
# print(*[el for el in c.fetchall()])
# c.execute("SELECT rowid, * FROM articles")
# # print(c.fetchmany(1))
# # print(c.fetchone()[0])
# items=c.fetchall()
# for el in items:
#     print(el[1] + "------" + el[4])
# db.commit()
# db.close()
#функціонал WHERE що дозволяє уточнювати пошуковий запит
# = елемент що ми шукаємо   <> всі елементи окрім елементу якого не має бути
# c.execute("SELECT rowid , * FROM articles WHERE title <> 'Yandex'")
# print(c.fetchall())

# #опція ORDER означає порядок вивденення DESC - спадання ,ASC - наростання
# c.execute("SELECT rowid , * FROM articles WHERE rowid < 5  ORDER BY views DESC")
# print(c.fetchall())

# #Видалення всіх елементів з БД
# c.execute("DELETE FROM articles")

# #Видалення певних елементів
# # c.execute('INSERT INTO articles VALUES ("Gorlami ","Italian ",20 , "Andi")')
# c.execute("DELETE from articles WHERE rowid = 2 ")
# c.execute("SELECT * FROM articles")
# print(c.fetchall())
#
# db.commit()
# db.close()
# c.execute('INSERT INTO articles VALUES ("Yandex","VK",10 , "Andrew")')
# c.execute('INSERT INTO articles VALUES ("Gorlami ","Italian ",20 , "Andi")')
# c.execute("UPDATE articles SET avtor = 'Admin' WHERE title ='Yandex' ")
c.execute("SELECT rowid , * FROM articles")
# print(c.fetchall())
print(c.fetchone()[2])
db.commit()
db.close()