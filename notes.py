#formatovanie CTRL+ALT+L

# L17
numebers = [1,2,3]
odd_nr = []

for item in numbers:
    if item %2 == 1:
        odd_nr.append(item)

numebers = [1,2,3]
odd_nr = [for item in numbers if item %2 ==1]

class Foo:
    def __somtning(self):
        print("a")

f = Foo()
f._Foo__something()


# from Demos.security.lsastore import retrieveddata
# from win32comext.mapi.emsabtags import PR_EMS_AB_LOCAL_INITIAL_TURN

# L11
class JobClassification:
    def __init__(self, job_classification: str, working_hours: int) -> None:
        self.job_classificaiton = job_classification
        self.working_hours = working_hours

    def AssignJobClassification(self) -> None:
        print(f"Pracovné zaradenienie: {self.job.classification}")

    def AssignWorkingHours(self) -> None:
        print(f"Pracovný uväzok: {self.job.classification}")


job_title_1 = JobClassification(job_classification="Sociálny pracovník", working_hours=40)
job_title_2 = JobClassification(job_classification="Opatrovateľ", working_hours=20)
print(f"Pracovné zaradenie: {job_title_1.job_classificaiton}")
print(f"Pracovné zaradenie: {job_title_2.job_classificaiton}")
job_title_1.AssignJobClassification()
job_title_2.AssignJobClassification()


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