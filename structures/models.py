from config import db
from models import Vehicle, Model, Make, City, Country
from sqlalchemy import func

def get_all_vehicles():
    query = (
        db.session.query(
            Vehicle.id.label("VIN"),
            Model.name.label("Модель"),
            Make.name.label("Производитель"),
            City.name.label("Город"),
            Country.name.label("Страна"),
            Vehicle.model_year.label("Год"),
            Vehicle.electric_range.label("Запас хода")
        )
        .select_from(Vehicle)
        .join(Model)
        .join(Make)
        .join(City)
        .join(Country)
    )
    return [query.statement.columns.keys(), query.all()]

def get_vehicle_electric_range_by_model():
    query = (
        db.session.query(
            Model.name.label("Модель"),
            func.max(Vehicle.electric_range).label("Максимальный запас хода"),
            func.min(Vehicle.electric_range).label("Минимальный запас хода"),
            func.avg(Vehicle.electric_range).label("Средний запас хода")
        )
        .select_from(Vehicle)
        .join(Model)
        .group_by(Model.name)
    )
    return [query.statement.columns.keys(), query.all()]

def get_vehicle_electric_range_by_make():
    query = (
        db.session.query(
            Make.name.label("Производитель"),
            func.max(Vehicle.electric_range).label("Максимальный запас хода"),
            func.min(Vehicle.electric_range).label("Минимальный запас хода"),
            func.avg(Vehicle.electric_range).label("Средний запас хода")
        )
        .select_from(Vehicle)
        .join(Model)
        .join(Make)
        .group_by(Make.name)
    )
    return [query.statement.columns.keys(), query.all()]

def get_vehicle_by_year_range(from_year, to_year):
    query = (
        db.session.query(
            Vehicle.id.label("VIN"),
            Model.name.label("Модель"),
            Make.name.label("Производитель"),
            City.name.label("Город"),
            Country.name.label("Страна"),
            Vehicle.model_year.label("Год"),
            Vehicle.electric_range.label("Запас хода")
        )
        .select_from(Vehicle)
        .join(Model)
        .join(Make)
        .join(City)
        .join(Country)
        .filter(Vehicle.model_year.between(from_year, to_year))
    )
    return [query.statement.columns.keys(), query.all()]

def get_vehicle_by_city():
    query = (
        db.session.query(
            City.name.label("Город"),
            func.max(Vehicle.electric_range).label("Максимальный запас хода"),
            func.min(Vehicle.electric_range).label("Минимальный запас хода"),
            func.avg(Vehicle.electric_range).label("Средний запас хода")
        )
        .select_from(Vehicle)
        .join(City)
        .group_by(City.name)
    )
    return [query.statement.columns.keys(), query.all()]

def get_vehicle_by_country():
    query = (
        db.session.query(
            Country.name.label("Страна"),
            func.max(Vehicle.electric_range).label("Максимальный запас хода"),
            func.min(Vehicle.electric_range).label("Минимальный запас хода"),
            func.avg(Vehicle.electric_range).label("Средний запас хода")
        )
        .select_from(Vehicle)
        .join(City)
        .join(Country)
        .group_by(Country.name)
    )
    return [query.statement.columns.keys(), query.all()]