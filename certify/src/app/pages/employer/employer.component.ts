import { HttpErrorResponse } from '@angular/common/http';
import { Component, Input, OnInit } from '@angular/core';
import { User, Employer } from 'src/app/models/user';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-employer',
  templateUrl: './employer.component.html',
  styleUrls: ['./employer.component.css']
})
export class EmployerComponent implements OnInit {
  employer!: Employer;
  users!: User[];

  constructor(private userService: UserService) { }

  ngOnInit() {
    this.getUsers();
    this.getEmployer();
  }

  getEmployer(): void {
    this.userService.getEmployer().subscribe(
      (response: Employer) => {
        this.employer = response;
        console.log(this.employer);
      },
      (error: HttpErrorResponse) => {
        alert(error.message);
      }
    );
  }

  getUsers(): void {
    this.userService.getUsers().subscribe(
      (response: User[]) => {
        this.users = response;
        console.log(this.users);
      },
      (error: HttpErrorResponse) => {
        alert(error.message);
      }
    );
  }



  public searchUser(key: string): void {
    console.log(key);
    const results: User[] = [];
    for (const user of this.users) {
      if (user.firstname.toLowerCase().indexOf(key.toLowerCase()) !== -1
      || user.email.toLowerCase().indexOf(key.toLowerCase()) !== -1
      || user.phone !== -1
      || user.lastname.toLowerCase().indexOf(key.toLowerCase()) !== -1) {
        results.push(user);
      }
    }
    this.users = results;
    if (results.length === 0 || !key) {
      this.getUsers();
    }
  }

}
