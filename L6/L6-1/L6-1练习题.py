#1.C
#2.B
def BMI(w,h):
    bmi = w/h*h
    if bmi <= 18.4:
        print('体重过轻')
    elif bmi >= 18.5 and <= 23.9:
        print('体重正常')
    elif bmi >= 24.0 and <= 27.9:
        print('体重过胖')
    else:
        print('肥胖！')