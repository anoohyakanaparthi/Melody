from django.shortcuts import render,redirect
from django.http import HttpResponse
import pickle
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import random
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def homepage(request):
    result=None
    if request.method=='POST':
        
        activities = ['study', 'work', 'cooking', 'workout', 'cleaning', 'sleeping', 'walking']
        moods = ['happy', 'sad', 'calm', 'energetic', 'anger']
        times = ['morning', 'afternoon', 'evening', 'night']
        genres = ['lofi', 'indie', 'classical', 'pop', 'metal', 'jazz']
        # Generate 100 synthetic rows
        rows = []
        for _ in range(100):
            rows.append({
                'age': random.randint(15, 50),
                'mood': random.choice(moods),
                'time': random.choice(times),
                'activity': random.choice(activities),
                'genre': random.choice(genres)
            })

        data = pd.DataFrame(rows)
        #step-2 preprocessing 
        #one hot encoding 
        x=pd.get_dummies(data.drop('genre',axis=1),drop_first=True)
        y=data['genre']

        
        #step-3 Split into train and test sets
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,stratify=y,random_state=7)

        #step-4 Train the model
        #model=DecisionTreeClassifier(random_state=42)
        #model.fit(x_train,y_train)

        model=RandomForestClassifier(random_state=42)
        model.fit(x_train,y_train)
        #y_pred=model.predict(x_test)
        #step-6 Accuracy
        #print('Accuracy:',accuracy_score(y_test,y_pred))

        columns=x.columns.tolist()
        print(columns)
        age=int(request.POST.get('age'))
        mood=request.POST.get('mood')
        time=request.POST.get('time')
        activity=request.POST.get('activity')
        df=pd.DataFrame({'age':[age],'mood':[mood],'time':[time],'activity':[activity]})
        df=pd.get_dummies(df)
        for col in columns:
            if col not in df.columns:
                df[col]=0
        df=df[columns]
        result=model.predict(df)[0]
    return render(request,'homepage.html',{'result':result})

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('num1')
        password = request.POST.get('num2')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('homepage')
    return render(request,'login.html')

def registration(request):
    if request.method == 'POST':
        username = request.POST.get('num1')
        password = request.POST.get('num2')
        conform = request.POST.get('num3')
        if password != conform:
            return render(request,'registration.html',{'result':'ERROR'})
        user=User.objects.create_user(username=username,password=password)
        return redirect('login')
    return render(request,'registration.html')
def home(request):
    return render (request,'homepage.html')
def logoutpage(request):
    logout(request)
    return redirect('login')
