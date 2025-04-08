from pymilvus import Collection, MilvusException, connections, db, utility


class MilvusDB:
    def __init__(self, db_name):
        conn = connections.connect(host="127.0.0.1", port=19530)
        try:
            existing_databases = db.list_database()
            if db_name in existing_databases:
                print(f"Database '{db_name}' already exists.")
                # Use the database context
                db.using_database(db_name)
            else:
                print(f"Database '{db_name}' does not exist.")
                db.create_database(db_name)
                print(f"Database '{db_name}' created successfully.")
        except MilvusException as e:
            print(f"An error occurred: {e}")
