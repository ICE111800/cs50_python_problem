def main():
    time = input("What time is it? ")
    time_slot = convert(time)

    if 7.0 <= time_slot <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_slot <= 13.0:
        print("lunch time")
    elif 18.0 <= time_slot <= 19.0:
        print("dinner time")
    
            

def convert(time):
    if "p.m." in time or "a.m." in time:
        time_part, period = time.split(" ")
        time_part = str(time_part)
        period = str(period)

        hour, minute = time_part.split(":")
        hour = int(hour)
        minute = float(minute)

        if period == "p.m." and hour < 12:
            hour += 12
        elif period == "p.m." and hour == 12:
            hour = 12
        elif period == "a.m." and hour == 12:
            hour = 0
        else:
            hour = hour

        result = round(float(hour + (minute / 60)), 2)
        return result
    else:
        hour, minute = time.split(":")
        hour = int(hour)
        minute = float(minute)

        result = round(float(hour + (minute / 60)), 2)
        return result


if __name__ == "__main__":
    main()
    