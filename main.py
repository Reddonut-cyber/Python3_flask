from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/plot', methods=['GET', 'POST'])
def plot():
    if request.method == 'POST':
        #Get user inputs
        x_from = float(request.form.get('x_from'))
        x_to = float(request.form.get('x_to'))
        function = request.form.get('function')
        color = request.form.get('color')
        
        #Create x values
        x_values = np.linspace(x_from, x_to, 500)
        
        if function == 'sin':
            y_values = np.sin(x_values)
        elif function == 'cos':
            y_values = np.cos(x_values)
        elif function == 'x^2':
            y_values = x_values**2
        elif function == 'sqrt(x)':
            y_values = np.sqrt(x_values)
        else:
            y_values = x_values
            
        #Plot the funcion
        plt.figure()
        plt.plot(x_values, y_values, color=color)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Plot {function} function')
        plt.savefig(image_name)
        plt.close()
        
        return render_template('plot.html', image_name=image_name)
    return render_template('plot_form.html')

@app.route("/histogram", methods=["GET", "POST"])
def histogram():
    if request.method == "POST":
        # Get user inputs
        data = request.form.get("data")
        data_list = [float(x) for x in data.split(",")]

        # Plot the histogram
        plt.figure()
        plt.hist(data_list, bins=10, color="skyblue", edgecolor="black")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.title("Histogram of User Data")
        plt.savefig(image_name)
        plt.close()
        
        return render_template("histogram.html", image_name=image_name)
    return render_template("histogram_form.html")

if __name__ == "__main__":
    app.run(debug=True)