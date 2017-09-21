import pandas as pd

df = pd.read_csv('busca.csv')

#df = dataFrame
X_df = df[['home', 'busca', 'logado']]
Y_df = df['comprou']

Xdummies_df = pd.get_dummies(X_df).astype(int)
Ydummies_df = Y_df # quando tem somente uma coluna

X = Xdummies_df.values
Y = Ydummies_df.values

#effectiveness test chuta tudo 0 ou 1
hits_of_one = sum(Y)
hits_of_zero = len(Y) - hits_of_one
base_hits_rate = 100.0 * max(hits_of_one, hits_of_zero) / len(Y)
print('Base hits rate: %f' % base_hits_rate)


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


from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model.fit(fit_data, fit_demarcation)

result = model.predict(test_data)
differences = result - test_demarcation

hits = [d for d in differences if d == 0]
total_hits = len(hits)
total_elements = len(test_data)

hits_rate = 100.0 * total_hits / total_elements

print('Algorithm Base hits rate: %f' % hits_rate)
print(total_elements)

