# task 1

import csv

usd_to_uah_rate = 39.2

def convert_to_uah(usd_salary):
    return int(usd_salary * usd_to_uah_rate)

def convert_salaries(input_file, output_file):
    try:
        with open(input_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            headers = next(reader)
            data = list(reader)

        data = list(map(lambda row: [row[0]] + [convert_to_uah(float(cell)) for cell in row[1:]], data))

        with open(output_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data)

        print("Salaries converted and saved successfully.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    input_file = "test_file.csv"
    output_file = "salaries_uah.csv"
    convert_salaries(input_file, output_file)
