def time_conversion(s):
    arr= s.split(":")
    if("PM" in s and int(arr[0])<12):
        return str(int(arr[0])+12)+":"+arr[1]+":"+arr[2].replace("PM","")
    if("PM" in s and int(arr[0])>=12):
        return s.replace("PM","")
    if("AM" in s and int(arr[0])==12):
        return "00:"+arr[1]+":"+arr[2].replace("AM","")
    return s.replace("AM","") 

print(time_conversion("06:40:03AM"))