from classes.class_1 import *
from classes.class_2 import *
from classes.class_3 import *
"""
Задание_1 
Выведите список всех магазинов, у которых название начинается с буквы «А», и список книг в них.
"""
"""
Задание_2
Вывод списка магазинов с максимальной численностью страниц в книгах которые присутствуют в данных магазинах
"""
"""
Задание_3
Вывод всех связных магазинов и книг в них отсортированный по магазинам а так же по колличеству книг в каждом магазине
"""
books = [
    Book(1,"Книга_1",2500,1),
Book(2,"А_Книга_2",250,2),
Book(3,"Б_Книга_3",50,3),
Book(4,"Л_Книга_4",10,4),
Book(5,"и_Книга_5",150,3),
Book(6,"х_Книга_6",200,4),
Book(7,"Книга_7",350,2),
Book(8,"Книга_8",455,1),
Book(9,"Книга_9",55,4),
Book(10,"Книга_10",123,1),
Book(11,"Книга_11",226,2),
Book(12,"Книга_12",104,3)
]
shops = [
Book_shop(1,"A это магазин_1"),
Book_shop(2,"Магазин_2"),
Book_shop(3,"Супер магазин агазин_3"),
Book_shop(4,"Дупер пупер магазин_4")

]

Shops_and_books = [
book_and_shop(1,2),
book_and_shop(1,3),
book_and_shop(1,5),
book_and_shop(2,2),
book_and_shop(2,3),
book_and_shop(2,1),
book_and_shop(3,1),
book_and_shop(3,2),
book_and_shop(3,6),
book_and_shop(3,3),
book_and_shop(4,1),
book_and_shop(4,2),
book_and_shop(4,4),
book_and_shop(4,3)
]

"""
Вывод из книжных магазинов книги с наибольшим колличеством страниц
"""
def main():
    one_to_many = [
        (b.name_book,b.lists,bs.name)
        for bs in shops
        for b in books
        if bs.id_shop == b.num_shop
    ]
    man_to_many=[
        (b.name_book,b.lists,bs.name)
        for bs in shops
        for b in books
        for rl in Shops_and_books
        if bs.id_shop == rl.num_shop_ID and b.book_id == rl.book_id_Sh_
    ]

    print("Задание_1")
    for i in range(len(one_to_many)):
        if((one_to_many[i][2])[0] == 'A'):
            print(one_to_many[i])
    print("Задание_2")
    a = True
    ans_2 = []
    while(a):
        tmp_name = one_to_many[0][2]
        tmp_max = 0
        tmp_i = 0
        tmp_max_money = 0
        id_start = 0
        id_stop = 0
        for i in range(len(one_to_many)):
            if (one_to_many[i][2] == tmp_name and one_to_many[i][1] > tmp_max_money):
                    tmp_max_money = one_to_many[i][1]
                    tmp_i = i
        for i in range(len(one_to_many)):
            if(one_to_many[i][2] == tmp_name):
                id_stop = i

        ans_2.append(one_to_many[tmp_i])

        del one_to_many[id_start:id_stop+1]
        if(len(one_to_many) == 0):
            a = False
    for i in range(len(ans_2)):
        print(ans_2[i])

    print("Задание_3")
    a = True
    ans_3 = []

    while(a):
        tmp_name = man_to_many[0][2]
        id_start = 0
        id_stop = 0
        for i in range(len(man_to_many)-1):
            if(man_to_many[i][2] == man_to_many[i+1][2]):
                if(man_to_many[i][1] > man_to_many[i+1][1]):
                    tmp = man_to_many[i]
                    man_to_many[i] = man_to_many[i+1]
                    man_to_many[i+1] = tmp
        for i in range(len(man_to_many)):
            if(man_to_many[i][2] == tmp_name):
                id_stop = i
                ans_3.append(man_to_many[i])
        del man_to_many[id_start:id_stop + 1]
        if(len(man_to_many) == 0):
            a = False

    for i in range(len(ans_3)-1):
        print(ans_3[i], end= ' ')
        if(ans_3[i][2] != ans_3[i+1][2]):
            print(' ')
    print(ans_3[len(ans_3)-1],end=' ')

try:
    main()
except:
    print("Ошибка")
