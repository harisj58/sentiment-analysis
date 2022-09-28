import gradio as gr
import joblib as jb
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
import nltk
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

cv = jb.load('.//models//transformer_v1.pkl')
model = jb.load('.//models//model_v1.pkl')


def preprocess_text(text):
    """
    Runs a set of transformational steps to
    preprocess the text of the tweet.
    """
    # convert all text to lower case
    text = text.lower()

    # remove any urls
    text = re.sub(r'http\S+|www\S+|https\S+', "", text, flags=re.MULTILINE)

    # replace '****' with 'curse'
    text = re.sub(r'\*\*\*\*', "gaali", text)

    # remove punctuations
    text = text.translate(str.maketrans("", "", string.punctuation))

    # remove user @ references and hashtags
    text = re.sub(r'\@\w+|\#', "", text)

    # remove useless characters
    text = re.sub(r'[^ -~]', '', text)

    # remove stopwords
    tweet_tokens = word_tokenize(text)
    filtered_words = [word for word in tweet_tokens if word not in stop_words]

    # stemming
    ps = PorterStemmer()
    stemmed_words = [ps.stem(w) for w in filtered_words]

    # lemmatizing
    lemmatizer = WordNetLemmatizer()
    lemma_words = [lemmatizer.lemmatize(w, pos='a') for w in stemmed_words]

    return ' '.join(lemma_words)


def sentiment_analysis(text):
    print(text)
    text = cv.transform([preprocess_text(text)])
    pred_prob = model.predict_proba(text)[0]
    output = {"Negative": float(pred_prob[0]), "Neutral": float(pred_prob[1]), "Positive": float(pred_prob[2])}
    print(output)
    return output


demo = gr.Interface(
    fn=sentiment_analysis,
    inputs=gr.Textbox(label="Input here", lines=2, placeholder="Input your text"),
    outputs=gr.Label(label="Sentiment Analysis"),
)
demo.launch()
