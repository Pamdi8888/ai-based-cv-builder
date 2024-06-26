from . import db

class User(db.Model):
    __tablename__ = 'user_info'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name = db.Column(db.String(255), nullable=False)
    date_of_birth = db.Column(db.Date)
    mail = db.Column(db.String(255), nullable=False, unique=True)
    marital_status = db.Column(db.String(50))
    hobbies = db.Column(db.Text)
    dream_sector1 = db.Column(db.String(255))
    dream_sector2 = db.Column(db.String(255))
    career_plans = db.Column(db.Text)
    additional_info = db.Column(db.Text)
    minor_course_details = db.Column(db.Text)
    skills = db.Column(db.Text)
    transaction_id = db.Column(db.String(255))
    prof_summary = db.Column(db.Text)
    password = db.Column(db.String(255), nullable=False)
    template_id = db.Column(db.Integer, db.ForeignKey('templates.id'))
    
    template = db.relationship("Template")
    languages = db.relationship("Language", back_populates="user")
    education = db.relationship("Education", back_populates="user")
    projects = db.relationship("Project", back_populates="user")
    social_accounts = db.relationship("SocialAccount", back_populates="user")
    work_experience = db.relationship("WorkExperience", back_populates="user")
    internships = db.relationship("Internship", back_populates="user")
    volunteer_activities = db.relationship("VolunteerActivity", back_populates="user")
    accomplishments = db.relationship("Accomplishment", back_populates="user")
    positions_of_responsibility = db.relationship("PositionOfResponsibility", back_populates="user")
    extra_curriculars = db.relationship("ExtraCurricular", back_populates="user")
    documents = db.relationship("Document", back_populates="user")

class Language(db.Model):
    __tablename__ = 'language'
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(100))
    proficiency = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id'))
    
    user = db.relationship('User', back_populates='languages')

class Education(db.Model):
    __tablename__ = 'education'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    grade_year = db.Column(db.String(50), nullable=False)
    grad_year = db.Column(db.Integer)
    percentage_cgpa = db.Column(db.String(10))
    specialization = db.Column(db.String(100))
    institution_id = db.Column(db.Integer, db.ForeignKey('institution.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id'))
    
    user = db.relationship("User", back_populates="education")
    institution = db.relationship("Institution")

class Institution(db.Model):
    __tablename__ = 'institution'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    education = db.relationship("Education", back_populates="institution")

class Document(db.Model):
    __tablename__ = 'document'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    category = db.Column(db.String(50))
    description = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id'))
    
    user = db.relationship('User', back_populates='documents')

class Template(db.Model):
    __tablename__ = 'templates'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    domain = db.Column(db.String(100))
    duration = db.Column(db.String(50))
    description = db.Column(db.String(500))
    url = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id'))
    
    user = db.relationship('User', back_populates='projects')

class SocialAccount(db.Model):
    __tablename__ = 'social_account'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id'))
    
    user = db.relationship("User", back_populates="social_accounts")

class WorkExperience(db.Model):
    __tablename__ = 'work_experience'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role = db.Column(db.String(255), nullable=False)
    cause = db.Column(db.String(255))
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id'))
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'))
    
    user = db.relationship("User", back_populates="work_experience")
    organization = db.relationship("Organization")

class Internship(db.Model):
    __tablename__ = 'internship'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role = db.Column(db.String(255), nullable=False)
    cause = db.Column(db.String(255))
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id'))
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'))
    
    user = db.relationship("User", back_populates="internships")
    organization = db.relationship("Organization")

class VolunteerActivity(db.Model):
    __tablename__ = 'volunteer_activity'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role = db.Column(db.String(255), nullable=False)
    cause = db.Column(db.String(255))
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id'))
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'))
    
    user = db.relationship("User", back_populates="volunteer_activities")
    organization = db.relationship("Organization")

class Accomplishment(db.Model):
    __tablename__ = 'accomplishment'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    date = db.Column(db.Date)
    type = db.Column(db.String(50))
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id'))
    
    user = db.relationship("User", back_populates="accomplishments")
    organization = db.relationship("Organization")

class PositionOfResponsibility(db.Model):
    __tablename__ = 'position_of_responsibility'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role = db.Column(db.String(255), nullable=False)
    cause = db.Column(db.String(255))
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id'))
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'))
    
    user = db.relationship("User", back_populates="positions_of_responsibility")
    organization = db.relationship("Organization")

class ExtraCurricular(db.Model):
    __tablename__ = 'extra_curricular'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(50))
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id'))
    
    user = db.relationship("User", back_populates="extra_curriculars")

class Organization(db.Model):
    __tablename__ = 'organization'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(50))
    
    work_experience = db.relationship("WorkExperience", back_populates="organization")
    internships = db.relationship("Internship", back_populates="organization")
    volunteer_activities = db.relationship("VolunteerActivity", back_populates="organization")
    accomplishments = db.relationship("Accomplishment", back_populates="organization")
    positions_of_responsibility = db.relationship("PositionOfResponsibility", back_populates="organization")
