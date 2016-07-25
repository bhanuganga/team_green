from flask import Flask, render_template, redirect, url_for, request
from manager import *
from event import *

app = Flask(__name__)
manager_instance = Manager()

@app.route('/read')
def read():
    a = request.args['list_of_event_ids']
    list_of_event_ids = a.split(',')
    storage = {}
    if a != '':
        for id in list_of_event_ids:
            x = manager_instance.read_event_by_id(id)
            if x==id:
                return 'id {} does not exist'.format(id)
            else:
                storage.update({id: x.__dict__})

    return render_template('search_result.html', storage=storage)


@app.route('/reader')
def reader():
    a = request.args['list_of_event_ids']
    b = a.split('.')
    storage = {}

    if b[0] != '':
        list_of_event_ids = b[0].split(',')
        for id in list_of_event_ids:
            x = manager_instance.read_event_by_id(id)
            storage.update({id: x.__dict__})

    storage1 = {}
    if b[1]!='':
        list_of_event_ids = b[1].split(',')
        for id in list_of_event_ids:
            x = manager_instance.read_event_by_id(id)
            storage1.update({id: x.__dict__})

    storage2 = {}
    if b[2] != '':
        list_of_event_ids = b[2].split(',')
        for id in list_of_event_ids:
            x = manager_instance.read_event_by_id(id)
            storage2.update({id: x.__dict__})

    return render_template('result.html', storage=storage,storage1=storage1,storage2=storage2)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=["POST"])
def add():
    name = request.form['name']
    date = request.form['date']
    city = request.form['city']
    info = request.form['info']
    event_instance = Event(name, date, city, info)
    message = manager_instance.add_event(event_instance)
    return "Save this id : {}".format(message)

@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        id=request.form['event_id']
        return redirect(url_for('read', list_of_event_ids=id))


@app.route('/fetch', methods=["POST"])
def fetch():
    e_id = request.form['event id']
    event_instance = manager_instance.read_event_by_id(e_id)
    if event_instance != e_id:
        return render_template('update.html', event=event_instance, id=e_id)
    else:
        return "No such id found!"

@app.route("/update", methods=["POST"])
def update():
    upd_name = request.form["upd_name"]
    upd_date = request.form["upd_date"]
    upd_city = request.form["upd_city"]
    upd_info = request.form["upd_info"]
    eid = request.form["id"]
    temp_dict = {"name":upd_name,"date":upd_date, "city":upd_city, "info":upd_info}
    message = manager_instance.update_event_by_id(eid, temp_dict)
    if message == 1:
        return "Successfully updated"
    else:
        return message


@app.route('/delete', methods=["POST"])
def delete():
    id = request.form["event id"]
    message = manager_instance.delete_event_by_id(id)
    if message == 1:
        return "Successfully deleted"
    else:
        return "id doesn't exist"

@app.route('/by_date', methods=['POST', 'GET'])
def by_date():
    if request.method == 'POST':
        a = manager_instance.list_event_by_date(request.form['date'])
        message = ','.join(a)
        return redirect(url_for('read', list_of_event_ids=message))


@app.route('/by_city', methods=['POST', 'GET'])
def by_city():
    if request.method == 'POST':
        a = manager_instance.list_event_by_city(request.form['city'])
        message = ','.join(a)
        return redirect(url_for('read', list_of_event_ids=message))


@app.route('/by_date_and_city', methods=['POST', 'GET'])
def by_date_and_city():
    if request.method == 'POST':
        a = manager_instance.list_event_by_date_and_city(request.form['date'], request.form['city'])
        message = ','.join(a)
        return redirect(url_for('read', list_of_event_ids=message))


@app.route('/by_daterange', methods=['POST', 'GET'])
def by_daterange():
    if request.method == 'POST':
        a = manager_instance.events_in_date_range(request.form['fromdate'], request.form['todate'])
        message = ','.join(a)
        return redirect(url_for('read', list_of_event_ids=message))


@app.route('/up_and_past', methods=['POST', 'GET'])
def up_and_past():
    if request.method == 'POST':
        a = manager_instance.today_upcoming_and_completed_events()
        message1 = ','.join(a[0])
        message2 = ','.join(a[1])
        message3 = ','.join(a[2])
        b = [message1, message2, message3]
        message = '.'.join(b)
        return redirect(url_for('reader', list_of_event_ids=message))


if __name__ == '__main__':
    app.run()
