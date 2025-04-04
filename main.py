from fastapi import FastAPI, Body

from Routers import category_router,product_router
app=FastAPI()



app.include_router(category_router.router)
app.include_router(product_router.router)




