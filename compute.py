import fastapi
import uvicorn

app = fastapi.FastAPI()


@app.get("/")
def root():
    return {"status": "working"}



@app.get("/compute/{values}")
def getComputing(values):
    try:
        liczby = values.split('_')
        liczbaA = float(liczby[0])
        liczbaB = float(liczby[1])
        return{
            "input" : [liczbaA,liczbaB],
            "sum": liczbaA+liczbaB,
            "diff": liczbaA-liczbaB,
            "multiply":liczbaA*liczbaB,
        }

    except KeyError:
        raise fastapi.HTTPException(
            status_code = 404,
            detail=f"{values} cos nie idzie"
        )



if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=2000, log_level="info")
