# {'full_name': 'Param Gandhi', 'date_of_birth': '2024-07-27', 'mail': 'paramagandhi@gmail.com', 'marital_status': '', 'hobbies': '', 'dream_sector1': '', 'dream_sector2': '', 'career_plans': '', 'additional_info': '', 'minor_course_details': '', 'skills': '', 'transaction_id': '', 'prof_summary': '', 'languages': [{'language': '', 'proficiency': ''}], 'education': [{'grade_year': '', 'grad_year': '', 'percentage_cgpa': '', 'specialization': '', 'institution': ''}], 'projects': [{'title': '', 'domain': '', 'duration': '', 'description': '', 'url': ''}], 'social_accounts': [{'name': '', 'url': ''}], 'work_experience': [{'role': '', 'cause': '', 'description': '', 'organization': ''}], 'internships': [{'role': '', 'cause': '', 'description': '', 'organization': ''}], 'volunteer_activities': [{'role': '', 'cause': '', 'description': '', 'organization': ''}], 'accomplishments': [{'name': '', 'description': '', 'date': '', 'organization': ''}], 'positions_of_responsibility': [{'role': '', 'cause': '', 'description': '', 'organization': ''}], 'extra_curriculars': [{'name': '', 'category': '', 'description': ''}], 'certifications': [{'name': '', 'date': '', 'organization': ''}], 'competitions': [{'name': '', 'date': '', 'position': '', 'organization': ''}], 'conferences_workshops': [{'name': '', 'date': '', 'description': '', 'organization': ''}], 'test_scores': [{'name': '', 'date': '', 'score': ''}], 'patents_publications': [{'name': '', 'date': '', 'description': '', 'organization': ''}], 'scholarships': [{'name': '', 'date': '', 'description': '', 'organization': ''}], 'photograph': ''}

# raw_data = {
#   "full_name": "Param Gandhi",
#   "date_of_birth": "2024-07-27",
#   "mail": "paramagandhi@gmail.com",
#   "marital_status": "",
#   "hobbies": "",
#   "dream_sector1": "",
#   "dream_sector2": "",
#   "career_plans": "",
#   "additional_info": "",
#   "minor_course_details": "",
#   "skills": "",
#   "transaction_id": "",
#   "prof_summary": "",
#   "languages": [
#     {
#       "language": "",
#       "proficiency": ""
#     }
#   ],
#   "education": [
#     {
#       "grade_year": "",
#       "grad_year": "",
#       "percentage_cgpa": "",
#       "specialization": "",
#       "institution": ""
#     }
#   ],
#   "projects": [
#     {
#       "title": "",
#       "domain": "",
#       "duration": "",
#       "description": "",
#       "url": ""
#     }
#   ],
#   "social_accounts": [
#     {
#       "name": "",
#       "url": ""
#     }
#   ],
#   "work_experience": [
#     {
#       "role": "",
#       "cause": "",
#       "description": "",
#       "organization": ""
#     }
#   ],
#   "internships": [
#     {
#       "role": "",
#       "cause": "",
#       "description": "",
#       "organization": ""
#     }
#   ],
#   "volunteer_activities": [
#     {
#       "role": "",
#       "cause": "",
#       "description": "",
#       "organization": ""
#     }
#   ],
#   "accomplishments": [
#     {
#       "name": "",
#       "description": "",
#       "date": "",
#       "organization": ""
#     }
#   ],
#   "positions_of_responsibility": [
#     {
#       "role": "",
#       "cause": "",
#       "description": "",
#       "organization": ""
#     }
#   ],
#   "extra_curriculars": [
#     {
#       "name": "",
#       "category": "",
#       "description": ""
#     }
#   ],
#   "certifications": [
#     {
#       "name": "",
#       "date": "",
#       "organization": ""
#     }
#   ],
#   "competitions": [
#     {
#       "name": "",
#       "date": "",
#       "position": "",
#       "organization": ""
#     }
#   ],
#   "conferences_workshops": [
#     {
#       "name": "",
#       "date": "",
#       "description": "",
#       "organization": ""
#     }
#   ],
#   "test_scores": [
#     {
#       "name": "",
#       "date": "",
#       "score": ""
#     }
#   ],
#   "patents_publications": [
#     {
#       "name": "",
#       "date": "",
#       "description": "",
#       "organization": ""
#     }
#   ],
#   "scholarships": [
#     {
#       "name": "",
#       "date": "",
#       "description": "",
#       "organization": ""
#     }
#   ],
#   "photograph": ""
# }

def DataManagement(raw_data):
    data = {
        'full_name': raw_data['full_name'],
        'date_of_birth': raw_data['date_of_birth'],
        'mail': raw_data['mail'],
        # 'marital_status': raw_data['marital_status'],
        # 'hobbies': raw_data['hobbies'],
        'dream_sector1': raw_data['dream_sector1'],
        'dream_sector2': raw_data['dream_sector2'],
        'career_plans': raw_data['career_plans'],
        'additional_info': raw_data['additional_info'],
        'minor_course_details': raw_data['minor_course_details'],
        'skills': raw_data['skills'],
        'prof_summary': raw_data['prof_summary'],
        'languages': raw_data['languages'],
        'education': raw_data['education'],
        'projects': raw_data['projects'],
        'social_accounts': raw_data['social_accounts'],
        'work_experience': raw_data['work_experience'],
        # 'internships': raw_data['internships'],
        'volunteer_activities': raw_data['volunteer_activities'],
        'accomplishments': raw_data['accomplishments'],
        'positions_of_responsibility': raw_data['positions_of_responsibility'],
        'extra_curriculars': raw_data['extra_curriculars'],
        'certifications': raw_data['certifications'],
        'competitions': raw_data['competitions'],
        'conferences_workshops': raw_data['conferences_workshops'],
        'test_scores': raw_data['test_scores'],
        'patents_publications': raw_data['patents_publications'],
        'scholarships': raw_data['scholarships'],
    }

    return data
