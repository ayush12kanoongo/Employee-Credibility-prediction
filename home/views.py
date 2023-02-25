from django.shortcuts import render
from joblib import load 
model = load('./savedModules/employee.joblib')

def main(request):
    return render(request,'index.html')

def predictMPG(request):
    print (request) 
    #if request.method == 'POST':
        #temp ={}
    satisfaction_level=request.GET.get('satisfaction_level')
    last_evaluation=request.GET.get('last_evaluation')
    time_spend_company=request.GET.get('time_spend_company')
    work_accident=request.GET.get('work_accident')
    promotion_last_5years=request.GET.get('promotion_last_5years')
    dept=request.GET.get('dept')
    sal=request.GET.get('sal')
    result = model.predict([[satisfaction_level, last_evaluation, time_spend_company, work_accident, promotion_last_5years, dept,sal]])
        
    print(result)
    return render(request,'predictMPG.html',{'predictMPG' : result})
    
