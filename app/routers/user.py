from .. import schemas,utils,models,database
from fastapi import FastAPI,Response,HTTPException,status,Depends,APIRouter
from sqlalchemy.orm import Session
from ..database import get_db

router=APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.post("/",response_model=schemas.UserOut)
def adduser(newuser:schemas.UserCreate,db: Session = Depends(get_db)):
    hashed_password=utils.hash(newuser.password)
    newuser.password=hashed_password
    new_user=models.User(**newuser.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}",response_model=schemas.UserOut)
def getuser(id:int,db: Session = Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if user==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id={id} not available")
    return user