# Вам дан тензор с суммами на счетах, где account[i][j] — это сумма денег, которую имеет i клиент в j-м банке.
#
# accounts = [[1,2,5],[3,6,1]]
# У 1-го клиента два счета на сумму 4 (1 + 3)
# У 2-го — 8 (2 + 6)
# У 3-го — 6 (5 + 1)
#
# Напишите функцию find_richest(), которая найдет Рокфеллера — самого богатого клиента.


def find_richest(accounts):
    summ = list(i*0 for i in range(0,len(accounts[0])))
    print(summ)
    for bank in accounts:
        i = 0
        for vklad in bank:
            summ[i] = summ[i] + bank[i]
            i+=1
    print(summ)
    maximum = max(summ)
    print(maximum)
    rokfeler = summ.index(maximum)
    return rokfeler


accounts = [[1, 2, 5], [3, 6, 1]]
print('rokfeler is', find_richest(accounts))
