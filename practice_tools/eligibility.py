def check_attendance(attended,total):
    attendance=(total/attended)*100
    if attendance>=75:
        return "eligible"
    else:
        return"not eligible"