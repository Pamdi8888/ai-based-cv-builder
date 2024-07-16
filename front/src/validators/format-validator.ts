import { AbstractControl, ValidatorFn } from '@angular/forms';

export function formatValidator(): ValidatorFn {
  return (control: AbstractControl): {[key: string]: any} | null => {
    const valid = control.value === 'professional' || control.value === 'casual';
    return valid ? null : {'invalidFormat': {value: control.value}};
  };
}