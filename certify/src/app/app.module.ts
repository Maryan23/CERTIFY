import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { UserpageComponent } from './pages/userpage/userpage.component';
import { EmployerComponent } from './pages/employer/employer.component';

@NgModule({
  declarations: [
    AppComponent,
    UserpageComponent,
    EmployerComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
