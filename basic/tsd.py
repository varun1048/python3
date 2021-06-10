def TSD(time=0,destent=0,speed=0):
    if not speed:
        print(str(destent/time) +" km/hr")
    elif not time:
        print(str(destent/speed) +" hr")
    else:
        print(str(time*speed) +" km")


TSD(10,4)