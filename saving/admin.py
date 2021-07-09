# 
from django.contrib import admin
# 
from django.contrib.auth.models import User # إستيراد اسم المستخدم
# 
# 
from saving.models import * #  استيراد كل المودل/الجداول من التطبيق المطلوب
# 
#
# 
# 
# 
# 
"""Important Note:
(fields) & (fieldsets) This Properties Can Not Be Put Together
# Controlling Which fields are Displayed and Laid Out
# fields = [('ASS_NameAssociation', 'ASS_Slug' ), 'ASS_AssociationLogo' , 'ASS_Address' ,('ASS_Mobile' , 'ASS_Phone') , 'ASS_Email' , 'ASS_BankAccount']
"""
#
#
#
#
##########################################################################
# *** Add The Child Table Inside The Parent Table ***
# class FinancialDataInline(admin.TabularInline):
#     """Defines format of inline book insertion (used in AuthorAdmin)"""
#     model = FinancialData_MODEL
# #
# class HousingDataDataInline(admin.TabularInline):
#     """Defines format of inline book insertion (used in AuthorAdmin)"""
#     model = HousingData_MODEL
#
# class PersonalDataInline(admin.TabularInline):
#     """Defines format of inline book insertion (used in AuthorAdmin)"""
#     model = PersonalData_MODEL
##########################################################################
#
#
#
#
#
# 'admin' ظهور الجداول المطلوبة في صفحة 
# 
# بينات الجمعية
@admin.register(AssociationData_MODEL)
class AssociationData_admin(admin.ModelAdmin): # تم وراثة الكلاس ادمن من اجل عمل عليه تعديل/كستمايز
    # Automatically Fill In Slug Field From 
    prepopulated_fields = {'ASS_Slug':['ASS_NameAssociation']} 
    #
    #
    # Add aFilter Box
    list_filter = ('ASS_NameAssociation', 'ASS_Mobile' , 'ASS_BankAccount')
    #
    #
    # Show Fields a List
    list_display = ('ASS_NameAssociation', 'ASS_Slug' , 'ASS_AssociationLogo' , 'ASS_Address' ,  'ASS_Mobile' , 'ASS_Phone' , 'ASS_Email' , 'ASS_BankAccount')
    #
    #
    # Controlling Which fields are Displayed and Laid Out
    # fields       = [('ASS_NameAssociation', 'ASS_Slug' ), 'ASS_AssociationLogo' , 'ASS_Address' ,('ASS_Mobile' , 'ASS_Phone') , 'ASS_Email' , 'ASS_BankAccount']
    #
    #
    # Add Data In Different Sections
    fieldsets = (
        (None, {
            'fields': ('ASS_NameAssociation','ASS_Slug','ASS_AssociationLogo','ASS_Address','ASS_Mobile')
        }),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': ('ASS_Phone','ASS_Email','ASS_BankAccount')
        }),
    )

    # inlines = [PersonalDataInline]
# 
# 
# 
# # البيانات الشخصية
# @admin.register(PersonalData_MODEL)
# class PersonalData_admin(admin.ModelAdmin): # تم وراثة الكلاس ادمن من اجل عمل عليه تعديل/كستمايز
#         FullName = {"FER_Slug": [
#                             'PER_FirstName' , 
#                             'PER_FatherName' ,
#                             'PER_GrandFatherName' ,
#                             'PER_FamilyName'
#                             ]} # ملئ حقل السلاق تلقائياَمن بيانات حقل اﻷسم الاول+الاب+الجد+العائلة
#         prepopulated_fields = FullName
        
# 
# 
# 
# البيانات المالبة
# admin.site.register(FinancialData_MODEL,)
# 
# 
# 
# البيانات السكنة
# admin.site.register(HousingData_MODEL)
# 
#
# 
# 
# 
