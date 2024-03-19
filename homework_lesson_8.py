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

        for row in data:
            row[1] = convert_to_uah(float(row[1]))
            row[2] = convert_to_uah(float(row[2]))
            row[3] = convert_to_uah(float(row[3]))
            row[4] = convert_to_uah(float(row[4]))
            row[5] = convert_to_uah(float(row[5]))
            row[6] = convert_to_uah(float(row[6]))
            row[7] = convert_to_uah(float(row[7]))
            row[8] = convert_to_uah(float(row[8]))
            row[9] = convert_to_uah(float(row[9]))
            row[10] = convert_to_uah(float(row[10]))
            row[11] = convert_to_uah(float(row[11]))
            row[12] = convert_to_uah(float(row[12]))

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
