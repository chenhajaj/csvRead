import csv


def median(mylist):
    sorts = sorted(mylist)
    length = len(sorts)
    if not length % 2:
        return ((sorts[length / 2]) + sorts[length / 2 - 1]) / 2.0
    return sorts[length / 2]

with open('iceff_1801_2-4_1484770496253.csv', 'rb') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar='|')
    skip = 0
    small = []
    big = []
    num = 2
    for row in data:
        if skip == 0:
            skip = 1
        else:
            if int(row[3]) == int(0):
                small = filter(None, small)
                big = filter(None, big)
                print(num, median(small), median(big))
                break
            elif int(row[7]) == num:
                small.append(row[23])   # Small centers
                big.append(row[24])     # Big centers
            else:
                small = filter(None, small)
                big = filter(None, big)
                print(num, median(small), median(big))
                small = []
                big = []
                num += 1
