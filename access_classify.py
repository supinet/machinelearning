from dados import access_load

X,Y = access_load()

data_fit = X[:90]
demarcation_fit = Y[:90]

test_fit = X[-9:]
test_demarcation = Y[-9:]

from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()
model.fit(data_fit, demarcation_fit)

result = model.predict(test_fit)

differences = result - test_demarcation

hits = [d for d in differences if d == 0]

total_hits = len(hits)

total_elements = len(test_fit)

hit_rate = 100.0 * total_hits / total_elements

print(hit_rate)