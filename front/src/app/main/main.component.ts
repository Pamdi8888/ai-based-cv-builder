import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormArray, Validators, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  mainForm: FormGroup;

  constructor(private fb: FormBuilder) {
    this.mainForm = this.fb.group({
      full_name: ['', [Validators.required, Validators.minLength(3)]],
      date_of_birth: ['', [Validators.required]],
      mail: ['', [Validators.required, Validators.email]],
      marital_status: [''],
      hobbies: [''],
      dream_sector1: [''],
      dream_sector2: [''],
      career_plans: [''],
      additional_info: [''],
      minor_course_details: [''],
      skills: [''],
      transaction_id: [''],
      prof_summary: [''],
      password: ['', [Validators.required, Validators.minLength(6)]],
      template_id: [1, [Validators.required]],
      languages: this.fb.array([this.createLanguage()]),
      education: this.fb.array([this.createEducation()]),
      projects: this.fb.array([this.createProject()]),
      social_accounts: this.fb.array([this.createSocialAccount()]),
      work_experience: this.fb.array([this.createWorkExperience()]),
      internships: this.fb.array([this.createInternship()]),
      volunteer_activities: this.fb.array([this.createVolunteerActivity()]),
      accomplishments: this.fb.array([this.createAccomplishment()]),
      positions_of_responsibility: this.fb.array([this.createPositionOfResponsibility()]),
      extra_curriculars: this.fb.array([this.createExtraCurricular()]),
      documents: this.fb.array([this.createDocument()])
    });
  }

  ngOnInit(): void {}

  // Getter methods for form arrays
  get languagesFormArray() { return this.mainForm.get('languages') as FormArray; }
  get educationFormArray() { return this.mainForm.get('education') as FormArray; }
  get projectsFormArray() { return this.mainForm.get('projects') as FormArray; }
  get socialAccountsFormArray() { return this.mainForm.get('social_accounts') as FormArray; }
  get workExperienceFormArray() { return this.mainForm.get('work_experience') as FormArray; }
  get internshipsFormArray() { return this.mainForm.get('internships') as FormArray; }
  get volunteerActivitiesFormArray() { return this.mainForm.get('volunteer_activities') as FormArray; }
  get accomplishmentsFormArray() { return this.mainForm.get('accomplishments') as FormArray; }
  get positionsOfResponsibilityFormArray() { return this.mainForm.get('positions_of_responsibility') as FormArray; }
  get extraCurricularsFormArray() { return this.mainForm.get('extra_curriculars') as FormArray; }
  get documentsFormArray() { return this.mainForm.get('documents') as FormArray; }

  // Methods to add new form groups to form arrays
  addLanguage() { this.languagesFormArray.push(this.createLanguage()); }
  addEducation() { this.educationFormArray.push(this.createEducation()); }
  addProject() { this.projectsFormArray.push(this.createProject()); }
  addSocialAccount() { this.socialAccountsFormArray.push(this.createSocialAccount()); }
  addWorkExperience() { this.workExperienceFormArray.push(this.createWorkExperience()); }
  addInternship() { this.internshipsFormArray.push(this.createInternship()); }
  addVolunteerActivity() { this.volunteerActivitiesFormArray.push(this.createVolunteerActivity()); }
  addAccomplishment() { this.accomplishmentsFormArray.push(this.createAccomplishment()); }
  addPositionOfResponsibility() { this.positionsOfResponsibilityFormArray.push(this.createPositionOfResponsibility()); }
  addExtraCurricular() { this.extraCurricularsFormArray.push(this.createExtraCurricular()); }
  addDocument() { this.documentsFormArray.push(this.createDocument()); }
  
  // Methods to create form groups
  createLanguage(): FormGroup {
    return this.fb.group({
      language: [''],
      proficiency: ['']
    });
  }

  createEducation(): FormGroup {
    return this.fb.group({
      grade_year: [''],
      grad_year: ['', [Validators.required]],
      percentage_cgpa: [''],
      specialization: [''],
      institution: ['']
    });
  }

  createProject(): FormGroup {
    return this.fb.group({
      title: [''],
      domain: [''],
      duration: [''],
      description: [''],
      url: ['']
    });
  }

  createSocialAccount(): FormGroup {
    return this.fb.group({
      name: [''],
      url: ['']
    });
  }

  createWorkExperience(): FormGroup {
    return this.fb.group({
      role: [''],
      cause: [''],
      description: [''],
      organization: ['']
    });
  }

  createInternship(): FormGroup {
    return this.fb.group({
      role: [''],
      cause: [''],
      description: [''],
      organization: ['']
    });
  }

  createVolunteerActivity(): FormGroup {
    return this.fb.group({
      role: [''],
      cause: [''],
      description: [''],
      organization: ['']
    });
  }

  createAccomplishment(): FormGroup {
    return this.fb.group({
      name: [''],
      description: [''],
      date: [''],
      type: [''],
      organization: ['']
    });
  }

  createPositionOfResponsibility(): FormGroup {
    return this.fb.group({
      role: [''],
      cause: [''],
      description: [''],
      organization: ['']
    });
  }

  createExtraCurricular(): FormGroup {
    return this.fb.group({
      name: [''],
      category: [''],
      description: ['']
    });
  }

  createDocument(): FormGroup {
    return this.fb.group({
      name: [''],
      category: [''],
      description: ['']
    });
  }

  onSubmit(): void {
    if (this.mainForm.valid) {
      console.log('Form Data:', this.mainForm.value);
      // Process the form data as per the backend requirements
    } else {
      console.log('Form is invalid');
    }
  }
}
