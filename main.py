from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()
# uvicorn main:app --reload
# main.py 파일에서 app을 실행
# --reload 저장될 때 restart 

# app => path operation decorator
# .get() => .get / .post  / .put / .delete = Operation
# 괄호 안은 path
@app.get('/blog')
def index(limit=10, published:bool = True, sort: Optional[str] = None): # => path operation function
    # only get 10 published blogs

    # 파라미터를 함수안에 선언 / 파라미터에 타입을 지정해줄 수 있음
    # 기본적으로 required가 적용
    # 디폴트값을 지정 가능
    if published : 
        return {'data': f'{limit} published blogs from the db'}
    else :
        return {'data': f'{limit} blogs from the db'}

@app.get('/blog/unpublished') # /blog/{id}와 매칭되면 에러
# {id} 보다 먼저 선언하면 다른 페이지로 인식
def unpublished(): 
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int): # type of parameter
    # 타입을 정의하지 않으면 string으로
    # 타입이 틀리면 에러메세지를 자동으로 생성!
    # fetch blog with id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    # fetch comments of blog with id = id
    return {'data' : {'1', '2'}}


# create model
class Blog(BaseModel) :
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(blog:Blog):
    #return request
    return {'data': f'Blog is created with title as {blog.title}'}

# if __name__ == "__main__" :
#     uvicorn.run(app, host="127.0.0.1", port=9000)