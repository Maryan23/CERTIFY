import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Employer } from '../models/employer'
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class EmployerService {

  private baseUrl = 'http://localhost:8080/api/';

  constructor(private http: HttpClient) { }



  getEmployer(): Observable<Employer> {
    return this.http.get<Employer>(`${this.baseUrl}/employer`);
  }
}
