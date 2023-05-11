import shutil

from fastapi import APIRouter, UploadFile

from app.tasks.tasks import hadler_pic

router = APIRouter(
    prefix='/images',
    tags=['Загрузка картинок']
)

@router.post('/hotels')
async def add_hotel_image(name:int, file: UploadFile):
    path = f'app/static/images/{name}.webp'
    with open(path , 'wb+') as image:
        shutil.copyfileobj(file.file, image)
    hadler_pic.delay(path)