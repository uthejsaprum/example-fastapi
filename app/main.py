
from fastapi import FastAPI
from .database import engine
from . import models
from .routers import post,user,auth,vote
from .config import settings

models.Base.metadata.create_all(bind=engine)

app=FastAPI()


app.include_router(user.router)
app.include_router(post.router)
app.include_router(auth.router)
app.include_router(vote.router)



# from random import randrange
# from typing import Optional,List
# from fastapi import Body, FastAPI,Response,status,HTTPException,Depends
# from pydantic import BaseModel
# from sqlalchemy.orm import Session
# from .database import engine,get_db
# from . import models,schemas,utils
# from .routers import post,user,auth



# @app.get("/sqlalch/")
# def testalch(db: Session = Depends(get_db)):
#     post=db.query(models.Post).all()
#     return {"message":post}

# @app.get("/posts/",response_model=List[schemas.ResponseBody])
# def get_posts(db: Session = Depends(get_db)):
#     post=db.query(models.Post).all()
#     # cursor.execute(f"""select id,title,content from poshhts""")
#     # posts=cursor.fetchall()
#     print(post)
#     return post


# @app.post("/posts",response_model=schemas.ResponseBody)
# def addpost(post:schemas.Post,db: Session = Depends(get_db)):
#     #     cursor.execute("""insert into poshhts(title,content) values(%s,%s) returning * """,
#     #                    (post.title,post.content))
#     #     conn.commit()
#     #     new_post=cursor.fetchone()
#     new_post=models.Post(**post.model_dump())       #unwrapping the dictionary
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)
#     return new_post


# @app.get("/posts/{id}",response_model=schemas.ResponseBody)
# def getapost(id:int,db: Session = Depends(get_db)):

#     # cursor.execute("""select * from posts where id=%s""",(str(id)))  #not working as expected
#     # cursor.execute(f"""select * from posts where id={id}""")
#     post=db.query(models.Post).filter(models.Post.id == id).first()
#     # post=cursor.fetchone()
#     # print(post)
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f'post with id = {id} not available')
#     return post



# @app.delete("/posts/{id}",response_model=schemas.ResponseBody)
# def getapost(id:int,db: Session = Depends(get_db)):
#     post=db.query(models.Post).filter(models.Post.id == id)
#     # cursor.execute(f"""delete from posts where id={id} returning * """)
#     # post=cursor.fetchone()
#     # conn.commit()
#     if post.first() == None :
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f'post with id = {id} not available')
#     post.delete(synchronize_session=False)
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)



# @app.put("/posts/{id}",response_model=schemas.ResponseBody)
# def updatepost(id:int,updatedpost:schemas.Post,db: Session = Depends(get_db)):
#     # cursor.execute("""update posts set title=%s,content=%s where id=%s returning * """,(post.title,post.content,str(id)))
#     # updated_post=cursor.fetchone()
#     # conn.commit()
#     # print(updated_post)

#     post_query=db.query(models.Post).filter(models.Post.id==id)
#     post=post_query.first()

#     if post==None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id={id} not available")
    
#     post_query.update(updatedpost.dict(),synchronize_session=False)
#     db.commit()
#     return post_query.first()


# @app.post("/users/",response_model=schemas.UserOut)
# def adduser(newuser:schemas.UserCreate,db: Session = Depends(get_db)):
#     hashed_password=utils.hash(newuser.password)
#     newuser.password=hashed_password
#     new_user=models.User(**newuser.model_dump())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user


# @app.get("/users/{id}",response_model=schemas.UserOut)
# def getuser(id:int,db: Session = Depends(get_db)):
#     user=db.query(models.User).filter(models.User.id==id).first()
#     if user==None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"user with id={id} not available")
#     return user















# @app.post("/posts/")
# def send_post(post:Post):
#     cursor.execute("""insert into poshhts(title,content) values(%s,%s) returning * """,
#                    (post.title,post.content))
#     conn.commit()
#     new_post=cursor.fetchone()
#     return {"data":new_post}


# @app.get("/posts/{id}")
# def getapost(id:int):
#     # cursor.execute("""select * from posts where id=%s""",(str(id)))  #not working as expected
#     cursor.execute(f"""select * from posts where id={id}""")

#     post=cursor.fetchone()
#     print(post)
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f'post with id = {id} not available')
#     return {"data":post}



# @app.delete("/posts/{id}")
# def delpost(id:int):
#     cursor.execute(f"""delete from posts where id={id} returning * """)
#     post=cursor.fetchone()
#     conn.commit()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id={id} not available")
#     return {"data":"post with id={id} deleted successfully"}


# @app.put("/posts/{id}")
# def updatepost(id:int,post:Post):
#     cursor.execute("""update posts set title=%s,content=%s where id=%s returning * """,(post.title,post.content,str(id)))
#     updated_post=cursor.fetchone()
#     conn.commit()
#     print(updated_post)
#     if not updated_post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id={id} not available")
#     return {"data":updated_post}



# @app.get("/posts/")
# def get_posts():
#     cursor.execute(f"""select id,title,content from poshhts""")
#     posts=cursor.fetchall()
#     print(posts)
#     return {"data":posts}


# @app.post("/posts/")
# def send_post(post:Post):
#     cursor.execute("""insert into poshhts(title,content) values(%s,%s) returning * """,
#                    (post.title,post.content))
#     conn.commit()
#     new_post=cursor.fetchone()
#     return {"data":new_post}


# @app.get("/posts/{id}")
# def getapost(id:int):
#     # cursor.execute("""select * from posts where id=%s""",(str(id)))  #not working as expected
#     cursor.execute(f"""select * from posts where id={id}""")

#     post=cursor.fetchone()
#     print(post)
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f'post with id = {id} not available')
#     return {"data":post}



# @app.delete("/posts/{id}")
# def delpost(id:int):
#     cursor.execute(f"""delete from posts where id={id} returning * """)
#     post=cursor.fetchone()
#     conn.commit()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id={id} not available")
#     return {"data":"post with id={id} deleted successfully"}


# @app.put("/posts/{id}")
# def updatepost(id:int,post:Post):
#     cursor.execute("""update posts set title=%s,content=%s where id=%s returning * """,(post.title,post.content,str(id)))
#     updated_post=cursor.fetchone()
#     conn.commit()
#     print(updated_post)
#     if not updated_post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id={id} not available")
#     return {"data":updated_post}

# my_posts=[{"title":"ap","content":"andhra pradesh","published":True,"rating":4,"id":1},
#        {"title":"tg","content":"telangana","published":False,"id":2},
#        {"title":"tn","content":"tamilnadu","rating":4,"id":3},
#        {"title":"gv","content":"goa","id":4},
#        {"title":"mh","content":"maharastra","published":True,"rating":3,"id":5}]

# my_data=[{"field_id":10008,"oid":935,"otype":"glossary_term",
#   "ts_updated":"2023-11-29T10:44:32.754768Z","value":[{"otype":"attribute","oid":450047},
#                                                       {"otype":"attribute","oid":447716},
#                                                       {"otype":"attribute","oid":456636},
#                                                       {"otype":"attribute","oid":453587},
#                                                       {"otype":"attribute","oid":458777},
#                                                       {"otype":"attribute","oid":550158},
#                                                       {"otype":"attribute","oid":538384},
#                                                       {"otype":"attribute","oid":525218},
#                                                       {"otype":"attribute","oid":583651},
#                                                       {"otype":"attribute","oid":467612}]},
#         {"field_id":10008,"oid":940,"otype":"glossary_term",
#   "ts_updated":"2023-11-29T10:44:32.754768Z","value":[]}]

# def find_id(id):
#     for p in my_posts:
#         if p['id']==id:
#             return p
        
# def del_post(id):
#     for i,p in enumerate(my_posts):
#         if p['id'] == id:
#             result=my_posts.pop(i)
#             return result
        
# def find_index(id):
#     for i,p in enumerate(my_posts):
#         if p['id']==id:
#             return i

# @app.get("/posts")
# def get_posts():
#     return {"data":my_posts}

# @app.get("/posts/latest")          #to get latest post
# def get_latest_posts():
#     post=my_posts[-1]
#     return {"data":post}

# @app.get("/posts/{id}")
# def get_posts(id:int):
#     post=find_id(id)
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id={id} is not available")
#         # response.status_code=status.HTTP_404_NOT_FOUND
#         # return {"mesage" : f"post with id={id} is not available"}
#     return {"data":post}




# @app.post("/posts",status_code=status.HTTP_201_CREATED)
# def postrequest(post:Post):
#     new_post=post.model_dump()
#     new_post['id']=randrange(1,10000000000)
#     my_posts.append(new_post)
#     return {"message":new_post}


# # @app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
# # def delete_post(id:int):
# #     d_post=del_post(id)
# #     return Response(status_code=status.HTTP_204_NO_CONTENT)



# @app.delete("/posts/{id}")
# def delete_post(id:int):
#     d_post=del_post(id)
#     if not d_post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id={id} not available")
#     return {"message":"post with id={id} successfully deleted"}




# @app.put("/posts/{id}")
# def update_post(id:int,post:Post):
#     updated_post=post.model_dump()
#     ind=find_index(id)
#     print(ind)
#     if ind==None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id={id} not available")
#     updated_post['id']=id
#     my_posts[ind]=updated_post
#     return {"message":updated_post}



# @app.put("/posts/{id}")
# def update_post(id:int,post:Post):
#     updated_post=post.model_dump()
#     ind=find_index(id)
#     updated_post['id']=id
#     my_posts[ind]=updated_post
#     return {"message":updated_post}



# @app.get("/misbah/posts/")
# def get_posts():
#     return my_data