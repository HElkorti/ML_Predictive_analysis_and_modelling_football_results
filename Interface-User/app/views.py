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
            season = 2022
            Day_code = 5


            # traitement : 

            svm = pickle.load(open("./app/mlModels/svmm.pkl", "rb"))

           # build a numpy array (ensure data types match the model's expectations)
            my_array = np.array([int(team_code), int(opponent_code), season, 
                                 int(round_code), int(venue_code), int(referee_code), 
                                 int(formation_code), Day_code, float(4), float(0.67) ,
                                 float(0.67) ,float(0.33) ,float(0.2)])

            # reshape the array if needed (SVM models usually expect a 2D array)
            my_array = my_array.reshape(1, -1)


            # predict :

            # make prediction
            winner_prediction = svm.predict(my_array)

            #svm.predict()

            




            context = {
                "winner": winner_prediction[0]  # Assuming winner_prediction is a single value
            }



            return render(request, "predict.html", context)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    else:
       return render(request, "predict.html") 



