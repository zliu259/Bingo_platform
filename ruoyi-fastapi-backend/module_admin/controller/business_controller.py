from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import HTMLResponse
from fastapi import APIRouter, File, UploadFile, HTTPException
from module_admin.cloudflare.controller import ProjectDatabase, ClientDatabase, CfDatabase
from pydantic import BaseModel


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

#Client
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

class ClientId(BaseModel):
    id: str

@businessController.get("/clients", summary="获取完整客户列表")
async def get_all_clients():
    db = ClientDatabase()
    clients = db.list_all_clients()
    print(clients)
    return clients

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

@businessController.post("/delete_clients", summary="删除客户")
async def delete_client(client_id:ClientId):
    db = ClientDatabase()
    db.delete_client(client_id.id)
    return {"code": 200}

#Provider
class Provider(BaseModel):
    id: str
    name: str
    abn: str
    address: str
    contact: str
    bank: str
    bsb: str
    account: str

@businessController.get("/providers", summary="获取完整供应商列表")
async def get_all_providers():
    db = CfDatabase()
    providers = db.list_all_providers()
    print(providers)
    return providers

@businessController.post("/add_providers", summary="添加新供应商")
async def add_provider(data:Provider):
    db = CfDatabase()
    db.insert_provider([data.dict()])
    return {"code": 200, "message": "Provider added successfully"}

#Quotation
class Quotation(BaseModel):
    id: str
    client_name: str
    client_contact: str
    client_details: str
    client_id: str
    provider_id: str
    date: str
    type: str
    status: int
    load: int
    statistics: str
    price: str
    gst: str
    total_price: str
    created_by: str

@businessController.get("/quotations", summary="获取完整报价单列表")
async def get_all_quotations():
    db = CfDatabase()
    quotations = db.list_all_quotations()
    print(quotations)
    return quotations

@businessController.post("/add_quotations", summary="添加新报价单")
async def add_quotation(data:Quotation):
    db = CfDatabase()
    db.insert_quotation([data.dict()])
    return {"code": 200, "message": "Quotation added successfully"}