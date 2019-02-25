from flask import Flask,jsonify,request,abort
import json, time, subprocess
import threading
import schedule as sh
app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def enter_api_system():
    result = {
        "result": "enter api system"
    }
    return jsonify(result)


@app.route('/schedule', methods=['POST','GET'])
def schedule():
    config_schedule()
    return jsonify({"status":True})


def config_schedule():
    with open('config.json') as f:
        data = json.load(f)
        for test_case in data["testing_case"]:
            # testing_time_spacing
            print(test_case["program_name"])
            sh.every(test_case["testing_time_spacing"]).seconds.do(run_test, test_case["program_name"])
    f.close()
    threading.Thread(target=run).start()
    return jsonify({"status":True})

def run():
    while True:
        sh.run_pending()
        time.sleep(1)


def run_test(test_name):
    try:
        subprocess.run(["python","testing_case/" + test_name + ".py"])
    except Exception as e:
        print(e)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081)