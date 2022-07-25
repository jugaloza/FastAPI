from fastapi import APIRouter,Depends,status,HTTPException
from blog import schemas,models
from typing import List
from sqlalchemy.orm import Session
from blog.database import get_db
from blog.repository import blog
from blog.oauth2 import get_current_user
router = APIRouter(prefix= '/blog',
                   tags=['Blogs'])


@router.get('/')
def get(db: Session = Depends(get_db),current_user: schemas.User = Depends(get_current_user)):
    return blog.get_all(db)
    

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(blogs: schemas.Blog,db: Session = Depends(get_db),current_user: schemas.User = Depends(get_current_user)):
    return blog.create_blog(blogs,db)




@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog)
def show(id: int,db : Session = Depends(get_db),current_user: schemas.User = Depends(get_current_user)):
    
    return blog.show_blog(id,db)




@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int,db: Session = Depends(get_db),current_user: schemas.User = Depends(get_current_user)):
    return blog.delete_blog(id,db)



@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id: int,request: schemas.Blog,db: Session = Depends(get_db),current_user: schemas.User = Depends(get_current_user)):
    return blog.update_blog(id,db,request)
    


