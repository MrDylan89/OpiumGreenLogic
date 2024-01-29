import db_lib as db
from os.path import join

def init_db():
    """Crea il database"""
    conn = db.connect_db()

    with open(join("database", "autenticazione.sql"), encoding="utf-8") as f:
        conn.executescript(f.read())

    conn.commit()
    conn.close()

    print("Database created successfully!")



if __name__ == "__main__":
    init_db()