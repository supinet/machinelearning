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

def searches_load():
    X = [];
    Y = [];

    file = open('busca.csv', 'rb')
    reader = csv.reader(file)
    reader.next()

    for home,busca,logado,comprou in reader:
        data = [int(home), busca, int(logado)]
        X.append(data)
        Y.append(int(comprou))

    return X,Y