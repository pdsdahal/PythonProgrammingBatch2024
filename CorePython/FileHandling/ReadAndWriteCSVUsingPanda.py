import pandas as pd
import os

current_file_absolute_path = os.getcwd()
base_path = os.path.dirname(current_file_absolute_path)
file_path = os.path.join(base_path, 'Resources', 'Student.csv')

data_student_frame = pd.read_csv(file_path)

# Display the top five rows
print(data_student_frame.head(10))

# locate first row
data_row_zero = data_student_frame.loc[0]
print(data_row_zero)

# Check data types
print("\n\nData Types")
print(data_student_frame.dtypes)

# Get basic statistics
print("\n\nBasic statistics")
print(data_student_frame.describe())