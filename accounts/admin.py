from django.contrib import admin
#
from django.contrib.auth.models import User # إستيراد اسم المستخدم
# 
from accounts.models import * #  استيراد كل المودل/الجداول من التطبيق المطلوب
#
#
#
#
#
#
# البيانات الشخصية
@admin.register(PersonalData_MODEL)
class PersonalData_admin(admin.ModelAdmin): # تم وراثة الكلاس ادمن من اجل عمل عليه تعديل/كستمايز
        FullName = {"PER_Slug": [
                        'PER_FirstName' , 
                        'PER_FatherName' ,
                        'PER_GrandFatherName' ,
                        'PER_FamilyName'
                        ]} # ملئ حقل السلاق تلقائياَمن بيانات حقل اﻷسم الاول+الاب+الجد+العائلة
        prepopulated_fields = FullName
#
#
#
#
#
#
# البيانات المالبة
admin.site.register(FinancialData_MODEL,)
#
#
#
#
#
#
# البيانات السكنة
admin.site.register(HousingData_MODEL)
# 
#
# 
# 
# 
