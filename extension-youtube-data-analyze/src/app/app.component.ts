import { Component, OnInit, inject } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { TranslocoService } from '@ngneat/transloco';
import { VideoDataRequest } from './models/api.model';
import { ApiService } from './services/api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent implements OnInit {
  private readonly apiService = inject(ApiService);
  private readonly translocoService = inject(TranslocoService);
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
    this.apiService.searchVideo({
      email: this.formSearch.value.email,
      search: this.formSearch.value.textSearch,
      language: this.translocoService.getActiveLang() as 'PT' | 'EN',
    } as VideoDataRequest);
  }

  newSearch(): void {
    this.searchDone = false;
    this.formSearch.reset();
  }
}
