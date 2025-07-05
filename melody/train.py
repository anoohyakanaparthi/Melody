
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import random

#step-1 Data collection (simple dataset)
'''
data=pd.DataFrame({
    'age':[16,23,38,20,42,36,67,15,19,28],
    'mood':['happy','sad','calm','energetic','sad','anger','calm','energetic','anger','happy'],
    'time':['morning','evening','morning','night','afternoon','afternoon','evening','night','night','evening'],
    'activity':['study','work','cooking','workout','work','cleaning','sleeping','study','study','walking'],
    'genre':['lofi','indie','classical','pop','classical','metal','jazz','lofi','metal','indie']
})
'''
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
model=DecisionTreeClassifier(random_state=42)
model.fit(x_train,y_train)

model2=RandomForestClassifier(random_state=42)
model2.fit(x_train,y_train)

#step-5 Make predictions
y_pred=model.predict(x_test)
y_pred1=model2.predict(x_test)

print(y_test)
print(y_pred)

print(x_train.columns)
print(x_test.columns)

print("Train genres:", set(y_train))
print("Test genres:", set(y_test))

#step-6 Accuracy
print('Accuracy:',accuracy_score(y_test,y_pred))
print('Accuracy (RandomForest):',accuracy_score(y_test,y_pred1))