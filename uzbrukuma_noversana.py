server_logs = [
    "10:00:01 User:Janis Status:Success",
    "10:00:02 User:Admin Status:Fail",
    "10:00:03 User:Admin Status:Fail",
    "10:00:04 User:Admin Status:Fail",
    "10:00:05 User:Peteris Status:Fail",
    "10:00:06 User:Peteris Status:Success",
    "10:00:07 User:Peteris Status:Fail",
    "10:00:08 User:Admin Status:Success",
    "10:00:09 User:Guest Status:Fail",
    "10:00:10 User:Guest Status:Fail",
    "10:00:11 User:Guest Status:Fail",
    "10:00:12 User:Guest Status:Fail"
]

fail_counts = {}

for log in server_logs:
    parts = log.split(' ')
    user = parts[1].split(':')[1]
    status = parts[2].split(':')[1]

    if status == "Fail":
        fail_counts[user] = fail_counts.get(user, 0) + 1
        if fail_counts[user] == 3:
            print(f"!!! BAN: Lietotājs {user} bloķēts!!!")
    elif status == "Success":
        fail_counts[user] = 0
