from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression

class Trainer():
    def train(self):
        ohe = OneHotEncoder()
        lr = LinearRegression()
