
def task8(minutes):

    hours = int(minutes/60)
    remaining_minutes = minutes % 60

    if hours == 1 :
        hours_str = '1 hour'
    elif hours < 1 :
        hours_str = '0 hours'
    else:
        hours_str = str(hours) +' hours'    

    if remaining_minutes == 1:
        minutes_str = '1 minute'
    elif remaining_minutes > 1:
        minutes_str = str(remaining_minutes) +' minutes'
    else: 
        minutes_str = '0 minutes' 

    hours_and_minutes = hours_str +', '+ minutes_str
    return hours_and_minutes

print(task8(71))
print(task8(133))
print(task8(1))
  

