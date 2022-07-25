from fastapi import FastAPI
from blog import models
from blog.database import engine
from blog.routers import blog,users,authentication


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(blog.router)
app.include_router(users.router)
app.include_router(authentication.router)

