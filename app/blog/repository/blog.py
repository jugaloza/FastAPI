
from sqlalchemy.orm import Session
from blog import models,schemas
from fastapi import HTTPException,status




def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create_blog(request: schemas.Blog,db: Session,creator_id=1):
    new_blog = models.Blog(title=request.title,body=request.body,creator_id=creator_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def show_blog(id: int,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail=f'Blog with Id {id} is not available')
    else:
        return blog

def delete_blog(id: int,db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if blog:
        db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)

        db.commit()
        return 'done'
    else:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail=f'Blog with Id {id} is not available')

def update_blog(id: int,db: Session,request: schemas.Blog):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog:
        db.query(models.Blog).filter(models.Blog.id == id).update({models.Blog.title : request.title},synchronize_session=False)
        db.commit()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with {id} not found')
    return 'done'
