class ClinicManagement:
    def __init__(self):
        pass

    def DoctorInformation():
        file=open("doctor.json","r")
        f1=file.read(file)
        doc_info=json.loads(f1)
        return doc_info
        
    def addDoctor():

    def displayDoct():
    
    def addAppointment():

    def doctorSearchById():
    
    def doctorSearchBySpclzn():
    
    def doctorSearchByName():

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