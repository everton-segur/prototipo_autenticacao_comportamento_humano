from datetime import datetime, timedelta

import numpy as np
from sklearn.metrics import confusion_matrix, classification_report

from dataset_creator_v3 import pattern_data, to_binary, pattern_time

times = ["2021-10-17 04:54:00.00000",
         "2021-10-17 08:09:00.00000",
         "2021-10-17 12:59:00.00000",
         "2021-10-17 16:19:00.00000",
         "2021-10-17 17:07:00.00000",
         "2021-10-17 19:32:00.00000",
         "2021-10-17 21:19:00.00000",
         "2021-10-17 21:29:00.00000",
         "2021-10-18 09:54:00.00000",
         "2021-10-18 10:09:00.00000",
         "2021-10-18 13:59:00.00000",
         "2021-10-18 16:19:00.00000",
         "2021-10-20 17:11:00.00000",
         "2021-10-20 19:36:00.00000",
         "2021-10-20 21:29:00.00000",
         "2021-10-20 22:29:00.00000",
         "2021-10-20 08:49:00.00000",
         "2021-10-20 08:54:00.00000",
         "2021-10-20 12:59:00.00000",
         "2021-10-25 18:19:00.00000",
         "2021-10-25 11:59:00.00000",
         "2021-10-25 08:39:00.00000",
         "2021-10-25 04:59:00.00000",
         "2021-10-25 22:07:00.00000",
         "2021-10-27 01:32:00.00000",
         "2021-10-27 05:19:00.00000",
         "2021-10-27 13:29:00.00000",
         ]


def validation_test(transformed_positive, multi_model):
    new_array = []
    validation_array = []
    for dict_value in transformed_positive:
        validation_array.append(dict_value.get("class"))
        var = list(dict_value.get("binary_value").values())
        del var[0]
        new_array.append(var)
    x_new = np.array(new_array)
    penguin_pred = multi_model.predict(x_new)

    print(classification_report(validation_array, penguin_pred))
    print(confusion_matrix(validation_array, penguin_pred))


def validate_for_date_and_time(multi_model, payload):
    times_to_test = []

    for time in times:
        date = datetime.strptime(time, pattern_time)

        for i in range(1, 10):
            times_to_test.append({"time": date + timedelta(minutes=i), "class": 1 if i <= 5 else 0})
            times_to_test.append({"time": date - timedelta(minutes=i), "class": 1 if i <= 5 else 0})
        for i in range(1, 5):
            times_to_test.append({"time": date + timedelta(hours=i, minutes=5), "class": 0})
            times_to_test.append({"time": date - timedelta(hours=i, minutes=5), "class": 0})

        times_to_test.append({"time": datetime.strptime(time, pattern_time), "class": 1})

    result = []

    for transformed in times_to_test:
        result.append(
            {"binary_value": to_binary('y', pattern_data(payload_data=payload, time=transformed.get("time")), 0),
             "class": transformed.get("class")})

    return validation_test(result, multi_model)


def validate(multi_model, payload):
    pattern_data_time = pattern_data(payload_data=payload, time=payload.get("timestamp"))
    data = to_binary("y", pattern_data_time, 0)
    var = list(data.values())
    del var[0]

    return True if multi_model.predict(np.array([var]))[0] != 0 else False
