import { AbstractControl, ValidatorFn } from '@angular/forms';

export function formatValidator(): ValidatorFn {
  return (control: AbstractControl): {[key: string]: any} | null => {
    const valid = control.value === '1' || control.value === '2';
    return valid ? null : {'invalidFormat': {value: control.value}};
  };
}