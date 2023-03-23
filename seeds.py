from app import db
from models import Animal

db.drop_all()
db.create_all()

cat = Animal(name="catomode", species="cat", photo_url="https://www.daysoftheyear.com/wp-content/uploads/international-cat-day1-scaled.jpg", age=2, available=True)
cat2 = Animal(name="KaSsebo", species="cat", photo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/3-Colored_Norwegian_Forest_Cat.jpg/1200px-3-Colored_Norwegian_Forest_Cat.jpg", age=1)
db.session.add(cat)
db.session.add(cat2)
db.session.commit()