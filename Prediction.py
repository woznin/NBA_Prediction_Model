import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


def wl_prediction(datax, datay, next_match_pred_data, visualize_cm=False):
    # set visualize_cm to check how accurate the classification is for past matches
    model = LogisticRegression(max_iter=250000)
    if visualize_cm:
        model2 = LogisticRegression(max_iter=250000)
        X_train, X_test, y_train, y_test = train_test_split(datax, datay, test_size=50)
        model2.fit(X_train, y_train)
        y_pred = model2.predict(X_test)
        cm = confusion_matrix(y_test, y_pred)
        sns.heatmap(cm, annot=True, fmt="d")
        plt.xlabel('Predicted labels')
        plt.ylabel('True labels')
        plt.title('Confusion Matrix')
        plt.show()
    model.fit(datax, datay)
    next_match_prediction = model.predict(next_match_pred_data)
    return next_match_prediction


def performance_prediction(datax, datay, matchup):
    X = pd.get_dummies(datax)
    model = LinearRegression()
    model.fit(X, datay)
    next_match = pd.get_dummies([matchup], columns=X.columns).reindex(columns=X.columns, fill_value=0)
    stats_prediction = model.predict(next_match)
    stats_prediction = stats_prediction.astype(int)
    return stats_prediction
