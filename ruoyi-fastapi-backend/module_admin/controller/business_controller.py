from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import HTMLResponse
from fastapi import APIRouter, File, UploadFile, HTTPException
from module_admin.cloudflare_db.controller import ProjectDatabase, ClientDatabase



businessController = APIRouter(prefix='/business', tags=['业务模块'])

@businessController.get("/test", summary="测试API")
async def test_api():
    return {"message": "Hello, World!"}

@businessController.get("/projects", summary="获取完整项目列表")
async def get_all_projects():
    db = ProjectDatabase()
    projects = db.list_all_projects()
    print(projects)
    return projects

@businessController.get("/clients", summary="获取完整客户列表")
async def get_all_clients():
    db = ClientDatabase()
    clients = db.list_all_clients()
    print(clients)
    return clients

from pydantic import BaseModel

class Client(BaseModel):
    name: str
    abn: str
    contact: str
    method: str
    details: str
    note: str
    client_id: str
    created_by: str
    created_time: str

@businessController.post("/add_clients", summary="添加新客户")
async def add_client(data:Client):
    db = ClientDatabase()
    db.insert_client([data.dict()])
    return {"code": 200}

@businessController.post("/update_clients", summary="更新客户信息")
async def update_client(data:Client):
    db = ClientDatabase()
    db.update_client(data.client_id, data.dict())
    return {"code": 200}
class ClientId(BaseModel):
    id: str
@businessController.post("/delete_clients", summary="删除客户")
async def delete_client(client_id:ClientId):
    db = ClientDatabase()
    db.delete_client(client_id.id)
    return {"code": 200}