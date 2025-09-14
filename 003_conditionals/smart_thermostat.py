device_status = 'active'
temp = 34

if device_status == 'active':
    print("Device is on")
    if temp > 35:
        print("High Temperature Alert!")
    else:
        print('Normal Temperature')    
else:
    print("Device is offline")        