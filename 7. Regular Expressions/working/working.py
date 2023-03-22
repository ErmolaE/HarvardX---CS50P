import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s = s.strip()
    if matches := re.search(r"^((?:[1-9]|1[0-2])(?::[0-5][0-9])? (?:AM|PM)) to ((?:[1-9]|1[0-2])(?::[0-5][0-9])? (?:AM|PM))$", s):
        f_times = []
        for match in matches.groups():
            l = match.split(" ")
            try:
                hours, minutes = l[0].split(":")
            except:
                hours = l[0]
                minutes = "00"
            if l[1] == "AM" and hours == "12":
                f_hours = 0
            elif l[1] == "PM" and hours != "12":
                f_hours = int(hours) + 12
            else:
                f_hours = int(hours)
            f_time = f"{f_hours:02}:{minutes}"
            f_times.append(f_time)
        return f"{f_times[0]} to {f_times[1]}"
    else:
        raise ValueError





if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()