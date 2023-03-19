import sys, csv
from tabulate import tabulate

def main():
    data = check_com_line_arg()
    print(create_table(data))

def check_com_line_arg():
    try:
        assert len(sys.argv) > 1, "Too few command-line arguments"
        assert len(sys.argv) < 3, "Too many command-line arguments"
        assert sys.argv[1].endswith(".csv") == True, "Not a CSV file"
        return sys.argv[1]
    except AssertionError as message:
        sys.exit(message)

def create_table(data):
    try:
        price = []
        pizza = sys.argv[1][:-4].capitalize()
        with open(data, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                price.append({f"{pizza} Pizza": row[f"{pizza} Pizza"], "Small": row["Small"], "Large": row["Large"]})

        return tabulate(price, headers="keys", tablefmt="grid")
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()