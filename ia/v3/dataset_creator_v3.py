import csv
from datetime import datetime, timedelta

import pandas as pd

from payloads_dataset import *

pattern_time = "%Y-%m-%d %H:%M:%S.%f"
pattern_time_out = "%Y-%m-%d %H:%M:%S.00000"


def binary_pure(key, value, get_random=0):
    result = bytes(value.encode())
    binary_list = {key: get_random}
    for byte in result:
        represent = int(bin(byte), 2)
        binary_list[(len(binary_list.keys()) - 2) + 1] = represent
    return binary_list


def to_binary(key: str, value: str, get_random):
    binary_list = binary_pure(key, value, get_random)

    while len(binary_list.keys()) < 255:
        binary_list[(len(binary_list.keys()) - 2) + 1] = int(bin(0), 2)

    return binary_list


def pattern_data(payload_data, time):
    return payload_data.get("data") + "::" + str(time)


def append_timestamp(payload_data, timestamp, minutes=5):
    input_date = datetime.strptime(timestamp, pattern_time)

    plus_date = input_date + timedelta(minutes=minutes)
    minus_date = input_date - timedelta(minutes=minutes)
    positive_dates = pd.date_range(start=str(minus_date), end=str(plus_date), freq=pd.offsets.Minute(1))

    negative_dates = pd.date_range(start=str(input_date.date()), end=str(input_date.replace(hour=23, minute=59)),
                                   freq=pd.offsets.Minute(60))

    negative_dates = negative_dates.difference(positive_dates)

    plus_week = (input_date + timedelta(weeks=1)) + timedelta(minutes=minutes)
    minus_week = (input_date + timedelta(weeks=1)) - timedelta(minutes=minutes)
    positive_dates_week = pd.date_range(start=str(minus_week), end=str(plus_week), freq=pd.offsets.Minute(1)).values

    positive_dates.union(positive_dates_week)

    plus_week = (input_date - timedelta(weeks=1)) + timedelta(minutes=minutes)
    minus_week = (input_date - timedelta(weeks=1)) - timedelta(minutes=minutes)
    positive_dates_week = pd.date_range(start=str(minus_week), end=str(plus_week), freq=pd.offsets.Minute(1)).values

    positive_dates.union(positive_dates_week)

    positive_rows_method = []
    for each_positive_time in positive_dates:
        concat_positive_result = pattern_data(payload_data, each_positive_time)
        positive_rows_method.append(concat_positive_result)

    negative_rows_method = []
    for each_negative_time in negative_dates:
        concat_negative_result = pattern_data(payload_data, each_negative_time)
        negative_rows_method.append(concat_negative_result)

    return positive_rows_method, negative_rows_method


def write(writer_rows, time, signal, payload_data, time_to_append=5):
    positive_rows, negative_rows = append_timestamp(payload_data, time, time_to_append)
    for row in positive_rows:
        transformed = to_binary('y', row, signal)
        writer_rows.writerow(transformed)

    for row in negative_rows:
        transformed = to_binary('y', row, 0)
        writer_rows.writerow(transformed)


def write_for_payload(writer, payload_data, class_e):
    # positives
    timestamp_payload = payload_data.get("timestamp")
    write(writer, timestamp_payload, class_e, payload_data=payload_data)
    time_value = datetime.strptime(timestamp_payload, pattern_time)
    # negatives
    write(writer, datetime.strftime(time_value - timedelta(hours=2), pattern_time), 0, payload_data=payload_data,
          time_to_append=1)
    write(writer, datetime.strftime(time_value - timedelta(hours=1), pattern_time), 0, payload_data=payload_data,
          time_to_append=1)
    write(writer, datetime.strftime(time_value + timedelta(hours=1), pattern_time), 0, payload_data=payload_data,
          time_to_append=1)
    write(writer, datetime.strftime(time_value + timedelta(hours=2), pattern_time), 0, payload_data=payload_data,
          time_to_append=1)
    write(writer, datetime.strftime(time_value - timedelta(minutes=50), pattern_time), 0, payload_data=payload_data,
          time_to_append=1)
    write(writer, datetime.strftime(time_value - timedelta(minutes=40), pattern_time), 0, payload_data=payload_data,
          time_to_append=1)
    write(writer, datetime.strftime(time_value - timedelta(minutes=30), pattern_time), 0, payload_data=payload_data,
          time_to_append=1)
    write(writer, datetime.strftime(time_value - timedelta(minutes=20), pattern_time), 0, payload_data=payload_data,
          time_to_append=1)
    write(writer, datetime.strftime(time_value - timedelta(minutes=10), pattern_time), 0, payload_data=payload_data,
          time_to_append=1)
    write(writer, datetime.strftime(time_value + timedelta(minutes=10), pattern_time), 0, payload_data=payload_data,
          time_to_append=1)
    write(writer, datetime.strftime(time_value + timedelta(minutes=20), pattern_time), 0, payload_data=payload_data,
          time_to_append=1)
    write(writer, datetime.strftime(time_value + timedelta(minutes=30), pattern_time), 0, payload_data=payload_data,
          time_to_append=1)
    write(writer, datetime.strftime(time_value + timedelta(minutes=40), pattern_time), 0, payload_data=payload_data,
          time_to_append=1)
    write(writer, datetime.strftime(time_value + timedelta(minutes=50), pattern_time), 0, payload_data=payload_data,
          time_to_append=1)
    write(writer, datetime.strftime(time_value - timedelta(days=30), pattern_time), 0, payload_data=payload_data,
          time_to_append=1)
    write(writer, datetime.strftime(time_value + timedelta(days=30), pattern_time), 0, payload_data=payload_data,
          time_to_append=1)


def main():
    try:

        with open('penguins_v3.csv', mode="w", newline='') as csv_file:
            fieldnames = ['y']

            for i in range(0, 254):
                fieldnames.append(i)

            print(f'total length {len(fieldnames)}')

            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()

            print(fieldnames)

            write_for_payload(writer, payload_data=classe_1_payload_1, class_e=1)
            write_for_payload(writer, payload_data=classe_1_payload_2, class_e=1)
            write_for_payload(writer, payload_data=classe_1_payload_3, class_e=1)
            write_for_payload(writer, payload_data=classe_1_payload_4, class_e=1)
            write_for_payload(writer, payload_data=classe_1_payload_5, class_e=1)
            write_for_payload(writer, payload_data=classe_1_payload_6, class_e=1)
            write_for_payload(writer, payload_data=classe_1_payload_7, class_e=1)
            write_for_payload(writer, payload_data=classe_1_payload_8, class_e=1)
            write_for_payload(writer, payload_data=classe_1_payload_9, class_e=1)
            write_for_payload(writer, payload_data=classe_1_payload_10, class_e=1)
            write_for_payload(writer, payload_data=classe_1_payload_11, class_e=1)
            write_for_payload(writer, payload_data=classe_1_payload_13, class_e=1)
            write_for_payload(writer, payload_data=classe_1_payload_12, class_e=1)
            write_for_payload(writer, payload_data=classe_1_payload_14, class_e=1)
            write_for_payload(writer, payload_data=classe_1_payload_15, class_e=1)
            write_for_payload(writer, payload_data=classe_1_payload_16, class_e=1)
            write_for_payload(writer, payload_data=classe_1_payload_17, class_e=1)
            write_for_payload(writer, payload_data=classe_1_payload_18, class_e=1)
            write_for_payload(writer, payload_data=classe_1_payload_19, class_e=1)
            write_for_payload(writer, payload_data=classe_1_payload_20, class_e=1)
            write_for_payload(writer, payload_data=classe_1_payload_21, class_e=1)
            write_for_payload(writer, payload_data=classe_1_payload_22, class_e=1)
            write_for_payload(writer, payload_data=classe_1_payload_23, class_e=1)
            write_for_payload(writer, payload_data=classe_1_payload_24, class_e=1)
            write_for_payload(writer, payload_data=classe_1_payload_25, class_e=1)
            write_for_payload(writer, payload_data=classe_1_payload_26, class_e=1)
            write_for_payload(writer, payload_data=classe_1_payload_27, class_e=1)

            print("payload wrote")
    except FileNotFoundError:
        print("continue")


if __name__ == '__main__':
    main()
