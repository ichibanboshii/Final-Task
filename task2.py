import sys

def process_data(data):
    total_time = 0
    runners = {}
    num_runners = 0
    fastest_time = sys.maxsize
    fastest_runner = None
    slowest_time = 0
    for line in data:
        if '::' not in line:
            if line != "END":
                print("Error in data stream. Ignoring. Carry on.")
                continue
            else:
                break
        else:
            runner_info = line.strip().split("::")
            runner_num = runner_info[0]
            time = int(runner_info[1])
            total_time += time
            num_runners += 1
            if time < fastest_time:
                fastest_time = time
                fastest_runner = runner_num
            if time > slowest_time:
                slowest_time = time

    avg_time = total_time / num_runners
    avg_time_min = int(avg_time // 60)
    avg_time_sec = int(avg_time % 60)

    fastest_time_min = int(fastest_time // 60)
    fastest_time_sec = int(fastest_time % 60)

    slowest_time_min = int(slowest_time // 60)
    slowest_time_sec = int(slowest_time % 60)

    print("Total Runners:", num_runners)
    print("Average Time: ", avg_time_min, "minutes", avg_time_sec, "seconds")
    print("Fastest Time: ", fastest_time_min, "minutes", fastest_time_sec, "seconds")
    print("Slowest Time: ", slowest_time_min, "minutes", slowest_time_sec, "seconds")
    print("Best Time Here: Runner #", fastest_runner)

def main():
    data = []
    while True:
        line = input("> ")
        if line.strip() == "END":
            break
        data.append(line)
    if not data:
        print("No data found. Nothing to do. What a pity.")
    else:
        process_data(data)

if __name__ == "__main__":
    print("Park Run Timer\n~~~~~~~~~~~~~~")
    print("Let's go!")
    main()
