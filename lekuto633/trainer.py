from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder, StandardScaler

class Trainer():
    def train(self):
        ohe = OneHotEncoder()
        std_scaler = StandardScaler()
        lr = LinearRegression()
