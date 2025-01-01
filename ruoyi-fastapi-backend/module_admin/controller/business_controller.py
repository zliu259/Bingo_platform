from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi import APIRouter, File, UploadFile, HTTPException
from module_admin.cloudflare_db.controller import ProjectDatabase


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



