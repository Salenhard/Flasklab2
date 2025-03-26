import csv
from config import db
from models import Country, City, Make, Model, Vehicle

def load_countries_from_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        unique_countries = set(row['County'] for row in reader if row['County'])
        for country_name in unique_countries:
            if not Country.query.filter_by(name=country_name).first():
                country = Country(name=country_name)
                db.session.add(country)
        db.session.commit()
        print(f"Loaded {len(unique_countries)} countries")

def load_cities_from_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        city_country_pairs = set((row['City'], row['County']) for row in reader if row['City'] and row['County'])
        for city_name, country_name in city_country_pairs:
            country = Country.query.filter_by(name=country_name).first()
            if country and not City.query.filter_by(name=city_name, country_id=country.id).first():
                city = City(name=city_name, country_id=country.id)
                db.session.add(city)
        db.session.commit()
        print(f"Loaded {len(city_country_pairs)} cities")

def load_makes_from_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        unique_makes = set(row['Make'] for row in reader if row['Make'])
        for make_name in unique_makes:
            if not Make.query.filter_by(name=make_name).first():
                make = Make(name=make_name)
                db.session.add(make)
        db.session.commit()
        print(f"Loaded {len(unique_makes)} makes")

def load_models_from_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        model_make_pairs = set((row['Model'], row['Make']) for row in reader if row['Model'] and row['Make'])
        for model_name, make_name in model_make_pairs:
            make = Make.query.filter_by(name=make_name).first()
            if make and not Model.query.filter_by(name=model_name, make_id=make.id).first():
                model = Model(name=model_name, make_id=make.id)
                db.session.add(model)
        db.session.commit()
        print(f"Loaded {len(model_make_pairs)} models")

def load_vehicles_from_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            vin = row['VIN (1-10)']
            if not vin:
                continue
            # Проверяем, существует ли уже такой VIN
            if Vehicle.query.get(vin):
                print(f"Skipping duplicate VIN: {vin}")
                continue
            country = Country.query.filter_by(name=row['County']).first()
            city = City.query.filter_by(name=row['City'], country_id=country.id).first() if country else None
            make = Make.query.filter_by(name=row['Make']).first()
            model = Model.query.filter_by(name=row['Model'], make_id=make.id).first() if make else None
            if city and model:
                vehicle = Vehicle(
                    id=vin,
                    model_id=model.id,
                    city_id=city.id,
                    model_year=int(row['Model Year']),
                    electric_range=int(row['Electric Range']) if row['Electric Range'] else None
                )
                db.session.add(vehicle)
            else:
                print(f"Skipping VIN {vin}: City or Model not found")
        db.session.commit()
        print("Loaded vehicles")

# Пример использования
if __name__ == "__main__":
    from app import app
    with app.app_context():
        db.drop_all()
        db.create_all()
        file_path = './data/vehicles.csv'  # Укажите путь к вашему CSV
        load_countries_from_csv(file_path)
        load_cities_from_csv(file_path)
        load_makes_from_csv(file_path)
        load_models_from_csv(file_path)
        load_vehicles_from_csv(file_path)