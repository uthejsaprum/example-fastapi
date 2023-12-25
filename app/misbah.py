from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

origins=['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

my_data=[{"field_id":10008,"oid":935,"otype":"glossary_term",
  "ts_updated":"2023-11-29T10:44:32.754768Z","value":[{"otype":"attribute","oid":450047},
                                                      {"otype":"attribute","oid":447716},
                                                      {"otype":"attribute","oid":456636},
                                                      {"otype":"attribute","oid":453587},
                                                      {"otype":"attribute","oid":458777},
                                                      {"otype":"attribute","oid":550158},
                                                      {"otype":"attribute","oid":538384},
                                                      {"otype":"attribute","oid":525218},
                                                      {"otype":"attribute","oid":583651},
                                                      {"otype":"attribute","oid":467612}]},
        {"field_id":10008,"oid":940,"otype":"glossary_term",
  "ts_updated":"2023-11-29T10:44:32.754768Z","value":[]},
  {"field_id":10008,"oid":1000,"otype":"glossary_term",
  "ts_updated":"2023-11-29T10:44:32.754768Z","value":[{"otype":"attribute","oid":950047},
                                                      {"otype":"attribute","oid":947716},
                                                      {"otype":"attribute","oid":956636},
                                                      {"otype":"attribute","oid":953587},
                                                      {"otype":"attribute","oid":958777},
                                                      {"otype":"attribute","oid":950158}]}]


my_data=[{"field_id":10008,"oid":1000,"otype":"glossary_term",
  "ts_updated":"2023-11-29T10:44:32.754768Z","value":[{"otype":"attribute","oid":950047},
                                                      {"otype":"attribute","oid":947716}]}]

@app.get("/getposts")
def get_all_posts():
    return my_data
@app.get("/")
def smaplefunc():
    return {"message":"helloworld hihihi"}