from flask import Flask, render_template
import requests, schedule

app=Flask(__name__)

def indo():
	api_url="https://api.kawalcorona.com/indonesia/"
	rstl= requests.get(api_url).json()
	return rstl

def jabar():
	api_url="https://api.kawalcorona.com/indonesia/provinsi/"
	rstl= requests.get(api_url).json()
	cek=rstl[1]
	ambil_dic= cek ["attributes"]
	a=[ambil_dic]
	return a

r_indo=schedule.every(2).seconds.do(indo)
r_jabar=schedule.every(2).seconds.do(jabar)

data_indo=indo()
data_jabar=jabar()

@app.route("/")
def index():
	return render_template("index.html", data_indo=data_indo, data_jabar=data_jabar)

if __name__ == '__main__':
	app.run(debug=True)