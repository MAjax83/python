secStr = input('введите время в секундах - ')
sec = int(secStr)

h = ((sec//3600))%24
m = (sec//60)%60
s = sec%60

print( '%02d:%02d:%02d'% (h, m, s) )