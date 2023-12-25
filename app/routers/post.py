from .. import schemas,utils,models,database,oauth2
from typing import List,Optional
from fastapi import FastAPI,Response,HTTPException,status,Depends,APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import get_db

router=APIRouter(
    prefix="/posts",
    tags=['Posts']
)


@router.get("/",response_model=List[schemas.ResponseBodyTwo])
def get_posts(db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user),
              search:Optional[str]="",limit:int=10,skip:int=0):
#     database.cursor.execute(f"""SELECT posts.id AS posts_id, posts.title AS posts_title, posts.content AS posts_content, posts.published AS posts_published, posts.created_at AS posts_created_at, posts.owner_id AS posts_owner_id, count(votes.post_id) AS votes
# FROM posts LEFT OUTER JOIN votes ON votes.post_id = posts.id GROUP BY posts.id""")

    # post=db.query(models.Post).filter(models.Post.owner_id==current_user.id).all()
    # post=db.query(models.Post,models.Vote.post_id).filter(models.Post.content.contains(search)).limit(limit).offset(skip).all()
    posts=db.query(models.Post).join(models.Vote,models.Vote.post_id==models.Post.id,
                                      isouter=True).group_by(models.Post.id).filter(models.Post.content.contains(search)).limit(limit).offset(skip).all()
    # print(result)
    # ,func.count(models.Vote.post_id)
    # ,func.count(models.Vote.post_id).label("votes")
    # ,response_model=List[schemas.PostOut]
    # cursor.execute(f"""select id,title,content from poshhts""")
    # posts=database.cursor.fetchall()
    # print(post)
    # print(limit)
    # print(result)




    result = []
    for post in posts:
        total_votes = db.query(models.Vote).filter(models.Vote.post_id == post.id).count()
        # print(total_votes)
        result.append({
            "id": post.id,
            "title": post.title,
            "content": post.content,
            "published":post.published,
            "created_at":post.created_at,
            "votes":total_votes,
            "owner":{
                "email":post.owner.email,
                "id":post.owner.id,
                "created_at":post.owner.created_at
                },
            "owner_id":post.owner_id
        })
    print(result)
    return result





@router.post("/",status_code=status.HTTP_201_CREATED)
def addpost(post:schemas.Post,db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    #     cursor.execute("""insert into poshhts(title,content) values(%s,%s) returning * """,
    #                    (post.title,post.content))
    #     conn.commit()
    #     new_post=cursor.fetchone()
    new_post=models.Post(owner_id=current_user.id,**post.model_dump())     #unwrapping the dictionary     #((OR))new_post.owner_id=current_user.id
    # print(new_post.dict())
    # print(current_user.password)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{id}",response_model=List[schemas.ResponseBody])
def getapost(id:int,db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):

    # cursor.execute("""select * from posts where id=%s""",(str(id)))  #not working as expected
    # cursor.execute(f"""select * from posts where id={id}""")
    # post=db.query(models.Post).filter(models.Post.id == id).first()
    posts=db.query(models.Post).join(models.Vote,models.Vote.post_id==models.Post.id,
                                      isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    # post=cursor.fetchone()
    print(posts)
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id = {id} not available')
    
    # if posts.owner_id!=current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
    #                         detail=f"not authorized to perform requested action")
    result = []
    total_votes = db.query(models.Vote).filter(models.Vote.post_id == posts.id).count()
        # print(total_votes)
    result.append({
        "id": posts.id,
        "title": posts.title,
        "content": posts.content,
        "published":posts.published,
        "created_at":posts.created_at,
        "votes":total_votes,
        "owner":{
            "email":posts.owner.email,
            "id":posts.owner.id,
            "created_at":posts.owner.created_at
            },
        "owner_id":posts.owner_id
            })
    # print(result)
    return result



@router.delete("/{id}",response_model=schemas.ResponseBody)
def getapost(id:int,db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    post_query=db.query(models.Post).filter(models.Post.id == id)
    # cursor.execute(f"""delete from posts where id={id} returning *""")
    # post=cursor.fetchone()
    # conn.commit()
    post=post_query.first()
    # print(post.owner_id)
    if post == None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id = {id} not available')
    if post.owner_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'not authorized to perform requested action')

    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@router.put("/{id}",response_model=schemas.ResponseBody)
def updatepost(id:int,updatedpost:schemas.Post,db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    # cursor.execute("""update posts set title=%s,content=%s where id=%s returning * """,(post.title,post.content,str(id)))
    # updated_post=cursor.fetchone()
    # conn.commit()
    # print(updated_post)

    post_query=db.query(models.Post).filter(models.Post.id==id)
    post=post_query.first()

    if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id={id} not available")
    
    if post.owner_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'not authorized to perform requested action')
    
    post_query.update(updatedpost.dict(),synchronize_session=False)
    db.commit()
    return post_query.first()
