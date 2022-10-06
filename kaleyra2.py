from datetime import date, datetime

def indian_to_iso(time):
    comp = time.split("-")
    iso = comp[2] + "-" + comp[1] + "-" + comp[0]
    return iso

def extract(params):
    time = params[2][1:-1]
    indian = time[:10]
    string =  indian_to_iso(indian) + "T" + time[11:]
    return datetime.fromisoformat(string)

def solve(N, logs, start_date, start_time, finish_date, finish_time):
    start = datetime.fromisoformat(indian_to_iso(start_date) + "T" + start_time)
    finish = datetime.fromisoformat(indian_to_iso(finish_date) + "T" + finish_time)
    
    
    for log in logs:
        params = log.split("__") # double underscore hai ye dhyan rakhna
        logtime = extract(log)
        if 400 <= params[4] <= 599 or not (start <= logtime <= finish):
            N -= 1
    
    print(N)
    
    
N = int(input())
logs = []
for i in range(N):
    logs.append(input())

start_date, start_time, finish_date, finish_time = input().split()