#formatovanie CTRL+ALT+L

# # L17
# numebers = [1,2,3]
# odd_nr = []
#
# for item in numbers:
#     if item %2 == 1:
#         odd_nr.append(item)
#
# numebers = [1,2,3]
# odd_nr = [for item in numbers if item %2 ==1]
#
# class Foo:
#     def __somtning(self):
#         print("a")
#
# f = Foo()
# f._Foo__something()
#
#
# # from Demos.security.lsastore import retrieveddata
# # from win32comext.mapi.emsabtags import PR_EMS_AB_LOCAL_INITIAL_TURN

# L11
class JobClassification:
    def __init__(self, job_classification: str, working_hours: int) -> None:
        self.job_classificaiton = job_classification
        self.working_hours = working_hours

    def AssignJobClassification(self) -> None:
        print(f"Pracovné zaradenienie: {self.job_classificaiton}")

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

# amendement requirements

class JobTenureProlonged:
    def __init__(self, prolonged_tenure: str, days: int) -> None:
        self.prolonged_tenure = prolonged_tenure
        self.days = days

    def set_reason(self) -> None:
        print(f"Dovod nepritomnosti je {self.prolonged_tenure}")

class Requirements:
    def __init__(self, reasons: list[JobTenureProlonged]) -> None:
        self.reasons = reasons

    def list_requirements(self):
        for reason in self.reasons:
            reason.set_reason()



class JobTenureShortened:
    def __init__(self, shortened_tenure:str, days: int) -> None:
        self.shortened_tenure = shortened_tenure
        self.days = days


reasons = [
    JobTenureProlonged(prolonged_tenure="ospravedlnená neprítomnosť zamestnanca", days=5),
    JobTenureProlonged(prolonged_tenure="neospravedlnená neprítomnosť zamestnanca", days=1),
    JobTenureProlonged(prolonged_tenure="výkon mimoriadnej služby", days=1),
    JobTenureProlonged(prolonged_tenure="výkon väzby alebo nepodmienečného trestu odňatia slobody", days=0)
]

requirements = Requirements(reasons=reasons)
# print(requirements)
requirements.list_requirements()

# #L7
# for i in range(4):
#     name_input = input("Please, choose a username: ")
#
#     try:
#         age_input = int(input("Please, enter your age: "))
#     except ValueError:
#         print("The age must be a number.")
#         continue  # skip to the next user