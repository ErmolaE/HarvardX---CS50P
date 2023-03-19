import sys, csv


def main():
    old, new = check_com_line_arg()
    create_scv(old, new)

def check_com_line_arg():
    try:
        assert len(sys.argv) > 2, "Too few command-line arguments"
        assert len(sys.argv) < 4, "Too many command-line arguments"
        assert sys.argv[1].endswith(".csv") == True, "Not a CSV file"
        assert sys.argv[2].endswith(".csv") == True, "Not a CSV file"
        return sys.argv[1], sys.argv[2]
    except AssertionError as message:
        sys.exit(message)

def create_scv(old, new):
    try:
        hogwarts = []
        with open(old, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                last, first = row["name"].split(", ")
                hogwarts.append({"first": first, "last": last, "house": row["house"]})
        with open(new, "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in hogwarts:
                writer.writerow(row)
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()