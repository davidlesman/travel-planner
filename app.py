from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class TravelPlan:
    def __init__(self):
        self.flights = []
        self.hotels = []
        self.activities = []
        self.taxis = []
        self.contacts = []
        self.extras = []

    def add_flight(self, flight_info):
        self.flights.append(flight_info)

    def add_hotel(self, hotel_info):
        self.hotels.append(hotel_info)

    def add_activity(self, activity_info):
        self.activities.append(activity_info)

    def add_taxi(self, taxi_info):
        self.taxis.append(taxi_info)

    def add_contact(self, contact_info):
        self.contacts.append(contact_info)

    def add_extra(self, extra_info):
        self.extras.append(extra_info)

    def delete_item(self, section, index):
        if section == 'flight' and index < len(self.flights):
            self.flights.pop(index)
        elif section == 'hotel' and index < len(self.hotels):
            self.hotels.pop(index)
        elif section == 'activity' and index < len(self.activities):
            self.activities.pop(index)
        elif section == 'taxi' and index < len(self.taxis):
            self.taxis.pop(index)
        elif section == 'contact' and index < len(self.contacts):
            self.contacts.pop(index)
        elif section == 'extra' and index < len(self.extras):
            self.extras.pop(index)

    def get_plan(self):
        return {
            "flights": self.flights,
            "hotels": self.hotels,
            "activities": self.activities,
            "taxis": self.taxis,
            "contacts": self.contacts,
            "extras": self.extras
        }

travel_plan = TravelPlan()

@app.route('/')
def home():
    return render_template('home.html', plan=travel_plan.get_plan())

@app.route('/add', methods=['POST'])
def add():
    section = request.form['section']
    info = request.form['info']
    if section == 'flight':
        travel_plan.add_flight(info)
    elif section == 'hotel':
        travel_plan.add_hotel(info)
    elif section == 'activity':
        travel_plan.add_activity(info)
    elif section == 'taxi':
        travel_plan.add_taxi(info)
    elif section == 'contact':
        travel_plan.add_contact(info)
    elif section == 'extra':
        travel_plan.add_extra(info)
    return redirect(url_for('home'))

@app.route('/delete/<section>/<int:index>', methods=['POST'])
def delete(section, index):
    travel_plan.delete_item(section, index)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
