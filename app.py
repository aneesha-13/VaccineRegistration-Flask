from flask import Flask
from flask import render_template,request,jsonify
import csv,json

app = Flask(__name__,static_url_path='/static')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add',methods=['POST','GET'])
def add():
    if(request.method=='POST'):
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']
        age=request.form['age']
        vaccinated=request.form['vaccinated']
        # if(request.form['vaccinated']=="True"):
        #     vaccinated=True
        # else:
        #     vaccinated=False
        with open('data1.csv', mode='a') as csv_file:
            data = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            data.writerow([name, email, phone, age, vaccinated])
    return render_template('show.html')
    
        #print("successful")
        # userdata=dict(request.form)
        # print(userdata)
        # name=userdata["name"]
        # email=userdata["email"]
        # phone=userdata["phone"]
        # age=userdata["age"]
        # vaccinated=userdata["vaccinated"]
        # print(type(name))
        # print(type(email))
        # print(type(phone))
        # print(type(age))
        # print(type(vaccinated))
        # print(name)
        # print(email)
        # print(phone)
        # print(age)
        # print(vaccinated)

    # return render_template('show.html')

    
@app.route('/get_person_details')
def get_person_details():
    with open('data1.csv') as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        first_line = True
        details = []
        for row in data:
            if not first_line:
                name=row[0] if row[0]!="" else None
                email=row[1] if row[1]!="" else None
                phone=int(row[2]) if row[2]!="" else None
                age=int(row[3]) if row[3]!="" else None
                if(row[4]=="True"):
                    vaccinated=True
                elif (row[4]=="False"):
                    vaccinated=False
                else:  
                    vaccinated=None
                details.append({"name": name,"email": email,"phone": phone,"age": age,"vaccinated": vaccinated,})
            else:
                first_line = False
    # return render_template("all_details.html", details=details)
    # return json.dumps(details)
    return jsonify(details)
    



@app.route('/get_persons_vaccinated')
def get_persons_vaccinated():
    with open('data1.csv') as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        first_line = True
        details = []
        # details_dict={}
        # res=""
        for row in data:
            if not first_line:
                name=row[0] if row[0]!="" else None
                email=row[1] if row[1]!="" else None
                phone=int(row[2]) if row[2]!="" else None
                age=int(row[3]) if row[3]!="" else None
                if(row[4]=="True"):
                    vaccinated=True
                elif (row[4]=="False"):
                    vaccinated=False
                else:  
                    vaccinated=None
                if(vaccinated):
                    details.append({"name": name,"email": email,"phone": phone,"age": age,"vaccinated": vaccinated,})
                    # details_dict["name"]=row[0]
                    # details_dict["email"]=row[1]
                    # details_dict["phone"]=int(row[2])
                    # details_dict["age"]=int(row[3])
                    # details_dict["vaccinated"]=row[4]
                    # json_string=json.dumps(details_dict,indent=2)
                    # print(json_string)
                    # res+=json_string
            else:
                first_line = False
    #return render_template("all_vaccinated.html", details=details)
    #return json.dumps(details)
    return jsonify(details)



if __name__ == '__main__':
   app.run(debug=True)
