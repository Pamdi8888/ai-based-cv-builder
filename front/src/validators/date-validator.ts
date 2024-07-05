import { AbstractControl, ValidationErrors } from '@angular/forms';

export function dateValidator(control: AbstractControl): ValidationErrors | null {
  const value = control.value;
  if (!value) {
    return null; // Let required validator handle empty fields
  }

  const date = new Date(value);
  const today = new Date();

  if (isNaN(date.getTime())) {
    return { invalidDate: true };
  }

  if (date > today) {
    return { futureDate: true };
  }

  return null;
}