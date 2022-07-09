air_temp = {"Monday": 16.4, "Tuesday": 17.3, "Wednesday": 17.2, "Thursday": 14.5, "Friday": 18.9, "Saturday": 20.1, "Sunday": 20.4}

for k, v in air_temp.items():
    temp_f = (v * 1.8) + 32
    print("The air temperature on {} was {:.2f}`F.".format(k, temp_f))
