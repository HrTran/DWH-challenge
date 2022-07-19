import pandas as pd
import glob
import os

def get_data_from(data_path):
    """
    e.g: data_path = '/data/accounts/'
    """
    all_changes = glob.glob(os.path.join(os.getcwd() + data_path, "*.json"))
    all_changes.sort()
    # print(all_changes)
    li = []
    for filename in all_changes:
        df = pd.read_json(filename)
        li.append(df)
    n = len(li)
    new_li = [li[x].rename(columns={'set': 'data'}) for x in range(0,n)]
    df = pd.concat(new_li, sort=False)
    return df[~df.index.duplicated(keep='last')]

accounts_path = '/data/accounts/'
cards_path = '/data/cards/'
sa_path = '/data/savings_accounts/'
accounts = get_data_from(accounts_path)
cards = get_data_from(cards_path)
sa = get_data_from(sa_path)

print("====================== Point 1 =====================")
print(accounts)
print(cards)
print(sa)
print("====================== Point 2 =====================")
account_table = accounts.loc[:, ['data']].T
card_table = cards.loc[:, ['data']].T
sa_table = sa.loc[:, ['data']].T

"""
>>> account_table
     account_id     name phone_number savings_account_id  address                    email card_id
data         a1  Anthony     87654321                sa1  Jakarta  anthony@anotherbank.com      c2
>>> card_table
     card_id card_number monthly_limit  status credit_used
data      c2    12123434         70000  ACTIVE       37000
>>> sa_table
     savings_account_id  status interest_rate_percent balance
data                sa1  ACTIVE                     4   33000
"""
account_n_card = pd.merge(account_table, card_table, on='card_id')
all = pd.merge(account_n_card, sa_table, on='savings_account_id')
print(all.T)
    