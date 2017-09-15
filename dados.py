import csv

def access_load():

    X = []
    Y = []

    file = open('acesso.csv', 'rb')
    reader = csv.reader(file)

    reader.next()

    for home,como_funciona,contato,comprou in reader:
        data = [int(home),int(como_funciona),int(contato)]
        X.append(data)
        Y.append(int(comprou))
    return X, Y