from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from sklearn.svm import SVC
import numpy as np 
import pickle

import json 


def predict_page(request):

    if request.method == 'POST':
        try:

            team_code = request.POST.get('team_code')
            opponent_code = request.POST.get('Opponent_code')
            round_code = request.POST.get('Round_code')
            venue_code = request.POST.get('Venue_code')
            referee_code = request.POST.get('Referee_code')
            formation_code = request.POST.get('Formation_code')

            # traitement : 

            svm = pickle.load(open("./app/mlModels/svm.pkl", "rb"))

            # build a numpy array


            # predict :

            #svm.predict()



            context = {
                "winner" : "pass the winner here"
            }

            return render(request, "predict.html", context)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    else:
       return render(request, "predict.html") 



