from fastapi import FastAPI, HTTPException, Query
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

conn_params = {
    "host": "rj.rdmapps.com.br",
    "port": 5432,
    "database": "prod",
    "user": "readonly_views",
    "password": "sepia_9Camisole_Region0_circa8_spasm5_vision8_1swain_Hankering_germicide2_blows0_Yiddish_Shake"
}

@app.get("/machines")
def listar_machines():
    try:
        conn = psycopg2.connect(**conn_params)
        cur = conn.cursor(cursor_factory=RealDictCursor)

        cur.execute("""
            SELECT *
            FROM public.machines
            ORDER BY created_at DESC
        """)

        dados = cur.fetchall()

        cur.close()
        conn.close()

        return dados

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    