from fastapi import APIRouter
from blog import schemas,database,models
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from blog.hashing import Hash
from blog.token import create_access_token
from fastapi.security import OAuth2PasswordRequestForm
router = APIRouter(tags=['login'])

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Invalid Credentials')

    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Invalid Credentials')

    
    access_token = create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}
    