from flask import Flask, request, jsonify,render_template

app = Flask(__name__,template_folder="templates")

# Dummy database (SQLite for simplicity)
doctors = [
    {
        "id": 1,
        "name": "Dr. John Doe",
        "specialty": "Cardiologist",
        "available_days": ["Monday", "Wednesday", "Friday"],
        "max_patients_per_day": 10
    },
    {
        "id": 2,
        "name": "Dr. Jane Smith",
        "specialty": "Dermatologist",
        "available_days": ["Tuesday", "Thursday", "Saturday"],
        "max_patients_per_day": 12
    },
    {
        "id": 3,
        "name": "Dr. David Brown",
        "specialty": "Cardiologist",
        "available_days": ["Monday", "Tuesday", "Wednesday"],
        "max_patients_per_day": 8
    },
    {
        "id": 4,
        "name": "Dr. Emily White",
        "specialty": "Neurologist",
        "available_days": ["Thursday", "Friday", "Saturday"],
        "max_patients_per_day": 9
    },
    {
        "id": 5,
        "name": "Dr. Michael Johnson",
        "specialty": "General Surgeon",
        "available_days": ["Monday", "Wednesday", "Friday"],
        "max_patients_per_day": 12
    },
    {
        "id": 6,
        "name": "Dr. Sarah Lee",
        "specialty": "Pediatrician",
        "available_days": ["Tuesday", "Thursday", "Saturday"],
        "max_patients_per_day": 10
    },
    {
        "id": 7,
        "name": "Dr. Robert Clark",
        "specialty": "Orthopedic Surgeon",
        "available_days": ["Monday", "Wednesday", "Friday"],
        "max_patients_per_day": 11
    },
    {
        "id": 8,
        "name": "Dr. Lisa Adams",
        "specialty": "Gynecologist",
        "available_days": ["Tuesday", "Thursday", "Saturday"],
        "max_patients_per_day": 10
    },
    {
        "id": 9,
        "name": "Dr. William Taylor",
        "specialty": "Oncologist",
        "available_days": ["Monday", "Wednesday", "Friday"],
        "max_patients_per_day": 7
    },
    {
        "id": 10,
        "name": "Dr. Maria Garcia",
        "specialty": "Psychiatrist",
        "available_days": ["Tuesday", "Thursday", "Saturday"],
        "max_patients_per_day": 8
    }
]



@app.route('/')
def home():  
    return render_template('home.html')

@app.route('/appointment_page')
def appointment_page():  
    return render_template('appointment_page.html')

@app.route('/API')
def api():  
    return render_template('API.html')

@app.route('/doctors', methods=['GET'])
def get_doctors():
    return jsonify(doctors)


@app.route('/doctors/<int:doctor_id>', methods=['GET'])
def get_doctor(doctor_id):
    doctor = next((d for d in doctors if d["id"] == doctor_id), None)
    if doctor:
        return jsonify(doctor)
    return jsonify({"error": "Doctor not found"}), 404

@app.route('/doctors/<string:specialty>', methods=['GET'])
def get_specilty(specialty):
    doc_specialty=[]
    for doc in doctors:
        if doc["specialty"]==specialty:
            doc_specialty.append(doc)
    if doc_specialty:
        return jsonify(doc_specialty)
    return jsonify({"error": "Specialty not found"}), 404


@app.route('/appointment',methods=["POST","GET"])
def appointment():
    doc_list=[]
    data=request.form
    # Patient_name=data["Patient_name"]
    Appointment_day=data['days']
    specialty=data['Speciality']

    for doc in doctors:
        if (Appointment_day in doc["available_days"]) and doc["specialty"]==specialty and doc["max_patients_per_day"]>=0:
            doc["max_patients_per_day"]=doc["max_patients_per_day"]-1
            doc_list.append(doc)
            print(doc_list)


    if doc_list:
        return jsonify(doc_list)

    return jsonify({"error": "Doctor not found"}), 404
    
    

if __name__ == '__main__':
    app.run(debug=True)
