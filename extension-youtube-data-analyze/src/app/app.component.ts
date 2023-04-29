import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent implements OnInit {
  formSearch: FormGroup;
  searchDone = false;

  ngOnInit(): void {
    this.initForm();
  }

  private initForm(): void {
    this.formSearch = new FormGroup({
      textSearch: new FormControl('', [
        Validators.required,
        Validators.minLength(3),
        Validators.maxLength(100),
      ]),

      email: new FormControl('', [
        Validators.required,
        Validators.pattern(/^[a-z0-9.]+@[a-z0-9]+\.[a-z]+(\.[a-z]+)?$/i),
      ]),
    });
  }

  send(): void {
    this.searchDone = true;
  }

  newSearch(): void {
    this.searchDone = false;
    this.formSearch.reset();
  }
}
