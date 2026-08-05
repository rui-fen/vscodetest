from fastapi import FastAPI

app = FastAPI()

#字典
def process_items(prices: dict[str, float]):
     for name,price in prices.items():
        print(name,price)


##变量可以是若干种类型中的任意一种，比如既可以是 int 也可以是 str
def process_items(item: str | int):
    print(item)


#可以声明一个值的类型是某种类型（比如 str），但它也可能是 None。
def say_hi(name: str | None = None):
    if name is None:
        print("Hi, there!")
    else:
        print(f"Hi, {name}!")



class Person:
    def __init__(self,name : str):
        self.name = name

def get_person_name(one_person:Person):
    return one_person.name


#Pydantic 是一个用于执行数据校验的 Python 库