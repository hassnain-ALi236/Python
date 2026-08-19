# CSV FILES

import pandas as pd

# Create
data = {
    "Name": ["Ali", "Sara", "Ahmed"],
    "Age": [20, 22, 19],
    "City": ["Lahore", "Karachi", "Islamabad"]
}
df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)

# Read
df_csv = pd.read_csv("students.csv")
print(df_csv)

# # Excel FIle
import pandas as pd

# Create
data = {
    "Name": ["Ali", "Sara", "Ahmed"],
    "Age": [20, 22, 19],
    "City": ["Lahore", "Karachi", "Islamabad"]
}
df = pd.DataFrame(data)
df.to_excel("students.xlsx", index=False)

# Read
df_excel = pd.read_excel("students.xlsx")
print(df_excel)

# JSON FILE
import pandas as pd

# Create
data = {
    "Name": ["Ali", "Sara", "Ahmed"],
    "Age": [20, 22, 19],
    "City": ["Lahore", "Karachi", "Islamabad"]
}
df = pd.DataFrame(data)
df.to_json("students.json")

# Read
df_json = pd.read_json("students.json")
print(df_json)