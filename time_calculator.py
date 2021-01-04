def add_time(start, duration, startday = None):
    week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    start_split = start.split()
    start_time_split = start_split[0].split(":")
    start_hour = int(start_time_split[0])
    start_minute = int(start_time_split[1])
    start_am_pm = start_split[1]

    duration_split = duration.split(":")
    duration_hours = int(duration_split[0])
    duration_minutes = int(duration_split[1])
    total_duration = (duration_hours * 60) + duration_minutes
    

    total_hours = start_hour + duration_hours
    
    total_minutes = start_minute + duration_minutes
    new_minutes = (start_minute + duration_minutes) % 60
    if total_minutes > 59:
        additional_hours = int(total_minutes/60)
        total_hours += additional_hours

    new_hour = total_hours % 12
    if new_hour == 0:
        new_hour = 12

    new_am_pm = None
    number_of_days = None

    
    if start_am_pm == "AM":
        if int(total_hours/12) % 2 == 0:
            new_am_pm = "AM"
        else:
            new_am_pm = "PM"

        left_till_next_day = (24*60) - ((start_hour*60) + start_minute)
        number_of_days = int(total_duration/(24*60))
        if total_duration % (24*60) > left_till_next_day:
            number_of_days += 1
    else:
        if int(total_hours/12) % 2 == 0:
            new_am_pm = "PM"
        else:
            new_am_pm = "AM" 
        left_till_next_day = (24*60) - (((start_hour+12)*60) + start_minute)
        number_of_days = int(total_duration/(24*60))
        if total_duration % (24*60) > left_till_next_day:
            number_of_days += 1


    if number_of_days == 0 and startday != None:
        new_time = str(new_hour) + ":" + str(new_minutes).zfill(2) + " " + new_am_pm + ", {}".format(startday.capitalize())
    elif number_of_days == 0:
        new_time = str(new_hour) + ":" + str(new_minutes).zfill(2) + " " + new_am_pm

    if number_of_days == 1 and startday != None:
        index1 = week_days.index(startday.capitalize())
        if index1 == 6:
            index2 = 0
        else:
            index2 = index1+1
        new_time = str(new_hour) + ":" + str(new_minutes).zfill(2) + " " + new_am_pm + ", {} (next day)".format(week_days[index2],)
    elif number_of_days == 1:
        new_time = str(new_hour) + ":" + str(new_minutes).zfill(2) + " " + new_am_pm + " (next day)"

    if number_of_days > 1 and startday != None:
        index1 = week_days.index(startday.capitalize())
        index2 = index1 + (number_of_days % 7)
        if index2 > 6:
            index2 = index2 % 7
        new_time = str(new_hour) + ":" + str(new_minutes).zfill(2) + " " + new_am_pm + ", {} ({} days later)".format(week_days[index2], number_of_days)
    elif number_of_days > 1:
        new_time = str(new_hour) + ":" + str(new_minutes).zfill(2) + " " + new_am_pm + " ({} days later)".format(number_of_days)

    return new_time