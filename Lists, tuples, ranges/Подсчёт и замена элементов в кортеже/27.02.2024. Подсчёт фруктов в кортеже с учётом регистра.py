# Çàäà÷à: ïîñ÷èòàòü êîëè÷åñòâî ôðóêòîâ â êîðòåæå.

while(True):
    try:

        tuple = (('Apple', 'Apple', 'Strawberry', 'Banana', 'banana', 'banana', 'mango'))
        print(tuple)
        value1 = input('Ââåäèòå íàçâàíèå ôðóêòà (ñ ó÷¸òîì ðåãèñòðà):~$ ')
        print('\nÊîëè÷åñòâî ñëîâ â êîðòåæå:',tuple.count(value1),'\n')

    except: continue
