from flask import Flask,escape,request,render_template
import pickle


vector=pickle.load(open("vectorizer.pkl","rb"))


model=pickle.load(open("fakenews_model.pkl",'rb'))



app = Flask(__name__,template_folder='templetes',static_folder='static')
#app = Flask(__name__, template_folder='../templates')
@app.route("/") 
def hello_world():
    return render_template('index.html')

@app.route('/prediction',methods=['GET','POST'])
def prediction():
    if request.method == "POST":
        news=str(request.form['news'])
        print(news)

        predict=model.predict(vector.transform([news]))[0]
        print(predict)

        return render_template('predict.html',prediction_text="News  is --> {}".format(predict))
    
    else:
        return render_template('predict.html')


if __name__ == '__main__':
    app.run()