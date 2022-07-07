import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split

import dataset_creator_v3
from model_utils import save_model, get_model, prepare_columns
from validation import validate

path_dataset = 'penguins_v3.csv'
model_name = 'saved_model_gradient.pkl'


def __fit_model():
    penguins_X, penguins_y = prepare_columns(penguins)
    x_penguin_train, x_penguin_test, y_penguin_train, y_penguin_test = train_test_split(penguins_X, penguins_y,
                                                                                        test_size=0.30, random_state=2,
                                                                                        stratify=penguins_y)
    # train a model on the training set
    multi_model = GradientBoostingClassifier(n_estimators=1000)

    multi_model.fit(x_penguin_train, y_penguin_train)

    save_model(multi_model, model_name)
    return multi_model


def get_result_for_gradient(args):
    model = get_model(model_name, __fit_model)
    return validate(model, args)


try:
    penguins = pd.read_csv(path_dataset, encoding='unicode_escape')
except FileNotFoundError:
    dataset_creator_v3.main()
    penguins = pd.read_csv(path_dataset, encoding='unicode_escape')
    __fit_model()
