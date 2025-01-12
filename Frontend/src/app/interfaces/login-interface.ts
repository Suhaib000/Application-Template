export interface LoginInterface {
  username: string;
  password: string;
}

export interface LoginResponseInterface{
  access: string;
  refresh: string;
}

export interface reset_pass_Interface {
  user:string;
  new_password: string;
  confirm_new_password: string;
}


