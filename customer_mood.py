from collections import Counter
import pandas as pd

#strategy: 80% fit, 10% test, 10% validation

#make read of csv
df = pd.read_csv('situacao_do_cliente.csv')
X_df = df[['recencia', 'frequencia', 'semanas_de_inscricao']]
Y_df = df['situacao']

Xdummies_df = pd.get_dummies(X_df).astype(int)
Ydummies_df = Y_df # when has only one column

X = Xdummies_df.values
Y = Ydummies_df.values

fit_percentage = 0.8
test_percentage = 0.1

#tamaho de treino 90% da coluna de comprou
#testes 100 registros = 10%
fit_length = int(fit_percentage * len(Y))
test_length = test_percentage * len(Y)
validation_length = len(Y) - fit_length - test_length

#dados do treino e #demarcation 0 until 799
fit_data = X[:fit_length]
fit_demarcation = Y[:fit_length]

fit_end = fit_length + test_length

#test 800 until 899
test_data = X[int(fit_length):int(fit_end)]
test_demarcation = Y[int(fit_length): int(fit_end)]

#test validation 999 until 999
validation_data = X[int(fit_end):]
validation_demarcation = Y[int(fit_end):]


def fit_and_predict(name, model, fit_data, fit_demarcation, test_data, test_demarcation):
    model.fit(fit_data, fit_demarcation)

    result = model.predict(test_data)
    hits = result == test_demarcation

    total_hits = sum(hits)
    total_elements = len(test_data)

    hits_rate = 100.0 * total_hits / total_elements

    msg = "Algorithm Base hits rate do {0}: {1}".format(name, hits_rate)
    print(msg)
    return hits_rate

def real_test(model, validation_data, validation_demarcation):
    result = model.predict(validation_data)
    hits = result == validation_demarcation

    total_hits = sum(hits)
    total_elements = len(validation_demarcation)

    hits_rate = 100 * total_hits / total_elements
    msg = "Rate of hits between winners two algorithms on real world: {0}".format(hits_rate)
    print(msg)

from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
modelOneVsRest = OneVsRestClassifier(LinearSVC(random_state = 0))
resultOneVsRest = fit_and_predict("OneVsRest", modelOneVsRest, fit_data, fit_demarcation, test_data, test_demarcation)


from sklearn.naive_bayes import MultinomialNB
modelMultinomial = MultinomialNB()
multinomialResult = fit_and_predict("MultinomialNB", modelMultinomial, fit_data, fit_demarcation, test_data, test_demarcation)

from sklearn.ensemble import AdaBoostClassifier
modelAdaboost = AdaBoostClassifier()
adaboostResult = fit_and_predict("AdaBoostClassifier", modelAdaboost, fit_data, fit_demarcation, test_data, test_demarcation)

if multinomialResult > adaboostResult :
    winner = modelMultinomial
else:
    winner = modelMultinomial

real_test(winner, validation_data, validation_demarcation)

#effectiveness test chuta um unico valor
base_hits = max(Counter(validation_demarcation).itervalues())
base_hits_rate = 100.0 * base_hits / len(validation_demarcation)
print('Base hits rate: %f' % base_hits_rate)

total_elements = len(validation_data)
print("Total tests: %d " % total_elements)
