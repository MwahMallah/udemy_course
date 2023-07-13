student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}

import pandas

student_df = pandas.DataFrame(student_dict)

for index, row in student_df.iterrows():
    if row.student == "Angela":
        print(row.score)