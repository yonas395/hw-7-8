# Created by yonas at 6/28/2022
Feature: selecting by department
  #

 #Scenario: User can select and search in a department
     #Given open amazon page
     #When Select AWS Courses department
     #Then Search for cloud practitioner
     #Then Verify AWS Courses department is selected

 #Scenario: User can select and search in a department
     #Given open amazon page
     #When Select department by courses
     #Then Search for cloud practitioner
     #Then Verify AWS Courses department is selected


  Scenario: User can select and search in a department
     Given open amazon page
     When Select department by audible
     Then Search for cloud practitioner
     Then Verify audible department is selected


  Scenario: user can hover over New Arrivals and see deals
    Given open amazon product B074TBCSC8
    Then  hover on New Arrivals
    Then  verify user see the deals