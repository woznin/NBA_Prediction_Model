import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LinearRegression
import seaborn as sns


def wl_model_process(datax, datay, next_match_pred_data):
    # X_train, X_test, y_train, y_test = train_test_split(datax, datay, test_size=0.2)
    model = LogisticRegression()
    model.fit(datax, datay)
    # model.fit(X_train, y_train)
    # y_pred = model.predict(X_test)
    # cm = confusion_matrix(y_test, y_pred)
    # sns.heatmap(cm, annot=True, fmt="d")
    # plt.xlabel('Predicted labels')
    # plt.ylabel('True labels')
    # plt.title('Confusion Matrix')
    # plt.show()
    next_match_prediction = model.predict(next_match_pred_data)
    print(f'Predicted outcome: {next_match_prediction}')


def stats_model_process(datax, datay, matchup):
    X = pd.get_dummies(datax)
    model = LinearRegression()
    model.fit(X, datay)
    next_match = pd.get_dummies([matchup], columns=X.columns).reindex(columns=X.columns, fill_value=0)
    stats_prediction = model.predict(next_match)
    stats_prediction = stats_prediction.astype(int)
    return stats_prediction
