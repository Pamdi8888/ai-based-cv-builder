from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from .llm.query import enhance_text

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        raw_data = request.form
        # name = request.form.get('name')
        if len(raw_data['name']) * len(raw_data['email']) * len(raw_data['organization']) > 0:
            print(raw_data)
            data = {
                'name': raw_data['name'],
                'email': raw_data['email'],
                'organizations': raw_data['organization']
            }
            return render_template('temp1.html', **data)
            # return render_template('home.html')
        else:
            flash('Any field cannot be blank', category='error')
    return render_template('home.html')


@views.route('/enhance', methods=['POST'])
def enhance():
    data = request.get_json()
    prompt = data['prompt']
    enhanced_text = enhance_text(prompt)
    return jsonify({'enhanced_text': enhanced_text})
