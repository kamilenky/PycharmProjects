# employee data
class EmployeeData:
    def ReturnEmployeeDataClass(self):
        print("EmployeeId")

class EmployeeName:
    def ReturnEmployeeName(self):
        print("Janko Hrasko")

class JobClassification:
    def __init__(self, job_classification: str, working_hours: int) -> None:
        self.job_classificaiton = job_classification
        self.working_hours = working_hours

    def AssignJobClassification(self) -> None:
        print(f"Pracovné zaradenienie: {self.job_classificaiton}")

    def AssignWorkingHours(self) -> None:
        print(f"Pracovný uväzok: {self.working_hours}")

job_title_1 = JobClassification(job_classification="Sociálny pracovník", working_hours=40)
job_title_2 = JobClassification(job_classification="Opatrovateľ", working_hours=20)

job_title_1.AssignJobClassification()
job_title_1.AssignWorkingHours()
job_title_2.AssignJobClassification()
job_title_2.AssignWorkingHours()

class EmployementType:
    def AssignEmployementType(self):
        print("Part-time")

class ContributionAmount:
    def SetFull(self):
        pass

    def SetReduced(self):
        pass

    def SetClassified(self):
        pass




# amendement requirements
class Requirements:
    pass

class ContractDuration:
    pass

class EmployeeSideObstacles:
    pass


# other

class ContractDates:
    pass



