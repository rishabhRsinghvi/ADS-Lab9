Capp. route(" / predict" , methods = ['GET', 'POST']
            
def predict():
    if request "GET":
        return render_template("predict.html")

df = pd.read_csv('spam.csv', encoding = 'latin-1')
df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis = 1, inplace = True)
df['label'] = df['type'].map({"ham": 0, spam :1})
X = df['text']
y = df['label']


from sktearn.feature-extraction.text import CountVectorizer
from sklearn. model_selection import GridSearchCV

cv = CountVectorizer()
X = cv.fit_transform(X)

from sklearn. model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.2, random_state = 42
)

from naive_bayes import MultinomialNB

clf = multinomialNB(alpha = 0.1, force_alpha = True)

clf.fit(X_train, y_train)
ctf.test(X_test, y_test)

message = request.form['message']
data = [message]
vect = cv.transforn(data). toarray()
my_prediction = ctf. predict(vect)
return render_template('predict.html', prediction = my_prediction)