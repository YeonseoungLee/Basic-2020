import datetime
current_year=datetime.datetime.now().year
current_month=datetime.datetime.now().month
current_day=datetime.datetime.now().day
birth_year,birth_month,birth_day=map(int, input('생일 입력> ').split())
if current_month> birth_month:              #현재월>생월
    age=current_year-birth_year
elif current_month<birth_month:             #현재월<생월
    age=current_year-birth_year-1
else:   
    if current_day< birth_day:              
        age= current_year-birth_year-1
    else:
        age=current_year-birth_year  
        
print('만나이는 %d입니다' % age)        