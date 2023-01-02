from flask import Flask, render_template, request
import pickle
import pandas
import numpy as np

app = Flask(__name__)


def motion_prediction(to_predict_list):
    to_predict_list = np.array(to_predict_list).reshape(1,4)
    loaded_model = pickle.load(open("model.pkl", "rb"))
    result = loaded_model.predict(to_predict_list)
    return result[0]

@app.route('/', methods=['GET','POST'])
def predict():

    

    if request.method == 'POST':
       timestamp = request.form.get("timestamp")
       x_axis = request.form.get("x-axis")
       y_axis = request.form.get("y-axis")
       z_axis = request.form.get("z-axis")
       
       x_axis = float(x_axis)
       y_axis = float(y_axis)
       z_axis = float(z_axis)

       input = []
       input.append(timestamp)
       input.append(x_axis)
       input.append(y_axis)
       input.append(z_axis)

       input = list(map(float, input))
       result = motion_prediction(input)
       action = ""
       
       motion_dict = {
          0:"Downstairs",
          1:"Jogging",
          2:"Sitting",
          3:"Standing",
          4:"Upstairs",
          5:"Downstairs",
       }
       
       activity = motion_dict[result]
       print(activity)
       Final_result = "The person is " + ' ' + str(result)
       return render_template('result.html', prediction = str(activity))

    else:
        return render_template('home.html')

    

if __name__ == '__main__':
    app.run(debug=True)

