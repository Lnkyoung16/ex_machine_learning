import pandas as pd

df = pd.DataFrame([],columns=["user_name", "card_number", "timestamp"])

new_data = {"user_name": "Kwanhoon Lee", "card_number": "1234567890123456", "timestamp":"2021/04/08"}

df = df.append(new_data, ignore_index=True)

df.to_csv("./data/test.csv")
