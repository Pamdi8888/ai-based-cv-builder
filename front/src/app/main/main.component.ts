import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormArray, Validators, FormGroup} from '@angular/forms';
import jsPDF from 'jspdf';
import html2canvas from 'html2canvas';
import {subjectValidator} from 'src/validators/subject-validator';
import {degreeValidator} from 'src/validators/degree-validator';
import {requiredFieldValidator} from 'src/validators/required-field-validator';
import {dateValidator} from 'src/validators/date-validator';
import {emailValidator} from 'src/validators/email-validator';
import {passwordValidator} from 'src/validators/password-validator';
import {templateIdValidator} from 'src/validators/template-id-validator';
import {graduationYearValidator} from 'src/validators/graduation-year-validator';
import {HttpClient} from '@angular/common/http';


@Component({
    selector: 'app-main',
    templateUrl: './main.component.html',
    styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

    mainForm: FormGroup;
    selectedFile: File | null = null;

    constructor(private fb: FormBuilder, private http: HttpClient) {
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
            // password: ['', [Validators.required, Validators.minLength(6)]],
            // template_id: [1, [Validators.required]],
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
            //  documents: this.fb.array([this.createDocument()])
            certifications: this.fb.array([this.createCertification()]),
            competitions: this.fb.array([this.createCompetition()]),
            conferences_workshops: this.fb.array([this.createConferenceWorkshop()]),
            test_scores: this.fb.array([this.createTestScore()]),
            patents_publications: this.fb.array([this.createPatentPublication()]),
            scholarships: this.fb.array([this.createScholarship()]),
            photograph: ['']
        });
    }

    ngOnInit(): void {
    }

    // Getter methods for form arrays
    get languagesFormArray() {
        return this.mainForm.get('languages') as FormArray;
    }

    get educationFormArray() {
        return this.mainForm.get('education') as FormArray;
    }

    get projectsFormArray() {
        return this.mainForm.get('projects') as FormArray;
    }

    get socialAccountsFormArray() {
        return this.mainForm.get('social_accounts') as FormArray;
    }

    get workExperienceFormArray() {
        return this.mainForm.get('work_experience') as FormArray;
    }

    get internshipsFormArray() {
        return this.mainForm.get('internships') as FormArray;
    }

    get volunteerActivitiesFormArray() {
        return this.mainForm.get('volunteer_activities') as FormArray;
    }

    get accomplishmentsFormArray() {
        return this.mainForm.get('accomplishments') as FormArray;
    }

    get positionsOfResponsibilityFormArray() {
        return this.mainForm.get('positions_of_responsibility') as FormArray;
    }

    get extraCurricularsFormArray() {
        return this.mainForm.get('extra_curriculars') as FormArray;
    }

    //get documentsFormArray() { return this.mainForm.get('documents') as FormArray; }
    get certificationsFormArray() {
        return this.mainForm.get('certifications') as FormArray;
    }

    get competitionsFormArray() {
        return this.mainForm.get('competitions') as FormArray;
    }

    get conferencesWorkshopsFormArray() {
        return this.mainForm.get('conferences_workshops') as FormArray;
    }

    get testScoresFormArray() {
        return this.mainForm.get('test_scores') as FormArray;
    }

    get patentsPublicationsFormArray() {
        return this.mainForm.get('patents_publications') as FormArray;
    }

    get scholarshipsFormArray() {
        return this.mainForm.get('scholarships') as FormArray;
    }

    // Methods to add new form groups to form arrays
    addLanguage() {
        this.languagesFormArray.push(this.createLanguage());
    }

    addEducation() {
        this.educationFormArray.push(this.createEducation());
    }

    addProject() {
        this.projectsFormArray.push(this.createProject());
    }

    addSocialAccount() {
        this.socialAccountsFormArray.push(this.createSocialAccount());
    }

    addWorkExperience() {
        this.workExperienceFormArray.push(this.createWorkExperience());
    }

    addInternship() {
        this.internshipsFormArray.push(this.createInternship());
    }

    addVolunteerActivity() {
        this.volunteerActivitiesFormArray.push(this.createVolunteerActivity());
    }

    addAccomplishment() {
        this.accomplishmentsFormArray.push(this.createAccomplishment());
    }

    addPositionOfResponsibility() {
        this.positionsOfResponsibilityFormArray.push(this.createPositionOfResponsibility());
    }

    addExtraCurricular() {
        this.extraCurricularsFormArray.push(this.createExtraCurricular());
    }

    //addDocument() { this.documentsFormArray.push(this.createDocument()); }
    addCertification() {
        this.certificationsFormArray.push(this.createCertification());
    }

    addCompetition() {
        this.competitionsFormArray.push(this.createCompetition());
    }

    addConferenceWorkshop() {
        this.conferencesWorkshopsFormArray.push(this.createConferenceWorkshop());
    }

    addTestScore() {
        this.testScoresFormArray.push(this.createTestScore());
    }

    addPatentPublication() {
        this.patentsPublicationsFormArray.push(this.createPatentPublication());
    }

    addScholarship() {
        this.scholarshipsFormArray.push(this.createScholarship());
    }

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
            grad_year: [''],
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
            //  type: [''],
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

    // createDocument(): FormGroup {
    //   return this.fb.group({
    //     name: [''],
    //     category: [''],
    //     description: ['']
    //   });
    // }

    createCertification(): FormGroup {
        return this.fb.group({
            name: [''],
            date: [''],
            organization: ['']
        });
    }

    createCompetition(): FormGroup {
        return this.fb.group({
            name: [''],
            date: [''],
            position: [''],
            organization: ['']
        });
    }

    createConferenceWorkshop(): FormGroup {
        return this.fb.group({
            name: [''],
            date: [''],
            description: [''],
            organization: ['']
        });
    }

    createTestScore(): FormGroup {
        return this.fb.group({
            name: [''],
            date: [''],
            score: ['']
        });
    }

    createPatentPublication(): FormGroup {
        return this.fb.group({
            name: [''],
            date: [''],
            description: [''],
            organization: ['']
        });
    }

    createScholarship(): FormGroup {
        return this.fb.group({
            name: [''],
            date: [''],
            description: [''],
            organization: ['']
        });
    }

    onFileSelected(event: any): void {
        const file = event.target.files[0];
        if (file && (file.type === 'image/jpeg' || file.type === 'image/jpg')) {
            this.selectedFile = file;
            this.mainForm.patchValue({
                photograph: file.name
            });
        } else {
            alert('Please select a valid .jpg or .jpeg file.');
            this.selectedFile = null;
            this.mainForm.patchValue({
                photograph: ''
            });
        }
    }

    onSubmit(): void {
        if (this.mainForm.valid) {
            console.log('Form Data:', this.mainForm.value);
            // You can use FormData to send both form data and file
            const formData = this.mainForm.value;
            // if (this.selectedFile) {
            //     // Here you would typically send the file to your server
            //     console.log('Selected File:', this.selectedFile);
            //     formData.append('photograph', this.selectedFile, this.selectedFile.name);
            // }
            // Append other form data as needed
            // for (const key in this.mainForm.value) {
            //     formData.append(key, this.mainForm.value[key]);
            // }

            // Send formData to your server
            console.log('FormData:', formData);
            this.http.post('http://127.0.0.1:5000/static', formData, {responseType: 'text'})
                .subscribe((response) => {
                        console.log('Form Submitted Successfully:');
                        const newWindow = window.open();
                        if (newWindow) {
                            newWindow.document.write(response);
                            newWindow.document.close();
                        } else {
                            console.error('Failed to open new window');
                        }
                    }, (error) => {
                        console.error('Error submitting form:', error);
                    }
                );
        } else {
            console.log('Form is invalid');
        }
    }
}
