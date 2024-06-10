from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from query import enhance_text

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.form
        # name = request.form.get('name')
        if len(data['name'])*len(data['email'])*len(data['organization']) > 0:
            print(data)
            return data
        else:
            flash('Any field cannot be blank', category='error')
    return render_template('home.html')

@views.route('/enhance', methods=['POST'])
def enhance():
    
    data = request.get_json()
    prompt = data['prompt']
    enhanced_text = enhance_text(prompt)
    return jsonify({'enhanced_text': enhanced_text})