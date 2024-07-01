import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormArray, Validators } from '@angular/forms';
import jsPDF from 'jspdf';
import html2canvas from 'html2canvas';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  constructor(private fb: FormBuilder,) {}

  mainForm: any;

  ngOnInit(): void {
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

  createLanguage(): any {
    return this.fb.group({
      language: [''],
      proficiency: ['']
    });
  }

  createEducation(): any {
    return this.fb.group({
      grade_year: [''],
      grad_year: ['', [Validators.required]],
      percentage_cgpa: [''],
      specialization: [''],
      institution: ['']
    });
  }

  createProject(): any {
    return this.fb.group({
      title: [''],
      domain: [''],
      duration: [''],
      description: [''],
      url: ['']
    });
  }

  createSocialAccount(): any {
    return this.fb.group({
      name: [''],
      url: ['']
    });
  }

  createWorkExperience(): any {
    return this.fb.group({
      role: [''],
      cause: [''],
      description: [''],
      organization: ['']
    });
  }

  createInternship(): any {
    return this.fb.group({
      role: [''],
      cause: [''],
      description: [''],
      organization: ['']
    });
  }

  createVolunteerActivity(): any {
    return this.fb.group({
      role: [''],
      cause: [''],
      description: [''],
      organization: ['']
    });
  }

  createAccomplishment(): any {
    return this.fb.group({
      name: [''],
      description: [''],
      date: [''],
      type: [''],
      organization: ['']
    });
  }

  createPositionOfResponsibility(): any {
    return this.fb.group({
      role: [''],
      cause: [''],
      description: [''],
      organization: ['']
    });
  }

  createExtraCurricular(): any {
    return this.fb.group({
      name: [''],
      category: [''],
      description: ['']
    });
  }

  createDocument(): any {
    return this.fb.group({
      name: [''],
      category: [''],
      description: ['']
    });
  }

  onSubmit(): void {
    const formData = this.mainForm.value;
    console.log('Form Data:', formData);
    // Process the form data as per the backend requirements
  }

}
