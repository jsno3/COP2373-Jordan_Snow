# Format
# first_name,last_name,exam_1,exam_2,exam_3 (integers)

import csv


def main():

    entries_amount = input('How many students are being entered? ')

    with open('grades.csv', 'w', newline='') as new_file:

        fieldnames = ['first_name', 'last_name', 'exam_1', 'exam_2', 'exam_3']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

        csv_writer.writeheader()

        for i in range(int(entries_amount)):

            first = input("Enter Student's First Name: ")

            last = input("Enter Student's Last Name: ")

            exam_1 = int(input("Enter Student's Grade for Exam 1: "))

            exam_2 = int(input("Enter Student's Grade for Exam 2: "))

            exam_3 = int(input("Enter Student's Grade for Exam 3: "))

            d = {'first_name': first, 'last_name': last, 'exam_1': exam_1, 'exam_2': exam_2, 'exam_3': exam_3}

            csv_writer.writerow(d)


main()