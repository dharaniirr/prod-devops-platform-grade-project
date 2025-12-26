from app.db import get_db_connection

def health_check():
    try:
        conn = get_db_connection()
        conn.close()
        return {"status": "ok", "database": "reachable"}
    except Exception:
        return {"status": "error", "database": "unreachable"}

