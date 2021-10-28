from flask_sqlalchemy_minimal import User
result = User.query.all()
print(result)
result = User.query.filter_by(username='admin').first()
print(result)