import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormArray, Validators } from '@angular/forms';
import jsPDF from 'jspdf';
import html2canvas from 'html2canvas';
import { subjectValidator } from 'src/validators/subject-validator';
import { degreeValidator } from 'src/validators/degree-validator';



@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  constructor(private fb: FormBuilder,) {

  }
  mainForm: any;
  ngOnInit(): void {
    this.mainForm = this.fb.group({
      personal: this.fb.group({
        name: ['', [Validators.required, Validators.minLength(3)]],
        email: ['', [Validators.required, Validators.email]],
        phone: ['', [Validators.required, Validators.pattern('^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$')]],
        linkedIn: ['']
      }),
      address: this.fb.group({
        street: ['', [Validators.maxLength(20), Validators.minLength(3)]],
        city: ['', [Validators.required, Validators.maxLength(20), Validators.minLength(2)]],
        state: ['', [Validators.required, Validators.maxLength(20), Validators.minLength(2)]],
        country: ['', [Validators.required, Validators.maxLength(20), Validators.minLength(2)]],
        postal: ['', [Validators.required]]
      }),
      education: this.fb.group({
        higher: this.fb.group({
          school: ['', [Validators.required, Validators.maxLength(40), Validators.minLength(5)]],
          grades: ['', [Validators.required, Validators.maxLength(8), Validators.minLength(1)]],
          year: ['', [Validators.required]],
          class: ['', [Validators.required, subjectValidator(/Select Subject/)]],
        }),
        graduation: this.fb.group({
          college: ['', [Validators.required, Validators.maxLength(40), Validators.minLength(5)]],
          grades: ['', [Validators.required, Validators.maxLength(8), Validators.minLength(1)]],
          year: ['', [Validators.required]],
          degree: ['', [Validators.required, degreeValidator(/Select Degree/)]],
        }),
        postGraduation: this.fb.group({
          college: ['', [Validators.maxLength(40), Validators.minLength(5)]],
          grades: ['', [Validators.maxLength(8), Validators.minLength(1)]],
          year: ['', []],
          degree: ['', [degreeValidator(/Select Degree/)]],
        }),
      }),
      skills: this.fb.array(["", "", ""]),
      techSkills: this.fb.array(["", "", ""]),
      hobbies: this.fb.array(["", "", ""]),
      experience: this.fb.array([
        this.fb.group({
          orgnization: [''],
          position: [''],
          joined: [''],
          workedTill: [''],
          current: [false],
          responsblities1: [''],
          responsblities2: [''],
        })
      ]),
      refrences: this.fb.array(["", ""]),
      languages: this.fb.array(["", ""]),
    })

  }


  get mySkills() {
    return this.mainForm.get('skills') as FormArray;
  }

  addSkill() {
    this.mySkills.push(this.fb.control(''));
  }

  get myTechSkills() {
    return this.mainForm.get('techSkills') as FormArray;
  }

  addTechSkills() {
    this.myTechSkills.push(this.fb.control(''));
  }

  get myHobbies() {
    return this.mainForm.get('hobbies') as FormArray;
  }

  addHobbies() {
    this.myHobbies.push(this.fb.control(''));
  }

  get myExperience() {
    return this.mainForm.controls['experience'] as FormArray;
  }

  addExperience() {
    let exps = this.fb.group({
      orgnization: [''],
      position: [''],
      joined: [''],
      workedTill: [''],
      current: [false],
      responsblities1: [''],
      responsblities2: [''],
    })
    this.myExperience.push(exps)
  }

  get myRefs() {
    return this.mainForm.get('refrences') as FormArray;
  }

  addRefs() {
    this.myRefs.push(this.fb.control(''));
  }

  get myLangs() {
    return this.mainForm.get('languages') as FormArray;
  }

  addLangs() {
    this.myLangs.push(this.fb.control(''));
  }

  get personalGroup() {
    return this.mainForm.controls.personal
  }
  get nameField() {
    return this.mainForm.controls.personal.controls['name']
  }

  get emailField() {
    return this.mainForm.controls.personal.controls['email']
  }
  get phoneField() {
    return this.mainForm.controls.personal.controls['phone']
  }

  get linkedInField() {
    return this.mainForm.controls.personal.controls['linkedIn']
  }

  get addressGroup() {
    return this.mainForm.controls.address
  }

  get streetField() {
    return this.addressGroup.controls['street']
  }
  get cityField() {
    return this.addressGroup.controls['city']
  }
  get stateField() {
    return this.addressGroup.controls['state']
  }
  get countryField() {
    return this.addressGroup.controls['country']
  }
  get postalField() {
    return this.addressGroup.controls['postal']
  }
  get educationGroup() {
    return this.mainForm.controls.education
  }
  get higherGroup() {
    return this.educationGroup.controls.higher
  }
  get graduationGroup() {
    return this.educationGroup.controls.graduation
  }
  get postGraduationGroup() {
    return this.educationGroup.controls.postGraduation
  }

  get hSchool() {
    return this.higherGroup.controls['school']
  }
  get hYear() {
    return this.higherGroup.controls['year']
  }
  get hGrades() {
    return this.higherGroup.controls['grades']
  }
  get hClass() {
    return this.higherGroup.controls['class']
  }

  get gCollege() {
    return this.graduationGroup.controls['college']
  }
  get gYear() {
    return this.graduationGroup.controls['year']
  }
  get gGrades() {
    return this.graduationGroup.controls['grades']
  }

  get gDegree() {
    return this.graduationGroup.controls['degree']
  }

  get pCollege() {
    return this.postGraduationGroup.controls['college']
  }
  get pYear() {
    return this.postGraduationGroup.controls['year']
  }
  get pGrades() {
    return this.postGraduationGroup.controls['grades']
  }

  get pDegree() {
    return this.postGraduationGroup.controls['degree']
  }

  public class = ['PCM', 'PCB', 'COMMERCE', 'ARTS'];
  public graduate = ["B.Sc", "B.E.", "B.TECH", "B.Com", "B.A.", "BBA","BCA"]
  public postGraduate = ["M.SC", "M.E.", "M.TECH", "M.Com", "M.A.", "MBA","MCA"]


  submitForm() {
    //this.openPDF();
    this.saveDoc();

  }

  public openPDF(): void {
    let DATA: any = document.getElementById('htmlData');
    html2canvas(DATA).then((canvas) => {
      let fileWidth = 150;
      // let fileHeight = (canvas.height * fileWidth) / canvas.width ;
      let fileHeight = 310;
      const FILEURI = canvas.toDataURL('image/png');
      let PDF = new jsPDF('p', 'mm', 'a4');
      let position = 1;
      PDF.addImage(FILEURI, 'PNG', 5, position, fileWidth, fileHeight);
      const name = this.nameField.value;
      const fileName = name + '.pdf';
      PDF.save(fileName);
    });


  }
  public saveDoc(): void {
    var doc = new jsPDF();
    var nameSize = 28
    var headSize = 12
    var contentSize = 10
    var lastLine = 0;


    doc.setFontSize(nameSize);
    doc.text(this.nameField.value, 5, 10);

    doc.setFontSize(headSize);
    doc.text("Address", 5, 25)
    doc.setFontSize(contentSize);
    doc.text(this.streetField.value + ",", 5, 30);
    doc.text(this.cityField.value + ",", 5, 35);
    doc.text(this.stateField.value + ",", 5, 40);
    doc.text(this.postalField.value + ", " + this.countryField.value, 5, 45);

    doc.setFontSize(headSize);
    doc.text("Email", 70, 25)
    doc.setFontSize(contentSize);
    doc.text(this.emailField.value, 100, 25);

    doc.setFontSize(headSize);
    doc.text("Contact No.", 70, 30)
    doc.setFontSize(contentSize);
    doc.text(this.phoneField.value, 100, 30);


    if (this.linkedInField.value !== "") {
      doc.setFontSize(headSize);
      doc.text("LinkedIn", 70, 35)
      doc.setFontSize(contentSize);
      doc.text(this.linkedInField.value, 100, 35);
    }


    doc.line(0, 48, 250, 48)

    doc.setFontSize(headSize);
    doc.text("Education Qualifications", 5, 55)

    if (this.pDegree.value !== "" && this.pCollege !== "" && this.pGrades !== "", this.pYear !== "") {
      doc.setFontSize(contentSize);
      doc.text(this.pDegree.value + " - " + this.pYear.value, 5, 63);
      doc.text(this.pCollege.value, 70, 63);
      doc.text(this.pGrades.value , 70, 67);
    }


    doc.setFontSize(contentSize);
    doc.text(this.gDegree.value + " - " + this.gYear.value, 5, this.pDegree.value !== "" ? 72 : 63);
    doc.text(this.gCollege.value, 70, this.pDegree.value !== "" ? 72 : 63);
    doc.text(this.gGrades.value, 70, this.pDegree.value !== "" ? 77 : 67);

    doc.setFontSize(contentSize);
    doc.text("12th " + this.hClass.value + " - " + this.hYear.value, 5, this.pDegree.value !== "" ? 82 : 72);
    doc.text(this.hSchool.value, 70, this.pDegree.value !== "" ? 82 : 72);
    doc.text(this.hGrades.value , 70, this.pDegree.value !== "" ? 87 : 77);

    doc.line(0, this.pDegree.value !== "" ? 90 : 83, 250, this.pDegree.value !== "" ? 90 : 83)

    doc.setFontSize(headSize);
    doc.text("Experience ", 5, this.pDegree.value !== "" ? 99 : 89)
    doc.setFontSize(contentSize);
    lastLine = this.pDegree.value !== "" ? 99 : 89;

    for (let i of this.myExperience.value) {
      doc.text(i.joined + " - " + (i.current ? "present" : i.workedTill), 5, lastLine + 6);
      doc.text(i.position + " at " + i.orgnization, 70, lastLine + 6);
      lastLine = lastLine + 6;
    }

    doc.line(0, lastLine + 5, 250, lastLine + 5)
    lastLine = lastLine + 5;
    doc.text("Skills", 5, lastLine + 6);
    lastLine = lastLine + 6;
    for (let sk of this.mySkills.value) {
      doc.text(sk, 15, lastLine + 6);
      lastLine = lastLine + 6;
    }
    doc.line(0, lastLine + 5, 250, lastLine + 5)
    lastLine = lastLine + 5;

    doc.text("Technicall Skills", 5, lastLine + 6);
    lastLine = lastLine + 6;
    for (let sk of this.myTechSkills.value) {
      doc.text(sk, 15, lastLine + 6);
      lastLine = lastLine + 6;
    }

    doc.line(0, lastLine + 5, 250, lastLine + 5)
    lastLine = lastLine + 5;

    doc.text("Languages", 5, lastLine + 6);
    lastLine = lastLine + 6;
    for (let sk of this.myLangs.value) {
      doc.text(sk, 15, lastLine + 6);
      lastLine = lastLine + 6;
    }
    doc.line(0, lastLine + 5, 250, lastLine + 5)
    lastLine = lastLine + 5;

    doc.text("Hobbies", 5, lastLine + 6);
    lastLine = lastLine + 6;
    for (let sk of this.myHobbies.value) {
      doc.text(sk, 15, lastLine + 6);
      lastLine = lastLine + 6;
    }
    doc.line(0, lastLine + 5, 250, lastLine + 5)
    lastLine = lastLine + 5;

    doc.text("Refrence", 5, lastLine + 6);
    lastLine = lastLine + 6;

    for (let sk of this.myRefs.value) {
      doc.text(sk, 15, lastLine + 6);
      lastLine = lastLine + 6;
    }
    doc.line(0, lastLine + 5, 250, lastLine + 5)
    lastLine = lastLine + 5;

    const name = this.nameField.value;
    const fileName = name + '.pdf';
    doc.save(fileName)
  }



}
