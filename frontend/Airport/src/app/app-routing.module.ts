import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { NavigationComponent } from './navigation/navigation.component';
import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { StaffComponent } from './pages/staff/staff.component';

const routes: Routes = [
  {path:'', component:NavigationComponent,
    children:[
      
      {path:'staff',component:StaffComponent},
      {path:'dashboard', component:DashboardComponent},
    ]
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
