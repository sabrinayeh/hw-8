import csv

employees = [
  {
    "first_name": "Bill", 
    "last_name": "Lumbergh",
    "job_title": "Vice President",
    "hire_date": 1985,
    "performance_review": "excellent"
  }, {
    "first_name": "Michael", 
    "last_name": "Bolton",
    "job_title": "Programmer",
    "hire_date": 1995,
    "performance_review": "poor"
  }, {
    "first_name": "Peter", 
    "last_name": "Gibbons",
    "job_title": "Programmer",
    "hire_date": 1989,
    "performance_review": "poor"
  }, {
    "first_name": "Samir", 
    "last_name": "Nagheenanajar",
    "job_title": "Programmer",
    "hire_date": 1974,
    "performance_review": "fair"
  }, {
    "first_name": "Milton", 
    "last_name": "Waddams",
    "job_title": "Collator",
    "hire_date": 1974,
    "performance_review": "does he even work here?"
  }, {
    "first_name": "Bob", 
    "last_name": "Porter",
    "job_title": "Consultant",
    "hire_date": 1999,
    "performance_review": "excellent"
  }, {
    "first_name": "Bob", 
    "last_name": "Slydell",
    "job_title": "Consultant",
    "hire_date": 1999,
    "performance_review": "excellent"
  }
]





with open("tps_report2.csv", "w", newline="") as csvfile:

    fieldnames = ["first_name", "last_name", "job_title", "hire_date", "performance_review", "finished_review"]

    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

    writer.writeheader()


    for each_employee in employees:
        each_employee["finished_review"] = "yes"

    for each_employee in employees:
        if each_employee["first_name"] == "Bill" or each_employee["job_title"] == "Consultant":
           each_employee["performance_review"] = "poor"
        else:
           each_employee["performance_review"] = "excellent"
       
        writer.writerow(each_employee)