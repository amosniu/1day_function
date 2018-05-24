#global的使用
def get_temp():
    global temp
    temp = 24
    print('当前的室温是%d'%temp)

def get_f_temp():
    temp_f = temp + 3
    print('当前的室温（华氏）是%d'%temp_f)

get_temp()

get_f_temp()