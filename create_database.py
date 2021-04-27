import pandas as pd

df = pd.DataFrame([], columns=["user_name", "card_number", "timestamp", "cvc"])
df.to_csv("./database/database.csv")