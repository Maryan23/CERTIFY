import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { User, Employer } from '../models/user'
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  private baseUrl = 'http://localhost:8080/api/';

  constructor(private http: HttpClient) { }



  getUser(): Observable<User> {
    return this.http.get<User>(`${this.baseUrl}/user`);
  }

  getUsers(): Observable<User[]> {
    return this.http.get<User[]>(`${this.baseUrl}/users`);
  }

  getEmployer(): Observable<Employer> {
    return this.http.get<Employer>(`${this.baseUrl}/employer`);
  }
}
