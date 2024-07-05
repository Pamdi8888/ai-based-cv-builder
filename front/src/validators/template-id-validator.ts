import { AbstractControl, ValidationErrors } from '@angular/forms';

export function templateIdValidator(control: AbstractControl): ValidationErrors | null {
  const templateId = control.value;
  if (!templateId) {
    return null; // Let required validator handle empty fields
  }

  if (!Number.isInteger(templateId) || templateId <= 0) {
    return { invalidTemplateId: true };
  }

  return null;
}