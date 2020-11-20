from django.shortcuts import render

# Create your views here.

def addPageView(request):
	items = request.session.get('items', [])
	# handling post request
	print("Came to add!!")
	if request.method == 'POST':
		print("found post request")
		item = request.POST.get('content', '').strip()
		print("item value is :" + item)
		if len(item) > 0:
			items.append(item)
			print("items added")
		if len(items) > 10:
			items = items[1:]
			print("remove extra notes")
		request.session['items'] = items

	return render(request, 'pages/index.html', {'items' : items})


def erasePageView(request):
	items = request.session.get('items', [])

	if request.method == 'POST':
		item = request.POST.get('content', '').strip()
		if len(item) > 0:
			items.remove(item)
		request.session['items'] = items

	return render(request, 'pages/index.html', {'items' : items})

def homePageView(request):
	items = request.session.get('items', [])
	# shorter way of writing instead of loader
	return render(request, 'pages/index.html', {'items' : items})