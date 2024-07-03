import pymongo

with open('./data/mongo_url.txt', 'r') as url:    
    mongo_url = url.read().strip()

def get_mongo_client(mongo_uri):
    """Establish connection to the MongoDB."""
    try:
        client = pymongo.MongoClient(mongo_uri)
        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")

            return client
        except Exception as e:
            print(e)
    except pymongo.errors.ConnectionFailure as e:
        print(f"Connection failed: {e}")
        return None

def load(database, collection):
    mongo_uri = mongo_url
    if not mongo_uri:
        print("MONGO_URI not set in environment variables")

    mongo_client = get_mongo_client(mongo_uri)

    # Ingest data into MongoDB
    db = mongo_client[database]
    col = db[collection]

    return col

def get_data(database, collection):
    mongo_uri = mongo_url
    if not mongo_uri:
        print("MONGO_URI not set in environment variables")

    mongo_client = get_mongo_client(mongo_uri)

    # Ingest data into MongoDB
    db = mongo_client[database]
    col = db[collection]

    return db