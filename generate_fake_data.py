from faker import Factory
import pandas as pd
import random

# To get data to try out this:
# https://sarahleejane.github.io/learning/python/2015/08/09/simple-tables-in-webapps-using-flask-and-pandas-with-python.html


def main():
    males = create_data('male', 20)
    females = create_data('female', 20)
    data = pd.concat([males, females], ignore_index=True)
    data.to_csv("dummy_data.csv")
    # Then to read the above file: data = pd.read_csv("dummy_data.csv", index_col=0)

def create_data(gender, size=10):
    fake = Factory.create()
    if gender=='male':
        names = [fake.name_male() for i in range(size)]
        gender = ['m' for i in range(size)]
    elif gender=='female':
        names = [fake.name_female() for i in range(size)]
        gender = ['f' for i in range(size)]
    else:
        raise Exception("UNCLEAR")
    origin = [fake.country() for i in range(size)]
    age = [random.randint(20,30) for i in range(size)]
    birth_month = [fake.month_name() for i in range(size)]
    data = pd.DataFrame(index=range(size), data=dict(
        names=names, gender=gender, origin=origin,
        age=age, birth_month=birth_month
        ))
    return data
