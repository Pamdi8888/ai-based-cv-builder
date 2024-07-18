from enum import unique
from . import db

class User(db.Model):
    __tablename__ = 'user_info'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name = db.Column(db.String(255), nullable=False)
    date_of_birth = db.Column(db.Date)
    mail = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(15))
    profession = db.Column(db.String(255))
    subjects = db.Column(db.Text)
    skills = db.Column(db.Text)
    transaction_id = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), nullable=False)
    template_id = db.Column(db.Integer, db.ForeignKey('templates.id'))
    profile_photo = db.Column(db.String(255))
    organization_photo = db.Column(db.String(255))

    # dream_sector1 = db.Column(db.String(255))
    # dream_sector2 = db.Column(db.String(255))
    # career_plans = db.Column(db.Text)
    # additional_info = db.Column(db.Text)
    # minor_course_details = db.Column(db.Text)
    # prof_summary = db.Column(db.Text)
    
    # social_accounts = db.relationship("SocialAccount", back_populates="user", cascade="all, delete-orphan")

    template = db.relationship("Template")
    languages = db.relationship("Language", back_populates="user", cascade="all, delete-orphan")
    education = db.relationship("Education", back_populates="user", cascade="all, delete-orphan")
    projects = db.relationship("Project", back_populates="user", cascade="all, delete-orphan")
    work_experience = db.relationship("WorkExperience", back_populates="user", cascade="all, delete-orphan")
    volunteer_activities = db.relationship("VolunteerActivity", back_populates="user", cascade="all, delete-orphan")
    accomplishments = db.relationship("Accomplishment", back_populates="user", cascade="all, delete-orphan")
    positions_of_responsibility = db.relationship("PositionOfResponsibility", back_populates="user", cascade="all, delete-orphan")
    extra_curriculars = db.relationship("ExtraCurricular", back_populates="user", cascade="all, delete-orphan")
    certifications = db.relationship("Certification", back_populates="user", cascade="all, delete-orphan")
    competitions = db.relationship("Competition", back_populates="user", cascade="all, delete-orphan")
    conferences_workshops = db.relationship("ConferenceWorkshop", back_populates="user", cascade="all, delete-orphan")
    test_scores = db.relationship("TestScore", back_populates="user", cascade="all, delete-orphan")
    patents_publications = db.relationship("PatentPublication", back_populates="user", cascade="all, delete-orphan")
    scholarships = db.relationship("Scholarship", back_populates="user", cascade="all, delete-orphan")


class Language(db.Model):
    __tablename__ = 'language'
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(100))
    proficiency = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id', ondelete='CASCADE'))
    
    user = db.relationship('User', back_populates='languages')


class Education(db.Model):
    __tablename__ = 'education'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    board_university = db.Column(db.String(255))  # New field for board/university
    grad_year = db.Column(db.String(10))
    percentage_cgpa = db.Column(db.String(10))
    specialization = db.Column(db.String(100))
    institution_id = db.Column(db.Integer, db.ForeignKey('institution.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id', ondelete='CASCADE'))
    
    user = db.relationship("User", back_populates="education")
    institution = db.relationship("Institution")


class Institution(db.Model):
    __tablename__ = 'institution'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    education = db.relationship("Education", back_populates="institution")


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
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id', ondelete='CASCADE'))
    
    user = db.relationship('User', back_populates='projects')




class WorkExperience(db.Model):
    __tablename__ = 'work_experience'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    duration = db.Column(db.String(50))  # New field for duration
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id', ondelete='CASCADE'))
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'))
    
    user = db.relationship("User", back_populates="work_experience")
    organization = db.relationship("Organization")


class VolunteerActivity(db.Model):
    __tablename__ = 'volunteer_activity'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    date = db.Column(db.String(255)) 
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id', ondelete='CASCADE'))
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'))
    
    user = db.relationship("User", back_populates="volunteer_activities")
    organization = db.relationship("Organization")


class Accomplishment(db.Model):
    __tablename__ = 'accomplishment'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    date = db.Column(db.String(255))
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id', ondelete='CASCADE'))
    
    user = db.relationship("User", back_populates="accomplishments")
    organization = db.relationship("Organization")


class PositionOfResponsibility(db.Model):
    __tablename__ = 'position_of_responsibility'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    duration = db.Column(db.String(50))  # New field for duration
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id', ondelete='CASCADE'))
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'))
    
    user = db.relationship("User", back_populates="positions_of_responsibility")
    organization = db.relationship("Organization")


class ExtraCurricular(db.Model):
    __tablename__ = 'extra_curricular'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(50))
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id', ondelete='CASCADE'))
    
    user = db.relationship("User", back_populates="extra_curriculars")


class Organization(db.Model):
    __tablename__ = 'organization'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    
    work_experience = db.relationship("WorkExperience", back_populates="organization")
    volunteer_activities = db.relationship("VolunteerActivity", back_populates="organization")
    accomplishments = db.relationship("Accomplishment", back_populates="organization")
    positions_of_responsibility = db.relationship("PositionOfResponsibility", back_populates="organization")


class Certification(db.Model):
    __tablename__ = 'certification'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    date = db.Column(db.String(255))
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id', ondelete='CASCADE'))
    
    user = db.relationship("User", back_populates="certifications")
    organization = db.relationship("Organization")


class Competition(db.Model):
    __tablename__ = 'competition'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    date = db.Column(db.String(255))
    position = db.Column(db.String(255))
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id', ondelete='CASCADE'))
    
    user = db.relationship("User", back_populates="competitions")
    organization = db.relationship("Organization")


class ConferenceWorkshop(db.Model):
    __tablename__ = 'conference_workshop'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    date = db.Column(db.String(255))
    description = db.Column(db.Text)
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id', ondelete='CASCADE'))
    
    user = db.relationship("User", back_populates="conferences_workshops")
    organization = db.relationship("Organization")


class TestScore(db.Model):
    __tablename__ = 'test_score'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    date = db.Column(db.String(255))
    score = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id', ondelete='CASCADE'))
    
    user = db.relationship("User", back_populates="test_scores")


class PatentPublication(db.Model):
    __tablename__ = 'patent_publication'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    date = db.Column(db.String(255))
    description = db.Column(db.Text)
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id', ondelete='CASCADE'))
    
    user = db.relationship("User", back_populates="patents_publications")
    organization = db.relationship("Organization")


class Scholarship(db.Model):
    __tablename__ = 'scholarship'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    date = db.Column(db.String(255))
    description = db.Column(db.Text)
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id', ondelete='CASCADE'))
    
    user = db.relationship("User", back_populates="scholarships")
    organization = db.relationship("Organization")

# class SocialAccount(db.Model):
#     __tablename__ = 'social_account'
    
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(255), nullable=False)
#     url = db.Column(db.String(255))
#     user_id = db.Column(db.Integer, db.ForeignKey('user_info.id', ondelete='CASCADE'))
    
#     user = db.relationship("User", back_populates="social_accounts")