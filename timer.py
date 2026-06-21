import time

print("Welcome to the timer!")
print()
time_to_count = (int(input("How many seconds do you want to count? ")))
time_to_counting = 1
print(time_to_counting)
for i in range(time_to_count-1):
    time.sleep(1)
    time_to_counting = time_to_counting + 1
    print(time_to_counting)
print("Done!")



