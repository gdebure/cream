from users.models import Employee
from django.contrib import admin


from import_export.admin import ImportExportModelAdmin


class EmployeeAdmin(ImportExportModelAdmin):
    resource_class = Employee
    pass

admin.site.register(Employee)
