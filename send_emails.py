import csv

def main():
    emails_list = get_recipients("emails.csv")
    for r in emails_list:
        print(r)


def get_recipients(filename):
    emails_list = []
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            emails_list.append(row["email"])
    return emails_list

if __name__ == "__main__":
    main() 