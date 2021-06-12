from deta import Deta
import core.config as config

# add your Project Key
deta = Deta(config.DETA_KEY)
# DB
db_users = deta.Base("users")
db_results = deta.Base("results")
db_products = deta.Base("products")
