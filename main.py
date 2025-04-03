from fastapi import FastAPI, Body

from Routers import category_router
app=FastAPI()

app.include_router(category_router.router)





