import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from "./component/login/login.component"
import { HomeComponent } from "./component/home/home.component"



const routes: Routes = [{ path: 'home', component: HomeComponent },
                        { path: 'login', component: LoginComponent },
                       ]

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
