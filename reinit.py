from package import db, create_app

## -------------< Cute little function to re-init the database easier >------------- ##
app = create_app()
ctx = app.app_context()
ctx.push()
db.drop_all()
db.create_all()
