import { AbstractControl, ValidationErrors } from '@angular/forms';

export function passwordValidator(control: AbstractControl): ValidationErrors | null {
  const password = control.value;
  if (!password) {
    return null; // Let required validator handle empty fields
  }

  const minLength = 6;
  const hasUpperCase = /[A-Z]/.test(password);
  const hasLowerCase = /[a-z]/.test(password);
  const hasNumber = /[0-9]/.test(password);

  const errors: ValidationErrors = {};

  if (password.length < minLength) {
    errors['minLength'] = { requiredLength: minLength, actualLength: password.length };
  }
  if (!hasUpperCase) {
    errors['upperCase'] = true;
  }
  if (!hasLowerCase) {
    errors['lowerCase'] = true;
  }
  if (!hasNumber) {
    errors['number'] = true;
  }

  return Object.keys(errors).length ? errors : null;
}