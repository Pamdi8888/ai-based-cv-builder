from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, json
# from .llm.query import enhance_text
from .models import *
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash
import os
from . import dataMgmt
from .llm.query import get_mistral as llm_service
from .llm.template import query_template
import uuid

views = Blueprint('views', __name__)

UPLOAD_FOLDER = 'website/static/uploads'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def password_hash(password):
    return generate_password_hash(password)


@views.route('/static/main', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        raw_data = json.loads(request.form.get('data'))

        print(f"Raw Data: {raw_data}")

        try:
            organization_photo = request.files['organization_photograph']
        except:
            organization_photo = None
        if organization_photo and allowed_file(organization_photo.filename):
            organization_photo_filename = secure_filename(organization_photo.filename)
            organization_photo_path = os.path.join(UPLOAD_FOLDER, organization_photo_filename)
            organization_photo.save(organization_photo_path)

        try:
            profile_photo = request.files['photograph']
        except:
            profile_photo = None
        if profile_photo and allowed_file(profile_photo.filename):
            profile_photo_filename = secure_filename(profile_photo.filename)
            profile_photo_path = os.path.join(UPLOAD_FOLDER, profile_photo_filename)
            profile_photo.save(profile_photo_path)

        # try:
        #     formatted_query = query_template.template.format(query=raw_data)
        #     ai_raw_data = json.loads(llm_service(formatted_query))
        #     print(f"AI Raw Data: {ai_raw_data}")
        #     ai_data = dataMgmt.DataManagement(ai_raw_data)
        #     print("AI Generated CV Rendered")
        #     return render_template('temp2.html', **ai_data)
        # except:
        data = dataMgmt.DataManagement(raw_data)
        print("User Data based CV Rendered")
        return render_template("temp2.html", **data)
    return render_template('index.html')


@views.route('/main')
def root():
    return redirect('/static/main')

@views.route('/')
def root_default():
    return redirect('/static/main')

@views.route('/static/main/')
def root_static():
    return redirect('/static/main')


# @views.route('/enhance', methods=['POST'])
# def enhance():
#     data = request.get_json()
#     prompt = data['prompt']
#     enhanced_text = enhance_text(prompt)
#     return jsonify({'enhanced_text': enhanced_text})


@views.route("/message", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data["query"]
    formatted_query = query_template.template.format(query=user_message)
    result = llm_service(formatted_query)
    return jsonify({"output": result})


@views.route('/user/add_full', methods=['POST'])
def add_full_user():
    # if 'data' not in request.form or 'profile_photo' not in request.files:
    #     return jsonify({'error': 'Missing form data or files'}), 400

    data = json.loads(request.form.get('data'))
    # print("a")
    # existing_user = User.query.filter_by(mail=data['mail']).first()
    # if existing_user:
    #     return jsonify({'error': 'User with this email already exists'}), 409
    # print('b')
    organization_photo_path = None
    try:
        organization_photo = request.files['organization_photograph']
    except:
        organization_photo = None
    if organization_photo and allowed_file(organization_photo.filename):
        organization_photo_filename = secure_filename(organization_photo.filename)
        organization_photo_path = os.path.join(UPLOAD_FOLDER, organization_photo_filename)
        organization_photo.save(organization_photo_path)
    # print('c')
    try:
        profile_photo = request.files['photograph']
    except:
        profile_photo = None
    if profile_photo and allowed_file(profile_photo.filename):
        profile_photo_filename = secure_filename(profile_photo.filename)
        profile_photo_path = os.path.join(UPLOAD_FOLDER, profile_photo_filename)
        profile_photo.save(profile_photo_path)
    else:
        return jsonify({'error': 'Profile photo type not allowed'}), 400

    print(f"data: {data} \n photo: {profile_photo} \n organization_photo: {organization_photo}s")

    t_id = str(uuid.uuid4())

    user = User(
        full_name=data['full_name'],
        date_of_birth=data['date_of_birth'],
        mail=data['mail'],
        dream_sector1=data.get('dream_sector1'),
        dream_sector2=data.get('dream_sector2'),
        career_plans=data.get('career_plans'),
        additional_info=data.get('additional_info'),
        minor_course_details=data.get('minor_course_details'),
        subjects=json.dumps(data.get('subjects')),
        skills=json.dumps(data.get('skills')),
        transaction_id=t_id,
        prof_summary=data.get('prof_summary'),
        # password=password_hash(data['password']),
        password='dummy_password',
        template_id=data.get('format'),
        profile_photo=profile_photo_path,
        organization_photo=organization_photo_path
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
            board_university=education_data['board_university'],
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
            description=work_experience_data.get('description'),
            duration=work_experience_data.get('duration'),
            organization_id=organization.id,
            user_id=user.id
        )
        db.session.add(work_experience)
    for volunteer_activity_data in data.get('volunteer_activities', []):
        organization = Organization.query.filter_by(name=volunteer_activity_data['organization']).first()
        if not organization:
            organization = Organization(name=volunteer_activity_data['organization'])
            db.session.add(organization)
            db.session.commit()
        volunteer_activity = VolunteerActivity(
            role=volunteer_activity_data['role'],
            description=volunteer_activity_data.get('description'),
            date=volunteer_activity_data.get('date'),
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
            description=position_of_responsibility_data.get('description'),
            duration=position_of_responsibility_data.get('duration'),
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
    for certification_data in data.get('certifications', []):
        organization = Organization.query.filter_by(name=certification_data['organization']).first()
        if not organization:
            organization = Organization(name=certification_data['organization'])
            db.session.add(organization)
            db.session.commit()
        certification = Certification(
            name=certification_data['name'],
            date=certification_data.get('date'),
            organization_id=organization.id,
            user_id=user.id
        )
        db.session.add(certification)
    for competition_data in data.get('competitions', []):
        organization = Organization.query.filter_by(name=competition_data['organization']).first()
        if not organization:
            organization = Organization(name=competition_data['organization'])
            db.session.add(organization)
            db.session.commit()
        competition = Competition(
            name=competition_data['name'],
            date=competition_data.get('date'),
            position=competition_data.get('position'),
            organization_id=organization.id,
            user_id=user.id
        )
        db.session.add(competition)
    for conference_workshop_data in data.get('conferences_workshops', []):
        organization = Organization.query.filter_by(name=conference_workshop_data['organization']).first()
        if not organization:
            organization = Organization(name=conference_workshop_data['organization'])
            db.session.add(organization)
            db.session.commit()
        conference_workshop = ConferenceWorkshop(
            name=conference_workshop_data['name'],
            date=conference_workshop_data.get('date'),
            description=conference_workshop_data.get('description'),
            organization_id=organization.id,
            user_id=user.id
        )
        db.session.add(conference_workshop)
    for test_score_data in data.get('test_scores', []):
        test_score = TestScore(
            name=test_score_data['name'],
            date=test_score_data.get('date'),
            score=test_score_data.get('score'),
            user_id=user.id
        )
        db.session.add(test_score)
    for patent_publication_data in data.get('patents_publications', []):
        organization = Organization.query.filter_by(name=patent_publication_data['organization']).first()
        if not organization:
            organization = Organization(name=patent_publication_data['organization'])
            db.session.add(organization)
            db.session.commit()
        patent_publication = PatentPublication(
            name=patent_publication_data['name'],
            date=patent_publication_data.get('date'),
            description=patent_publication_data.get('description'),
            organization_id=organization.id,
            user_id=user.id
        )
        db.session.add(patent_publication)
    for scholarship_data in data.get('scholarships', []):
        organization = Organization.query.filter_by(name=scholarship_data['organization']).first()
        if not organization:
            organization = Organization(name=scholarship_data['organization'])
            db.session.add(organization)
            db.session.commit()
        scholarship = Scholarship(
            name=scholarship_data['name'],
            date=scholarship_data.get('date'),
            description=scholarship_data.get('description'),
            organization_id=organization.id,
            user_id=user.id
        )
        db.session.add(scholarship)
    db.session.commit()
    return jsonify({'message': f'User created successfully with id: {t_id}'}), 201
