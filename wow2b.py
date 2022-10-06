def implementAPI(logs):
    registered = {}
    loggedin = {}
    outlog = []
    
    for log in logs:
        words = log.strip().split()
        if words[0] == "register":
            username, password = words[1], words[2]
            if username in registered:
                outlog.append("Username already exists")
            else:
                registered[username] = password
                outlog.append("Registered Successfully")
        elif words[0] == "login":
            username, password = words[1], words[2]
            if username in loggedin:
                outlog.append("Login Unsuccessful")
            elif registered[username] != password:
                outlog.append("Login Unsuccessful")
            else:
                loggedin[username] = password
                outlog.append("Logged In Successfully")
        else:
            username = words[1]
            if username not in registered or username not in loggedin:
                outlog.append("Logout Unsuccessful")
            else:
                loggedin.pop(username)
                outlog.append("Logged Out Successfully")
    return outlog


print(implementAPI(["register david david123", "register adam 1Adam1", "login david david123", "login adam 1adam1", "logout david"]))

