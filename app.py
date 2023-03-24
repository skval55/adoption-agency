from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Animal

from forms import AddAnimalForm
from forms import EditAnimalForm



app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adoption_agency"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def homepage():
    """home page"""

    animals = Animal.query.all()

    return render_template("home.html", animals=animals)

@app.route('/add', methods=['GET', 'POST'])
def add_animal():
    """add animal for and post animal"""

    form = AddAnimalForm()
    for x in form:

        print(x.type)
    print("*****************")

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        if photo_url == "":
            photo_url = 'https://i.pinimg.com/originals/8c/0c/ea/8c0ceac06ec6bf6e3b7065e4346f30a1.gif'
        age = form.age.data
        notes = form.notes.data
        db.session.add(Animal(name=name, species=species, photo_url=photo_url, age=age, notes=notes))
        db.session.commit()

        return redirect('/')
    else:
        return render_template("add-animal.html", form=form)


@app.route('/<int:animal_id>', methods=['GET', 'POST'])
def animal_page(animal_id):
    """shows animals detail and gives option to edit"""

    animal = Animal.query.get_or_404(animal_id)
    form = EditAnimalForm(obj = animal)

    if form.validate_on_submit():
        animal.photo_url = form.photo_url.data
        if animal.photo_url == "":
            animal.photo_url = 'https://i.pinimg.com/originals/8c/0c/ea/8c0ceac06ec6bf6e3b7065e4346f30a1.gif'
        animal.notes = form.notes.data
        animal.available = form.available.data
        db.session.commit()
        return redirect(f'/{animal.id}')
    else:
        return render_template('animal-page.html', animal = animal, form=form)