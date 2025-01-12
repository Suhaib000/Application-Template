import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {environment} from "../../environments/environment";
import {LoginInterface , reset_pass_Interface} from "../interfaces/login-interface";

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor(private http: HttpClient,){ }


  login(data: LoginInterface): Observable<any> {
    return this.http.post(`${environment.baseUrl}auth/jwt/create/`, data);
  }

}
