from flask import Flask, render_template, request, flash
from forms import PlaneForm
import calendar
import fctplanes as fp

app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/plane', methods = ['GET', 'POST'])
def plane():
    form = PlaneForm()
    
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('plane.html', form = form)
        else:
            carrier = form.Carrier.data
            day = int(form.day.data)
            month = int(form.month.data)
            year = int(form.year.data)
            distance = int(form.distance.data)
            hour_dep = int(form.hour_dep.data)
            min_dep = int(form.min_dep.data)
            hour_arr = int(form.hour_arr.data)
            min_arr = int(form.min_arr.data)
            city = str(dict(form.City.choices).get(form.City.data))
            # Conversion heure de départ en minutes
            time_dep = 60*hour_dep + min_dep
            # Conversion heure de d'arrivée en minutes
            time_arr = 60*hour_arr + min_arr
            # jour de la semaine
            #day_week = 0
            if fp.validate_date(year, month, day) == True:
                day_week = calendar.weekday(year, month, day) + 1
            else:
                form.day.data = ''
                return render_template('plane.html', form = form)
            # Nombre de vols dans l'année par aéroport
            nb_flight = int(form.City.data)
            #if month == 2:
            #    form.City.data = str(city)
            #    form.min_arr.data = str(day_week)
            #    return render_template('success.html', form = form)
            #else:
            #    return render_template('plane.html', form = form)
            if day_week != 0:
                delay_arr = fp.plane_prediction(carrier, month, day_week, distance, time_dep, time_arr, nb_flight)
                form.City.data = str(city)
                form.year.data = str(day).zfill(2) + '-' + str(month).zfill(2) + '-' + str(year)
                form.hour_dep.data = str(hour_dep).zfill(2) + 'h' + str(min_dep).zfill(2)
                form.hour_arr.data = str(hour_arr).zfill(2) + 'h' + str(min_arr).zfill(2)
                form.min_arr.data = str(delay_arr)
                return render_template('success.html', form = form)
            else:
                return render_template('plane.html', form = form)
    elif request.method == 'GET':
        return render_template('plane.html', form = form)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404		
		
if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, port = 8080)