import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { VideoDataRequest } from '../models/api.model';

const URL = 'http://localhost';
const PORT = 5000;
const ROUT_SEARCH = '/search';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  constructor(private http: HttpClient) {}

  searchVideo(videoDataRequest: VideoDataRequest): void {
    this.http
      .post<void>(`${URL}:${PORT}${ROUT_SEARCH}`, videoDataRequest)
      .subscribe();
  }
}
