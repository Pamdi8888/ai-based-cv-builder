import { AbstractControl, ValidationErrors } from '@angular/forms';

export function graduationYearValidator(control: AbstractControl): ValidationErrors | null {
  const year = control.value;
  if (!year) {
    return null; // Let required validator handle empty fields
  }

  const currentYear = new Date().getFullYear();
  const yearNumber = Number(year);

  if (!Number.isInteger(yearNumber) || yearNumber < 1900 || yearNumber > currentYear + 10) {
    return { invalidGraduationYear: true };
  }

  return null;
}