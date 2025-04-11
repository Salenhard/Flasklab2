from app import app
from structures.models import *
from flask import render_template


@app.route('/')
def index():
    [vehicles_head, vehicles_body] = get_all_vehicles()
    html = render_template(
        'index.html',
        vehicles_head=vehicles_head,
        vehicles_body=vehicles_body
    )
    return html


@app.route('/year-range')
def year_range():
    [vehicles_head, vehicles_body] = get_vehicle_by_year_range(2000, 2007)
    html = render_template(
        'index.html',
        vehicles_head=vehicles_head,
        vehicles_body=vehicles_body
    )
    return html


@app.route('/model')
def model():
    [vehicles_head, vehicles_body] = get_vehicle_electric_range_by_model()
    html = render_template(
        'index.html',
        vehicles_head=vehicles_head,
        vehicles_body=vehicles_body
    )
    return html


@app.route('/make')
def make():
    [vehicles_head, vehicles_body] = get_vehicle_electric_range_by_make()
    html = render_template(
        'index.html',
        vehicles_head=vehicles_head,
        vehicles_body=vehicles_body
    )
    return html


@app.route('/city')
def city():
    [vehicles_head, vehicles_body] = get_vehicle_by_city()
    html = render_template(
        'index.html',
        vehicles_head=vehicles_head,
        vehicles_body=vehicles_body
    )
    return html


@app.route('/test')
def test():
    [vehicles_head, vehicles_body] = get_vehicle_electric_range_by_popular_model()
    html = render_template(
    'index.html',
    vehicles_head = vehicles_head,
    vehicles_body = vehicles_body
    )
    return html


@app.route('/country')
def country():
    [vehicles_head, vehicles_body] = get_vehicle_by_country()
    html = render_template(
        'index.html',
        vehicles_head=vehicles_head,
        vehicles_body=vehicles_body
    )
    return html
