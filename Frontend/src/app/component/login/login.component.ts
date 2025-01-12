import { Component } from '@angular/core';
import { LoginService } from '../../service/login.service';  // Import AuthService
import { Router } from '@angular/router';  // To navigate after successful login
import {LoginInterface , LoginResponseInterface} from "../../interfaces/login-interface";
import { CookieService } from 'ngx-cookie-service';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {


  loginData: LoginInterface = { username: '', password: '' };  // Use LoginInterface for loginData
  errorMessage: string = '';  // To store login error messages
  loading: boolean = false;  // To show a loading indicator

  constructor(private authService: LoginService, private router: Router,public cookiesService: CookieService,) {}

  onSubmit(): void {
    this.loading = true;  // Show loading indicator
    this.authService.login(this.loginData).subscribe(  // Pass loginData as the argument
      (response:LoginResponseInterface) => {
        this.loading = false;  // Hide loading indicator
        console.log('Login successful:', response);

        this.cookiesService.set("access", response.access);
        this.cookiesService.set("refresh", response.refresh);


        this.router.navigate(['/home']);  // Redirect to home or home page
      },
      (error) => {
        this.loading = false;  // Hide loading indicator
        this.errorMessage = 'Invalid credentials. Please try again.';  // Show error message
        console.error('Login failed:', error);
      }
    );
  }


}
