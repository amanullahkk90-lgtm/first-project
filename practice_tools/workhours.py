def check_hours(hours):
    hour=sum(hours)
    if hour >=40:
        return "Target met"
    else:
        return "below target"