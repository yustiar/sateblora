from django.shortcuts import render

import pandas as pd


def index(request):
	initdf = pd.read_csv('https://docs.google.com/spreadsheets/d/'+
					'1MSafdFvvdyqJrRKwLFN0xqpNKIsMbBXZPz9tVjG-1-w'+
					'/export?gid=0'+
                    '&format=csv',
                     dtype=str,
                     # Parse column values to datetime
                    )

	# print(initdf)
	nama_indikator = initdf['indikator']
	tahun_indikator = initdf['tahun']	
	nilai_indikator = initdf['nilai']
	satuan_indikator = initdf['satuan']
	icon_indikator = initdf['icon']
	ket_indikator = initdf['keterangan']

	indikator_all = zip(nama_indikator,tahun_indikator,nilai_indikator,satuan_indikator,icon_indikator,ket_indikator)
	print(indikator_all)

	context = {
		'Title' : 'SateBlora | Satu Datane Blora ',
		'Heading' : 'Dashboard Data',
		# 'posts':posts,
		'indikator_all':indikator_all,
	}

	return render(request, 'index.html', context)

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