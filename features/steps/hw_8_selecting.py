from behave import given, when, then

@given('open amazon product B074TBCSC8')
def open_amazon_product(context):
    context.app.hw8_department.open_amazon_product()


@then('hover on New Arrivals')
def hover_New_Arrivals(context):
    context.app.hw8_department.hover_New_Arrivals()


@then('verify user see the deals')
def verify_user_see_the_deals(context):
    context.app.hw8_department.verify_user_see_the_deals()



#@when('Select AWS Courses department')
#def Select_AWS_dept(context):
#    context.app.hw8_department.Select_AWS_dept()


#@then('Verify AWS Courses department is selected')
#def verify_dept(context):
#    context.app.hw8_department.verify_dept()


@when('Select department by {alias}')
def Select_AWS_dept(context, alias):
    context.app.hw8_department.Select_AWS_dept(alias)


#@then('Verify AWS Courses department is selected')
#def verify_dept(context):
#    context.app.hw8_department.verify_dept()


@then('Verify {department} department is selected')
def verify_dept(context, department):
    context.app.hw8_department.verify_dept(department)
