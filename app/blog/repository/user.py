from sqlalchemy.orm import Session
from blog import schemas,models
from blog import hashing
from fastapi import HTTPException,status


def create(db: Session,request: schemas.User):
    new_user = models.User(id = request.id,name= request.name,email=request.email,password = hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show_user(id: int,db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail=f'User with {id} not found')
    else:
        return user
