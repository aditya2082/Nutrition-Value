from django.shortcuts import render

# # Create your views here.
# def home(request):
#     import requests
    
#     query = '1lb brisket and fries'
#     api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
#     response = requests.get(api_url, headers={'X-Api-Key': 'nG52QrHGJ+yKrzihkCFNMg==mFc8eAzaH4hDqatb'})
#     if response.status_code == requests.codes.ok:
#         print(response.text)
#     else:
#         print("Error:", response.status_code, response.text)


#     return render(request, 'home.html')




def home(request):
    import requests
    import json
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query, headers = {'X-Api-Key': 'nG52QrHGJ+yKrzihkCFNMg==mFc8eAzaH4hDqatb'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)

        except Exception as e:
            api = "Oops! There Was an Error !!"
            print(e)

        return render(request, 'home.html', {'api':api})
    else:
        return render(request, 'home.html', {'query':'Enter a valid query'})
