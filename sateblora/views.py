from django.shortcuts import render

import pandas as pd
import requests as re 
from django.http import JsonResponse
import json
import ast


def index(request):
	url = 'https://webapi.bps.go.id/v1/api/list'
	params = {
		'model': 'infographic',
		'lang': 'ind',
		'domain': '3316',
		'page':1,
		'key': '6c0136a5ba2dc0794749c4fe5bbcffea'
	}

	res = re.get(url, params=params)
	data = res.json()
	posts = data['data'][1]
	judul_infografis = []
	gambar_infografis = []
	download_infografis = []

	for item in posts:
	    judul_infografis.append(item['title'])
	    gambar_infografis.append(item['img'])
	    download_infografis.append(item['dl'])

	infografis_all = zip(judul_infografis,gambar_infografis,download_infografis)


	initdf = pd.read_csv('https://docs.google.com/spreadsheets/d/'+
					'1MSafdFvvdyqJrRKwLFN0xqpNKIsMbBXZPz9tVjG-1-w'+
					'/export?gid=0'+
                    '&format=csv',
                     dtype=str,
                     # Parse column values to datetime
                    )

	nama_indikator = initdf['indikator']
	tahun_indikator = initdf['tahun']	
	nilai_indikator = initdf['nilai']
	satuan_indikator = initdf['satuan']
	icon_indikator = initdf['icon']
	ket_indikator = initdf['keterangan']

	indikator_all = zip(nama_indikator,tahun_indikator,nilai_indikator,satuan_indikator,icon_indikator,ket_indikator)

	context = {
		'Title' : 'SateBlora | Satu Datane Blora ',
		'Heading' : 'Dashboard Data',
		'infografis_all':infografis_all,
		'indikator_all':indikator_all,

	}

	return render(request, 'index.html', context)

def load_more_infografis(request):
	offset=int(request.POST['offset'])
	page=(offset/10)+1
	url = 'https://webapi.bps.go.id/v1/api/list'
	params = {
		'model': 'infographic',
		'lang': 'ind',
		'domain': '3316',
		'page':page,
		'key': '6c0136a5ba2dc0794749c4fe5bbcffea'
	}
	posts=[]

	res = re.get(url, params=params)
	data = res.json()

	posts = data['data'][1]
	totalresult = data['data'][0]['total']
	return JsonResponse(data={
		'posts':posts,
		'totalResult':totalresult,
	})


#####################################################################################################################
def load_init_pub(request):
	url = 'https://webapi.bps.go.id/v1/api/list'
	params = {
		'model': 'publication',
		'lang': 'ind',
		'domain': '3316',
		'page':1,
		'key': '6c0136a5ba2dc0794749c4fe5bbcffea'
	}

	res = re.get(url, params=params)
	data = res.json()
	posts = data['data'][1]
	totalitem = data['data'][0]

	return JsonResponse(data={
		'posts':posts,
		'totalitem':totalitem
	})

def load_more_pub(request):
	offset=int(request.POST['offset'])
	page=(offset/10)+1
	url = 'https://webapi.bps.go.id/v1/api/list'
	params = {
		'model': 'publication',
		'lang': 'ind',
		'domain': '3316',
		'page':page,
		'key': '6c0136a5ba2dc0794749c4fe5bbcffea'
	}
	posts=[]

	res = re.get(url, params=params)
	data = res.json()

	posts = data['data'][1]
	totalresult = data['data'][0]['total']
	return JsonResponse(data={
		'posts':posts,
		'totalResult':totalresult,
	})

def detail_pub(request):
	indekspub=request.POST['offset']
	url = 'https://webapi.bps.go.id/v1/api/view'
	params = {
		'model': 'publication',
		'lang': 'ind',
		'domain': '3316',
		'id':indekspub,
		'key': '6c0136a5ba2dc0794749c4fe5bbcffea'
	}
	res = re.get(url, params=params)
	data = res.json()
	posts = data['data']

	return JsonResponse(data={
		'posts':posts,
	})

def cari_pub(request):
	keyword=request.POST['offset']
	posts=[]
	if len(keyword) > 2:
		for i in range(100):
			url = 'https://webapi.bps.go.id/v1/api/list'
			params = {
				'model': 'publication',
				'lang': 'ind',
				'domain': '3316',
				'page':i+1,
				'key': '6c0136a5ba2dc0794749c4fe5bbcffea',
				'keyword': keyword
			}
			res = re.get(url, params=params)
			data = res.json()
			if data['data-availability'] != 'list-not-available':
				posts.extend(data['data'][1])
			else:
				break
	return JsonResponse(data={
		'posts':posts,
	})


#####################################################################################################################
def load_init_brs(request):
	url = 'https://webapi.bps.go.id/v1/api/list'
	params = {
		'model': 'pressrelease',
		'lang': 'ind',
		'domain': '3316',
		'page':1,
		'key': '6c0136a5ba2dc0794749c4fe5bbcffea'
	}

	res = re.get(url, params=params)
	data = res.json()
	posts = data['data'][1]
	totalitem = data['data'][0]

	return JsonResponse(data={
		'posts':posts,
		'totalitem':totalitem
	})

def load_more_brs(request):
	offset=int(request.POST['offset'])
	page=(offset/10)+1
	url = 'https://webapi.bps.go.id/v1/api/list'
	params = {
		'model': 'pressrelease',
		'lang': 'ind',
		'domain': '3316',
		'page':page,
		'key': '6c0136a5ba2dc0794749c4fe5bbcffea'
	}
	posts=[]

	res = re.get(url, params=params)
	data = res.json()

	posts = data['data'][1]
	totalresult = data['data'][0]['total']

	return JsonResponse(data={
		'posts':posts,
		'totalResult':totalresult,
	})

def detail_brs(request):
	indeksbrs=request.POST['offset']
	url = 'https://webapi.bps.go.id/v1/api/view'
	params = {
		'model': 'pressrelease',
		'lang': 'ind',
		'domain': '3316',
		'id':indeksbrs,
		'key': '6c0136a5ba2dc0794749c4fe5bbcffea'
	}
	res = re.get(url, params=params)
	data = res.json()
	posts = data['data']
	return JsonResponse(data={
		'posts':posts,
	})

def cari_brs(request):
	keyword=request.POST['offset']
	posts=[]
	if len(keyword) > 2:
		for i in range(100):
			url = 'https://webapi.bps.go.id/v1/api/list'
			params = {
				'model': 'pressrelease',
				'lang': 'ind',
				'domain': '3316',
				'page':i+1,
				'key': '6c0136a5ba2dc0794749c4fe5bbcffea',
				'keyword': keyword
			}
			res = re.get(url, params=params)
			data = res.json()
			if data['data-availability'] != 'list-not-available':
				posts.extend(data['data'][1])
			else:
				break
	print(posts)
	return JsonResponse(data={
		'posts':posts,
	})

#####################################################################################################################
def load_init_berita(request):
	url = 'https://webapi.bps.go.id/v1/api/list'
	params = {
		'model': 'news',
		'lang': 'ind',
		'domain': '3316',
		'page':1,
		'key': '6c0136a5ba2dc0794749c4fe5bbcffea'
	}

	res = re.get(url, params=params)
	data = res.json()
	posts = data['data'][1]
	totalitem = data['data'][0]
	return JsonResponse(data={
		'posts':posts,
		'totalitem':totalitem
	})
def load_more_berita(request):
	offset=int(request.POST['offset'])
	page=(offset/10)+1
	url = 'https://webapi.bps.go.id/v1/api/list'
	params = {
		'model': 'news',
		'lang': 'ind',
		'domain': '3316',
		'page':page,
		'key': '6c0136a5ba2dc0794749c4fe5bbcffea'
	}
	posts=[]

	res = re.get(url, params=params)
	data = res.json()

	posts = data['data'][1]
	totalresult = data['data'][0]['total']
	return JsonResponse(data={
		'posts':posts,
		'totalResult':totalresult,
	})

def detail_berita(request):
	indeksberita=request.POST['offset']
	url = 'https://webapi.bps.go.id/v1/api/view'
	params = {
		'model': 'news',
		'lang': 'ind',
		'domain': '3316',
		'id':indeksberita,
		'key': '6c0136a5ba2dc0794749c4fe5bbcffea'
	}
	res = re.get(url, params=params)
	data = res.json()
	posts = data['data']
	return JsonResponse(data={
		'posts':posts,
	})
def cari_berita(request):
	keyword=request.POST['offset']
	posts=[]
	print(keyword)
	if len(keyword) > 2:
		for i in range(100):
			url = 'https://webapi.bps.go.id/v1/api/list'
			params = {
				'model': 'news',
				'lang': 'ind',
				'domain': '3316',
				'page':i+1,
				'key': '6c0136a5ba2dc0794749c4fe5bbcffea',
				'keyword': keyword
			}
			res = re.get(url, params=params)
			data = res.json()
			if data['data-availability'] != 'list-not-available':
				posts.extend(data['data'][1])
			else:
				break
	
	return JsonResponse(data={
		'posts':posts,
	})


#####################################################################################################################
def load_init_data(request):
	sosial = []
	ekonomi = []
	pertanian = []
	
	with open(r"static/json/sosial.json") as f:
	    data1 = f.read()
	with open(r"static/json/ekonomi.json") as f:
	    data2 = f.read()
	with open(r"static/json/pertanian.json") as f:
	    data3 = f.read()
	sosial = list(ast.literal_eval(data1))
	ekonomi = list(ast.literal_eval(data2))
	pertanian = list(ast.literal_eval(data3))

	return JsonResponse(data={
		'sosial':sosial,
		'ekonomi':ekonomi,
		'pertanian':pertanian,
	})

def load_more_data(request):
	posts=[]
	offset=str(request.POST['offset'])
	# print(offset)
	#STATICTABLE
	for i in range(100):
		url = 'https://webapi.bps.go.id/v1/api/list'
		params = {
			'model': 'statictable',
			'lang': 'ind',
			'domain': '3316',
			'subject':int(offset.split("_")[1]),
			'page':i+1,
			'key': '6c0136a5ba2dc0794749c4fe5bbcffea'
		}
		res = re.get(url, params=params)
		data = res.json()
		if data['data-availability'] != 'list-not-available':
			posts.extend(data['data'][1])
		else:
			break
	  
	
	return JsonResponse(data={
		'posts':posts,
	})
def detail_data(request):
	posts=[]
	offset=str(request.POST['offset'])
	url = 'https://webapi.bps.go.id/v1/api/view'
	params = {
		'model': 'statictable',
		'lang': 'ind',
		'domain': '3316',
		'id':offset,
		'key': '6c0136a5ba2dc0794749c4fe5bbcffea'
	}
	res = re.get(url, params=params)
	data = res.json()
	posts = data['data']
	return JsonResponse(data={
		'posts':posts,
	})