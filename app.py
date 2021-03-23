from flask import Flask, render_template,request
import pymongo
app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def homepage():
    return render_template('index.html')

@app.route('/rajasthantour', methods = ['GET','POST'])
def rajasthan():
    return render_template('rajasthantour.html')

@app.route('/gujarat', methods = ['GET','POST'])
def gujarat():
    return render_template('gujarat.html')

@app.route('/himachal', methods = ['GET','POST'])
def himachal():
    return render_template('himachal.html')

@app.route('/travelnow', methods = ['GET','POST'])
def travelnow():
    return render_template('travelnow.html')

@app.route('/contactus', methods = ['POST'])
def lastpage():
    if request.method == 'POST':
        name = request.form["name"]
        email =request.form['inputEmail4']
        address = request.form['inputAddress']
        city = request.form['inputCity']
        zip = request.form['inputZip']
        phone = request.form['phoneno']
        CONNECTION_URL = 'mongodb+srv://gaurav:gaurav10@cluster0.w5eom.mongodb.net/userdata?retryWrites=true&w=majority'
        client = pymongo.MongoClient(CONNECTION_URL)
        dataBase = client['userdata']
        COLLECTION_NAME = "gktour"
        collection = dataBase[COLLECTION_NAME]
        records = {'Name': name, 'Email': email, 'Adress': address, 'City': city, 'Zip': zip, 'phone_no': phone}

        rec = collection.insert_one(records)

        # print(name,email,address,city,zip,phone)

    return render_template('contact.html',name = name)

if __name__ == '__main__':
    app.run()





