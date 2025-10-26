import sys

time_spent_at_work = int(sys.stdin.readline().strip())

break_time = 0
for minute in range(time_spent_at_work):
    work_time = time_spent_at_work - break_time
    # Alice spends a minute AT WORK
    if work_time > 360 and break_time < 30:
        break_time += 1
    elif work_time > 540 and break_time < 45:
        break_time += 1
    elif work_time > 600:
        break_time += 1

print(break_time)
