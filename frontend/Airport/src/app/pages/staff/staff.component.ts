import { Component, OnInit } from '@angular/core';
import { StaffService } from '../../service/staff.service';

@Component({
  selector: 'app-staff',
  templateUrl: './staff.component.html',
  styleUrl: './staff.component.css'
})
export class StaffComponent implements OnInit {

  list:any

  constructor(private staff:StaffService){}

  ngOnInit(): void {
    
  }

  getstaff(){
    this.staff.getAll().subscribe((data:any)=>{
      console.log(data);
      
    })
  }

  updateStaff(Sid:any){

  }

  deleteStaff(Sid:any){

  }

}
