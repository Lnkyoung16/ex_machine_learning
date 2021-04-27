import pandas as pd

def query_card_number(card_number):
    df = pd.read_csv("./database/database.csv", index_col=0)

    if str(card_number) in df.values:
        return 1
    else:
        return 0



if True :
    print("True")