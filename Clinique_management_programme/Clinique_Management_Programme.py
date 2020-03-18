class ClinicManagement:

    def __init__(self):
        pass

    def DoctorInformation(self):
        file=open("doctor.json","r+")
        f1=file.read(file)
        doc_info=json.loads(f1)
        return doc_info
        
    def addDoctor(self):
        docName=str(input("Enter the doctor Name:\n"))
        docId=int(input("Enter the Doctor ID:\n"))
        dSpcl=str(input(" Enter specialization: \n"))
        dAvil=str(input("Enter avilablity in (AM/PM/BOTH): \n"))
        file=open("doctor.json","r")
        f1=file.read()
        json_f=json.loads(f1)
        new_doc={"name":docName,"id":docId,"specialization":dSpcl,"availability": dAvil}
        file=open("doctor.json","w")
        json_f['doctor'].append(new_doc)
        file.write(json.dump(json_f,indent=2))
        print("Record Inserted Successfully")
    
    def displayDoct(self):
        count=0
        doct=self.DoctorInformation()
        doctors= doct['doctor']
        print(" Doctors Details \n Serial No \t\t Name \t\t\t\t\t Specialization ")
        for i in range(len(doctors)):
            name=doctors[i]['name']
            spcl=doctors[i]['spwcialization']
            count+=1
            print('',count,'\t\t',name ,'\t\t',spcl)

    def patientInformation(self):
        file=open("petients.json","r+")
        f=file.read() 
        json_pent=json.loads(f)
        f.case()
        return json_pent

    def appointment(self):
        file=open("appointment.json","r+")
        f1=file.read()
        json_app=json.loads(f1)
        f1.close()
        return json_app
    
    def addAppointment(self):
        doct=self.DoctorInformation()
        doctors=doct['doctors']
        for i in range(len(doctors)):
            name = doctors[i]['name']
            spclzn = doctors[i]['specialization']
            available = doctors[i]['availability']
            print(name, '    ', spclzn, '    ', available, '    ')
        doctName=input("Enter the Doctor Name")
        time = input("Availability time (AM/PM/BOTH)")
        appointmentDict = self.appointment()  
        appointmentList = appointmentDict[doctName] 
        print("Appointment list is ", appointmentList)
        if len(appointmentList) <=5:
            for i in range(len(doctors)):
                if doctors[i]["name"] == doctName:
                    if time.upper() == doctors[i]["availability"]:
                        print("Doctor is Available..!! Please Enter the patient details:")
                        name = input(" Enter pName:")
                        id = int(input(" Enter patient Id:"))
                        age = int(input(" Enter patient age:"))
                        mob_no = input(" Enter patient's pMobNumber:")
                        file=open('appointments.json','r')
                        f=file.read()
                        jsonfile=json.loads(f)
                        new_data = new_dict = {"pName": name, "Id": id, "pAge": age, "pMobNumber": mob_no, "Time": time}
                        file=open("appointments.json","a+")
                        jsonfile[doctors].append(new_data)
                        file.write(json.dumps(jsonfile,indent=2))
                        print("Your appointment is fixed. Thank You !")
                    else:
                        print("Sorry. Doctor is not available at the Moment !! ")

    def users(self):
        question=int(input("Press \n 1.Managment \n 2.Patient "))
        if question == 1:
            code=int(input("Enter the security code"))
            if code == 12345:
                choice = int(input("Press \n 1. Add doctor \n 2. View doctor \n 3. Go back\n"))
                if choice == 1:
                    self.addDoctor()
                    break
                if choice == 2:
                    self.displayDoct()
                    break
                if choice == 3:
                    yn == 3
            else:
                print("Wrong input")
        if question == 2:
            choice = int(input("Press \n 1. Add oppintment \n 2. search doctor \n 3. Go back"))
            if choice == 1:
                self.addAppointment()
                    break
            if choice == 2:
                option = int(input("Press \n 1. Seach by ID \n 2. Search by Specalization \n 3. Seach by Name\n"))
                if option == 1:
                    self.doctorSearchById()
                    break
                if option == 2:
                    self.doctorSearchBySpclzn()
                    break
                if option == 3:
                    self.doctorSearchByName()
                    break
            
if __name__ == '__main__':
    ClMg = ClinicManagement()
    patient = ClMg.patientInformation()
    appointment = ClMg.appointment()
    ClMg.Users()