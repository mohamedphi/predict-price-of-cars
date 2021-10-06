from flask import Flask , render_template , Request
from flask.globals import request
import joblib
app=Flask(__name__)
model=joblib.load("model.h5")
scaler=joblib.load("scaler.h5")
feull=["Diesel" ,"Electric","LPG","Petrol"]
Transmission=["Manual"]
Location_n=['Location_Bangalore',
       'Location_Chennai', 'Location_Coimbatore', 'Location_Delhi',
       'Location_Hyderabad', 'Location_Jaipur', 'Location_Kochi',
       'Location_Kolkata', 'Location_Mumbai', 'Location_Pune']
company_n=['company_Audi',
       'company_BMW', 'company_Bentley', 'company_Chevrolet', 'company_Datsun',
       'company_Fiat', 'company_Force', 'company_Ford', 'company_Honda',
       'company_Hyundai', 'company_ISUZU', 'company_Isuzu', 'company_Jaguar',
       'company_Jeep', 'company_Lamborghini', 'company_Land',
       'company_Mahindra', 'company_Maruti', 'company_Mercedes-Benz',
       'company_Mini', 'company_Mitsubishi', 'company_Nissan',
       'company_Porsche', 'company_Renault', 'company_Skoda', 'company_Smart',
       'company_Tata', 'company_Toyota', 'company_Volkswagen',
       'company_Volvo']
Owner=['Owner_Type_Fourth_Above', 'Owner_Type_Second', 'Owner_Type_Third']
@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")
@app.route("/predict",methods=["GET"])
def predict():
    liput_list=[request.args.get("model_of_cars"),request.args.get("Kilometers_Driven")
    , request.args.get("Seats"),request.args.get("Engine"),request.args.get("Power"),
    request.args.get("Mileage")
             ]
   
    fuell_demies=[0 for i in range(4)]
    Transmission_demies=[0 for i in range(1)]
    location_demies=[0 for i in range(10)]
    company_demies=[0 for i in range(30)]
    owner_demies=[0 for i in range(3)]
    try:
        fuell_demies[feull.index(request.args.get("Fuel_Type"))]=1
    except:
        pass
    try:
        Transmission_demies[Transmission.index(request.args.get("Transmission_Type"))]=1
    except:
        pass
    try:
        location_demies[Location_n.index(request.args.get("Location"))]=1
    except:
        pass
    try:
        company_demies[company_n.index(request.args.get("company"))]=1
    except:
        pass
    try:
        owner_demies[Owner.index(request.args.get("Owner_Type"))]=1
    except:
        pass
    liput_list+=fuell_demies
    liput_list+=Transmission_demies
    liput_list+=location_demies
    liput_list+=company_demies
    liput_list+=owner_demies
    liput_list=[int(x)for x in liput_list]
  
    predict = model.predict(scaler.transform([liput_list]))[0]

    return render_template("index.html",predict=predict)




if __name__ =="__main__":
    app.run(debug=True,port="9000")