#Step 1 - Packages to Install
#pip install fastapi
#pip install uvicorn

#Option - Run from Terminal
#uvicorn Example1:app --reload
  
#Run from Spyder / Example Code  
from fastapi import FastAPI
import uvicorn
from fastapi import Form, Request
app = FastAPI(debug=True)

#http://localhost:8002/api1/raj
@app.get('/api1/{searchparam1}')
def api1(searchparam1: str):
    paramname = searchparam1
    print(paramname)
    return str(paramname)

#http://localhost:8002/api2/?searchparam1=ABC&searchparam2=100
@app.get('/api2/')
def api2(searchparam1: str,searchparam2: int):
    param1 = searchparam1
    param2 = str(searchparam2)
    print(str(param1  +','+ param2))
    return str(param1 +','+ param2)

if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8002)
