def f1(lista):
    for y in lista:
        if not isinstance(y, str):
            return "error"
        if len(y) > 4:
            return [y]


print(f1(['Pas', 'Macka', 'Stol']))


def f2(lista, dictionary):
    if isinstance(lista, list) and isinstance(dictionary, dict) == False:
        return "error"

    if len(lista) != len(dictionary):
        return "nemaju isti broj elemenata"

    for y in lista:
        for x in dictionary:
            if not isinstance(y, int) and not isinstance(x, int):
                return "nisu svi tipa int"

    return {x: y if 5 < y < 10 else y == -1 for y, x in zip(lista, dictionary)}


print(f2([8, 7, 1], {1: 2, 2: 1, 3: 2}))


def f3(list1):
    if not isinstance(list1, list):
        return "error"
    for x in list1:
        if not isinstance(x, dict):
            return "nisu svi dictionary"
        if len(x) < 3:
            return "nemaju svi 3 ključa"


print(f3([{"cijena": 8, "naziv": "Kruh", "kolicina": 1}, {"cijena": 13, "naziv": "Sok", "kolicina": 2},
          {"cijena": 7, "naziv": "Upaljac", "kolicina": 1}]))
