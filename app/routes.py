from flask import render_template, redirect, jsonify
from app import app, db
from app.models import MarkerRequest
from .forms import SubmitForm
import requests
from config import Config
from urllib.parse import quote


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SubmitForm()
    if form.validate_on_submit():
        formatted_place = quote(form.place.data, safe='')
        api_response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}".format(formatted_place, Config.GMAPS_KEY))
        api_response_dict = api_response.json()

        name = form.name.data
        latitude = str(api_response_dict['results'][0]['geometry']['location']['lat'])
        longitude = str(api_response_dict['results'][0]['geometry']['location']['lng'])
        description = form.description.data
        type=form.type.data

        new_marker = MarkerRequest(name=name, latitude=latitude, longitude=longitude, description=description, type=type)
        db.session.add(new_marker)
        db.session.commit()

        return redirect('/')
    return render_template('index.html', title="SCBC Data Entry", form=form)


@app.route('/api/all-markers', methods=['GET'])
def get_markers():
    markers_list = []
    for marker in MarkerRequest.get_all():
        marker_as_dict = {
            'id': marker.id,
            'title': marker.name,
            'latitude': marker.latitude,
            'longitude': marker.longitude,
            'description': marker.description,
            'type': marker.type
        }
        markers_list.append(marker_as_dict)
    return jsonify({'markers': markers_list})

