import math

from Demos.win32cred_demo import mc

from model import ModelClock as MC

def getClockAngle(h, m):
    mc = MC()
    
    #verifica se a petição já foi calculada
    sql = """SELECT * FROM queries WHERE hour=%s AND minutes=%s"""
    r = mc.select(sql, (h,m))
    if len(r) > 0:
        print('angle db')
        return {'angle':r[0][3]} #retorna o ângulo do banco de dados
    else:
        angle = clockToAngle(h,m)
        mc.insert(h, m, angle) #inserir o novo ângulo no banco de dados
        print('new angle')
        return {'angle':angle}

def getQueries():
    sql = """SELECT * FROM queries"""
    r = mc.select(sql)
    return r

#calcula o ângulo dos ponteiros do relógio com hora e minuto fornecidos
def clockToAngle(h,m):
    hour = (60 * h + m) / 2.0
    minute = 6 * m
    angle = abs(hour - minute)

    if angle > 180:
        angle = 360 - angle
        
    return math.floor(angle)

if __name__ == '__main__':
    getClockAngle(2,2)