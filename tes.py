import requests, schedule

def indo():
	api_url="https://api.kawalcorona.com/indonesia/"
	rstl= requests.get(api_url).json()
	print(rstl)

def jabar():
	api_url="https://api.kawalcorona.com/indonesia/provinsi/"
	rstl= requests.get(api_url).json()
	cek=rstl[1]
	ambil_dic= cek ["attributes"]
	a=[ambil_dic]
	print(a)

r_indo=schedule.every(2).seconds.do(indo)
r_jabar=schedule.every(2).seconds.do(jabar)

while True:
	schedule.run_pending()

data_indo=indo()
print(data_indo)

data_jabar=jabar()
print(data_jabar)