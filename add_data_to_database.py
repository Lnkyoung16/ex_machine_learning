import pandas as pd
import time
import random

for i in range(2, 20):
    if i % 2 == 0:
        print(i)
    else:
        print("bear")
    print("pass")

def add_data_to_database(user_name="", card_number=""):
    # load a database file from database dir
    df = pd.read_csv("./database/database.csv", index_col=0)
    pd.to_csv()

    current_time = time.strftime('%Y/%m/%d', time.localtime(time.time()))

    cvc = ""
    for i in range(0, 3):
        cvc += str(random.randint(0, 9))

    new_data = {"user_name": user_name , "card_number": card_number, \
                "timestamp": current_time , "cvc": cvc}

    df = df.append(new_data, ignore_index=True)
    df.to_csv("./database/database.csv")
