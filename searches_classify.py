from collections import Counter
import pandas as pd

#df = pd.read_csv('busca.csv')
df = pd.read_csv('busca2.csv')

#df = dataFrame
X_df = df[['home', 'busca', 'logado']]
Y_df = df['comprou']

Xdummies_df = pd.get_dummies(X_df).astype(int)
Ydummies_df = Y_df # quando tem somente uma coluna

X = Xdummies_df.values
Y = Ydummies_df.values

fit_percentage = 0.9

#tamaho de treino 90% da coluna de comprou
#testes 100 registros = 10%
fit_length = fit_percentage * len(Y)
test_length = len(Y) - fit_length

#dados do treino e #demarcation
fit_data = X[:int(fit_length)]
fit_demarcation = Y[:int(fit_length)]

#test
test_data = X[-int(test_length):]
test_demarcation = Y[-int(test_length):]

def fit_and_predict(model, fit_data, fit_demarcation, test_data, test_demarcation):
    model.fit(fit_data, fit_demarcation)

    result = model.predict(test_data)
    hits = (result == test_demarcation)

    # isn't necessary anymore
    #hits = [d for d in differences if d == 0]
    total_hits = sum(hits)
    total_elements = len(test_data)

    hits_rate = 100.0 * total_hits / total_elements

    print('Algorithm Base hits rate: %f' % hits_rate)

from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
fit_and_predict(model, fit_data, fit_demarcation, test_data, test_demarcation)

from sklearn.ensemble import AdaBoostClassifier
model = AdaBoostClassifier()
fit_and_predict(model, fit_data, fit_demarcation, test_data, test_demarcation)

#effectiveness test chuta um unico valor
base_hits = max(Counter(test_demarcation).itervalues())

base_hits_rate = 100.0 * base_hits / len(test_demarcation)
print('Base hits rate: %f' % base_hits_rate)
print("Total tests: %f " % len(test_data))
