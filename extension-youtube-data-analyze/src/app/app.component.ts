import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent implements OnInit {
  formSearch: FormGroup;

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

      email: new FormControl('', [Validators.required, Validators.email]),
    });
  }

  send(): void {
    console.log(this.formSearch.value);
  }
}
