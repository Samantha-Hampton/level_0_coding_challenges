def convert_to_time(num):
    hours = int(num / 60)
    minutes = num % 60
    if hours == 1:
        hours_plural = ""
    else:
        hours_plural = "s"

    if minutes == 1:
        minutes_plural = ""
    else:
        minutes_plural = "s"

    print(f"{hours} hour{hours_plural}, {minutes} minute{minutes_plural}")


convert_to_time(1)
