# Sentiment Analysis Tool - A work of Haris Javed

Find out the sentiment conveyed by your words. Try out the project for yourself: https://bit.ly/3EeLL5i.

## Project Details

### Tech Stack:
Python and various Machine Learning libraries.
<p align="left">
<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a><a href="https://scikit-learn.org/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit_learn" width="40" height="40"/> </a><a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/> </a> <a href="https://numpy.org/" target="_blank" rel="noreferrer"> <img src="https://numpy.org/images/logo.svg" alt="numpy" width="40" height="40"/> </a><a href="https://matplotlib.org/" target="_blank" rel="noreferrer"> <img src="https://matplotlib.org/_static/images/logo_dark.svg" alt="matplotlib" width="40" height="40"/> </a><a href="https://www.nltk.org/" target="_blank" rel="noreferrer"> <img src="https://files.anaconda.com/production/resources/open-source/nltk-logo.svg" alt="nltk" width="40" height="40"/> </a> <a href="https://gradio.app/" target="_blank" rel="noreferrer"> <img src="https://gradio.app/assets/gradio.svg" alt="gradio" width="40" height="40"/> </a></p>

### Installation:

- Make sure you have Python installed and ready to go.
- Clone this repository onto your system.
- Create a new Python environment and install the dependencies in it. This can be done as follows:
  - Open `command prompt` and `cd` to the directory where you have cloned the repo.
  - Run the command `Python -m venv env` to create a new virtual environment named `env`.
  - Activate the enviroment by running the command `env\Scripts\activate.bat`.
  - Install depencies by running the command `pip install -r requirements.txt` .

The above steps will create a python virtual environment and install the required depndencies in it. To go through the noteboook, follow these steps:
- Open `command prompt` and `cd` to the directory where you have cloned the repo.
- Activate the python environment by running the command `env\Scripts\activate.bat`.
- View the notebook by running `jupyter notebook`.

Once your model is created by following the notebook, you may use [`Gradio`](https://gradio.app/) to create a custom GUI like the one created by [me](https://bit.ly/3EeLL5i).

### Description:

The application is intended to bring forth the sentiment carried by the user's words.

The words are preprocessed, fed into a machine learning model which categorizes it into one of three categories: negative, neutral or positive.

The analysis also provides the percentage confidence of the model regarding the classification in each of the three categories. 

The GUI of this project was created using Gradio. The project is hosted in one of the spaces provided by the site Hugging Face🤗.


## Screenshots

The site on visiting: 

![image](https://user-images.githubusercontent.com/72334266/193752283-1922991e-cf1e-4c7e-a8a9-d135f2d515c7.png)

The site in action:

![ezgif-3-7addcae1f8](https://user-images.githubusercontent.com/72334266/193752488-a77a589f-ee20-4c07-8222-560840af0266.gif)


