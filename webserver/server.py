import logging
from flask import jsonify,Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

#configure logging
#logging.basicConfig(filename='app.log', level=logging.DEBUG,                    format='%(asctime)s %(levelname)s %(message)s')

@app.route("/")
def my_home():
    #logging.info('Rendering home page')
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    #logging.info(f'Rendering page: {page_name}')
    return render_template(page_name)

def write_to_file(data):
    with open("database.txt", mode = "a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email},{subject},{message}")

def write_to_csv(data):
    with open("database.csv", mode = "a", newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = csv.writer(database2, delimiter=',',quoting=csv.QUOTE_MINIMAL)
        file.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
          #  logging.debug(f"Received form data: {data}")
            return redirect("/thankyou.html")
        except Exception as e:
         #   logging.error("Error occurred during form submission", exc_info=True)
            return "something went wrong with my csv or html redirection, try again!"
    else:
     #   logging.warning("GET request made to submit_form routine")
        return "something went wrong as its not a post method, try again!"

if __name__ == "__main__":
  #  logging.info("Starting Flask application")
    app.run()
