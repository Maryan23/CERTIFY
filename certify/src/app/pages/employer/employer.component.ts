import { HttpErrorResponse } from '@angular/common/http';
import { Component, Input, OnInit } from '@angular/core';
import { Employer } from 'src/app/models/employer';
import { User } from 'src/app/models/user';
import { EmployerService } from 'src/app/services/employer.service';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-employer',
  templateUrl: './employer.component.html',
  styleUrls: ['./employer.component.css']
})
export class EmployerComponent implements OnInit {
  employer!: Employer;
  users!: User[];

  constructor(private employerService: EmployerService, private userService: UserService) { }

  ngOnInit() {
    this.getUser();
    this.getEmployer();
  }

  getEmployer(): void {
    this.employerService.getEmployer().subscribe(
      (response: Employer) => {
        this.employer = response;
        console.log(this.employer);
      },
      (error: HttpErrorResponse) => {
        alert(error.message);
      }
    );
  }

  getUser(): void {
    this.userService.getUser().subscribe(
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
      this.getUser();
    }
  }

}
