import { AbstractControl, ValidationErrors } from '@angular/forms';

export function requiredFieldValidator(control: AbstractControl): ValidationErrors | null {
  const value = control.value;
  if (value === null || value === undefined || value === '') {
    return { required: true };
  }
  return null;
}