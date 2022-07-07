def save_model(multi_model, model_name):
    import pickle
    with open(model_name, "wb") as file:
        pickle.dump(multi_model, file)
    print("model wrote")


def load_model(model_name):
    import pickle

    return pickle.load(model_name)


def get_model(model_name, function_callback):
    try:
        with open(model_name, mode="rb") as file:
            if file:
                return load_model(file)
            else:
                function_callback()
    except IOError:
        return function_callback()


def prepare_columns(penguins):
    penguins.dropna(inplace=True)
    penguins.reset_index()
    penguin_features = []
    for i in range(0, 254):
        penguin_features.append(str(i))
    penguin_label = 'y'
    penguins_X, penguins_y = penguins[penguin_features].values, penguins[penguin_label].values
    return penguins_X, penguins_y
