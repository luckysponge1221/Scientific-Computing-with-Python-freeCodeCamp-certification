def add_time(start, duration, start_day=''):
    hr_start, mnt_start = split_time_am_pm(start)
    hr_dur, mnt_dur = split_time(duration)

    minute = mnt_start + mnt_dur
    hour = hr_start + hr_dur
    am_pm = ''
    day = 0

    if minute >= 60:
        hour += int(minute/60)
        minute = minute % 60
    if minute < 10:
        minute = "0" + str(minute)
    
    if hour >= 24:
        day = int(hour/24)
        hour = hour % 24

    if hour == 0:
        hour = 12
        am_pm = "AM"
    elif hour > 0 and hour < 12:
        am_pm = "AM"
    elif hour == 12:
        hour = 12
        am_pm = "PM"
    elif hour > 12:
        hour -= 12
        am_pm = "PM"

    new_time = f"{hour}:{minute} {am_pm}"

    weekdays = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    
    if start_day != '':
        if start_day.lower() in weekdays:
            end_day = weekdays[(weekdays.index(start_day.lower()) + day) % 7].capitalize()
            new_time += f", {end_day}"
    else:
        end_day = ''

    if day == 1:
        new_time += f" (next day)"
    elif day > 1:
        new_time += f" ({day} days later)"

    return new_time

def split_time_am_pm(start):
    split_am_pm = start.split(' ')
    split_hour_minute = split_am_pm[0].split(':')

    hour = split_hour_minute[0]
    minute = split_hour_minute[1]

    print(split_am_pm)
    if split_am_pm[1] == 'PM':
        hour = 12 + int(hour)

    return int(hour), int(minute)

def split_time(dur):
    split_hour_minute = dur.split(':')
    print(split_hour_minute)
    hour = split_hour_minute[0]
    minute = split_hour_minute[1]
    return int(hour), int(minute)

start = '6:30 PM'
dur = '205:12'
start_day = 'tuesday'

print(add_time(start, dur, start_day))
