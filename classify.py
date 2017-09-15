#1 = yes, 0 = not
#fat[{YES}1,0{NO}], short-leg[{YES}1,0{NO}], bark[{YES}1,0{NO}]
pig1 = [1, 1, 0]
pig2 = [1, 1, 0]
pig3 = [1, 1, 0]
dog1 = [1, 1, 1]
dog2 = [0, 1, 1]
dog3 = [0, 1, 1]

data = [pig1, pig2, pig3, dog1, dog2, dog3]

demarcation =  [1, 1, 1, -1, -1, -1]

#based on baresian algorithm,import multinomial algorithm
from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()

#trainee
model.fit(data, demarcation)

#predict
mysterious1 = [1, 1, 1]
mysterious2 = [1, 0, 0]
mysterious3 = [0, 0, 1]

#test
tests = [mysterious1, mysterious2, mysterious3]

#demarcation test expected result [dog, pig, dog]
demarcation_test = [-1, 1, -1]
#pretending
#demarcation_test = [-1, 1, 1]

#result validation
result = model.predict(tests)
print(result)

differences = result - demarcation_test
#difference to show hits
print(differences)

hits = [d for d in differences if d == 0]
total_hits = len(hits)

total_elements = len(tests)

hit_rate = 100.0 * total_hits / total_elements

print(hit_rate)