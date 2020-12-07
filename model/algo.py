import pandas as pd
import re
import joblib
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multiclass import OneVsRestClassifier
from stop_words import get_stop_words
from sklearn.svm import SVC

# import & clean 
df = pd.read_csv("./data/articles_data.csv", usecols=['title', 'source_name'])
df = df.dropna()
df['title'] = df['title'].apply(lambda text: re.sub('[^A-Za-z]+', ' ', text.lower()))
print(df.head())

# algo
clf = make_pipeline(
    TfidfVectorizer(stop_words=get_stop_words('en')),
    OneVsRestClassifier(SVC(kernel='linear', probability=True))
)

clf = clf.fit(X=df['title'], y=df['source_name'])

# predict
text = "Louise Kennedy AW2019: Long coats, sparkling tweed dresses and emerald knits"
print(clf.predict_proba([text])[0])
print(clf.predict([text]))

# save
model_filename = "news_title.joblib"
joblib.dump((clf), model_filename)