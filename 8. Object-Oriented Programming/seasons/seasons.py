from datetime import date
import inflect, sys


def main():
    user_date = input("Date of birth:")
    current_time = date.today()
    date_of_birth = get_date(user_date)
    age_words = get_age(date_of_birth, current_time)
    print(f"{age_words} minutes")


def get_date(user_date):
    try:
        l = user_date.strip().split("-")
        date_of_birth = date(int(l[0]), int(l[1]), int(l[2]))
        return date_of_birth
    except:
        sys.exit(1)


def get_age(date_of_birth, current_time):
    age = current_time - date_of_birth
    minutes = int(age.total_seconds()/60)
    age_words = inflect.engine().number_to_words(minutes, andword="")
    return age_words.capitalize()


if __name__ == "__main__":
    main()