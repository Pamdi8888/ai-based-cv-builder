from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, json
from .llm.query import enhance_text
from .models import *
from werkzeug.utils import secure_filename
import os

views = Blueprint('views', __name__)

UPLOAD_FOLDER = 'website/static/uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'jpg', 'jpeg', 'docx', 'png', 'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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

@views.route('/user/add_full', methods=['POST'])
def add_full_user():
    if 'data' not in request.form or 'profile_photo' not in request.files:
        return jsonify({'error': 'Missing form data or files'}), 400

    data = json.loads(request.form['data'])

    existing_user = User.query.filter_by(mail=data['mail']).first()
    if existing_user:
        return jsonify({'error': 'User with this email already exists'}), 409

    profile_photo = request.files['profile_photo']
    if profile_photo and allowed_file(profile_photo.filename):
        profile_photo_filename = secure_filename(profile_photo.filename)
        profile_photo_path = os.path.join(UPLOAD_FOLDER, profile_photo_filename)
        profile_photo.save(profile_photo_path)
    else:
        return jsonify({'error': 'Profile photo type not allowed'}), 400

    user = User(
        full_name=data['full_name'],
        date_of_birth=data['date_of_birth'],
        mail=data['mail'],
        marital_status=data.get('marital_status'),
        hobbies=data.get('hobbies'),
        dream_sector1=data.get('dream_sector1'),
        dream_sector2=data.get('dream_sector2'),
        career_plans=data.get('career_plans'),
        additional_info=data.get('additional_info'),
        minor_course_details=data.get('minor_course_details'),
        skills=data.get('skills'),
        transaction_id=data.get('transaction_id'),
        prof_summary=data.get('prof_summary'),
        password=data['password'],
        template_id=data.get('template_id'),
        profile_photo=profile_photo_path
    )
    db.session.add(user)
    db.session.commit()

    for language_data in data.get('languages', []):
        language = Language(
            language=language_data['language'],
            proficiency=language_data['proficiency'],
            user_id=user.id
        )
        db.session.add(language)

    for education_data in data.get('education', []):
        institution = Institution.query.filter_by(name=education_data['institution']).first()
        if not institution:
            institution = Institution(name=education_data['institution'])
            db.session.add(institution)
            db.session.commit()

        education = Education(
            grade_year=education_data['grade_year'],
            grad_year=education_data['grad_year'],
            percentage_cgpa=education_data['percentage_cgpa'],
            specialization=education_data['specialization'],
            institution_id=institution.id,
            user_id=user.id
        )
        db.session.add(education)

    for project_data in data.get('projects', []):
        project = Project(
            title=project_data['title'],
            domain=project_data['domain'],
            duration=project_data['duration'],
            description=project_data['description'],
            url=project_data.get('url'),
            user_id=user.id
        )
        db.session.add(project)

    for social_account_data in data.get('social_accounts', []):
        social_account = SocialAccount(
            name=social_account_data['name'],
            url=social_account_data.get('url'),
            user_id=user.id
        )
        db.session.add(social_account)

    for work_experience_data in data.get('work_experience', []):
        organization = Organization.query.filter_by(name=work_experience_data['organization']).first()
        if not organization:
            organization = Organization(name=work_experience_data['organization'])
            db.session.add(organization)
            db.session.commit()

        work_experience = WorkExperience(
            role=work_experience_data['role'],
            cause=work_experience_data.get('cause'),
            description=work_experience_data.get('description'),
            organization_id=organization.id,
            user_id=user.id
        )
        db.session.add(work_experience)

    for internship_data in data.get('internships', []):
        organization = Organization.query.filter_by(name=internship_data['organization']).first()
        if not organization:
            organization = Organization(name=internship_data['organization'])
            db.session.add(organization)
            db.session.commit()

        internship = Internship(
            role=internship_data['role'],
            cause=internship_data.get('cause'),
            description=internship_data.get('description'),
            organization_id=organization.id,
            user_id=user.id
        )
        db.session.add(internship)

    for volunteer_activity_data in data.get('volunteer_activities', []):
        organization = Organization.query.filter_by(name=volunteer_activity_data['organization']).first()
        if not organization:
            organization = Organization(name=volunteer_activity_data['organization'])
            db.session.add(organization)
            db.session.commit()

        volunteer_activity = VolunteerActivity(
            role=volunteer_activity_data['role'],
            cause=volunteer_activity_data.get('cause'),
            description=volunteer_activity_data.get('description'),
            organization_id=organization.id,
            user_id=user.id
        )
        db.session.add(volunteer_activity)

    for accomplishment_data in data.get('accomplishments', []):
        organization = Organization.query.filter_by(name=accomplishment_data['organization']).first()
        if not organization:
            organization = Organization(name=accomplishment_data['organization'])
            db.session.add(organization)
            db.session.commit()

        accomplishment = Accomplishment(
            name=accomplishment_data['name'],
            description=accomplishment_data.get('description'),
            date=accomplishment_data.get('date'),
            type=accomplishment_data.get('type'),
            organization_id=organization.id,
            user_id=user.id
        )
        db.session.add(accomplishment)

    for position_of_responsibility_data in data.get('positions_of_responsibility', []):
        organization = Organization.query.filter_by(name=position_of_responsibility_data['organization']).first()
        if not organization:
            organization = Organization(name=position_of_responsibility_data['organization'])
            db.session.add(organization)
            db.session.commit()

        position_of_responsibility = PositionOfResponsibility(
            role=position_of_responsibility_data['role'],
            cause=position_of_responsibility_data.get('cause'),
            description=position_of_responsibility_data.get('description'),
            organization_id=organization.id,
            user_id=user.id
        )
        db.session.add(position_of_responsibility)

    for extra_curricular_data in data.get('extra_curriculars', []):
        extra_curricular = ExtraCurricular(
            name=extra_curricular_data['name'],
            category=extra_curricular_data.get('category'),
            description=extra_curricular_data.get('description'),
            user_id=user.id
        )
        db.session.add(extra_curricular)

    for document_data in data.get('documents', []):
        if 'document_file' in request.files:
            document_file = request.files['document_file']
            if document_file and allowed_file(document_file.filename):
                document_filename = secure_filename(document_file.filename)
                document_file_path = os.path.join(UPLOAD_FOLDER, document_filename)
                document_file.save(document_file_path)
            else:
                return jsonify({'error': 'Document file type not allowed'}), 400

            document = Document(
                name=document_data['name'],
                category=document_data['category'],
                description=document_data['description'],
                is_authorized=document_data['is_authorized'],
                file_path=document_file_path,
                user_id=user.id
            )
            db.session.add(document)
        else:
            return jsonify({'error': 'Missing document file'}), 400

    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

@views.route('/user/upload_profile_photo', methods=['POST'])
def upload_profile_photo():
    if 'profile_photo' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['profile_photo']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        return jsonify({'message': 'File uploaded successfully', 'file_path': file_path}), 201

    return jsonify({'error': 'File type not allowed'}), 400

@views.route('/user/upload_document', methods=['POST'])
def upload_document():
    if 'document' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['document']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        return jsonify({'message': 'File uploaded successfully', 'file_path': file_path}), 201

    return jsonify({'error': 'File type not allowed'}), 400


