import os
import db_store as db
import store

if os.path.exists("data.sqlite"):
    os.remove("data.sqlite")

d = db.db_store()
d.load_db()

