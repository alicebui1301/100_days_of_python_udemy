import pandas

student_dict = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90,
}

student_data_frame = pandas.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    if row.Score >= 60:
        print(row.Student, row.Score)   