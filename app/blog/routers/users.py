from fastapi import APIRouter,Depends,Response,HTTPException,status
from blog import schemas,models,database
from sqlalchemy.orm import Session
from blog import hashing
from blog.repository import user





router = APIRouter(prefix='/user',tags=['users'])

@router.post('/',response_model=schemas.ShowUser)
def create_user(request: schemas.User,db: Session = Depends(database.get_db)):
    
    return user.create(db,request)
    

@router.get('/{id}',response_model=schemas.ShowUser)
def show_user(id: int,db: Session = Depends(database.get_db)):
    return user.show_user(id,db)
    



