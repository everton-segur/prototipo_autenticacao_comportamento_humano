from flask import Flask, request

from penguins_v3_decision_tree import get_result_for_decision_tree
from penguins_v3_naive_bayes import get_result_for_naive_bayes
from penguins_v3_random_forests import get_result_for_random_forests
from penguins_v3_gradient_boosting import get_result_for_gradient

application = Flask(__name__)


@application.route('/gradient', methods=["POST"])
def default_gradient():
    data = request.form.get("data")
    time_stamp = request.form.get("timestamp")
    payload = {
        "data": data,
        "timestamp": time_stamp
    }

    print(payload)
    return {"isAuthorized": get_result_for_gradient(payload)}


@application.route('/decision-tree', methods=["POST"])
def default_decision_tree():
    data = request.form.get("data")
    time_stamp = request.form.get("timestamp")
    payload = {
        "data": data,
        "timestamp": time_stamp
    }

    print(payload)
    return {"isAuthorized": get_result_for_decision_tree(payload)}


@application.route('/naive-bayes', methods=["POST"])
def default_naive_bayes():
    data = request.form.get("data")
    time_stamp = request.form.get("timestamp")
    payload = {
        "data": data,
        "timestamp": time_stamp
    }

    print(payload)
    return {"isAuthorized": get_result_for_naive_bayes(payload)}


@application.route('/random-forests', methods=["POST"])
def default_random_forests():
    data = request.form.get("data")
    time_stamp = request.form.get("timestamp")
    payload = {
        "data": data,
        "timestamp": time_stamp
    }

    print(payload)
    return {"isAuthorized": get_result_for_random_forests(payload)}


if __name__ == "__main__":
    application.run(host="0.0.0.0")
