from datetime import datetime
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": 123,
    "signup_ts": "2024-06-01 12:22",
    "friends": [1, "2", b"3"],
}

user = User(**external_data)
print(user)

#FastAPI 利用这些类型提示来完成多件事情。

#在 FastAPI 中，用类型提示来声明参数，你将获得：

#编辑器支持。
#类型检查。
#并且 FastAPI 会使用相同的声明来：

#定义要求：从请求路径参数、查询参数、请求头、请求体、依赖等。
#转换数据：把请求中的数据转换为所需类型。
#校验数据：对于每个请求：
#当数据无效时，自动生成返回给客户端的错误。
#使用 OpenAPI 记录 API：
#然后用于自动生成交互式文档界面。


@app.get('/burgers')
async def read_burgers():
    burgers = await get_burgers(2)
    return burgers