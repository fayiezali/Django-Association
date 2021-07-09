from typing import ClassVar
# 
from django.db import models
# 
from django.contrib.auth.models import User # إستيراد اسم المستخدم
# 
from django.urls import reverse  # To generate URLS by reversing URL patterns
#
# 
# 
#   
# 
# 
# بيانات الجمعية
class AssociationData_MODEL(models.Model):
    ASS_NameAssociation =   models.CharField(max_length=100                       , db_index=True , blank=False , null=False , verbose_name="إسم الجمعية"         ,help_text='هذا الحقل مخصص لإسم الجمعية')
    ASS_Slug            =   models.SlugField(unique=True                          , db_index=True , blank=False , null=False , verbose_name="الإسم التعريفي")
    ASS_AssociationLogo =   models.ImageField(upload_to='AssociationData_Image/'  , db_index=True , blank=False , null=False , verbose_name="شعار الجمعية"         ,default='Default_Image.png' )
    ASS_Address         =   models.CharField(max_length=250                       , db_index=True , blank=False , null=False , verbose_name="العنوان")
    ASS_Mobile          =   models.CharField(max_length=10                        , db_index=True , blank=False , null=False , verbose_name="الجوال")
    ASS_Phone           =   models.CharField(max_length=250                       , db_index=True , blank=False , null=False , verbose_name="الهاتف"               ,help_text='ضع مفتاح المدينة قبل الرقم مثال:012')
    ASS_Email           =   models.EmailField(max_length=250                      , db_index=True , blank=False , null=False , verbose_name="البريد الألكتروني")
    ASS_BankAccount     =   models.CharField(max_length=50                        , db_index=True , blank=False , null=False , verbose_name="الحساب البنكي - الآيبان" ,help_text='مثال: SA000000')
    # 
    # 'admin'عرض إسم الحقل في صفحة
    def __str__(self):
        return self.ASS_NameAssociation
    # 
    class Meta: 
        verbose_name = 'Association Data'
        #'admin'طريقة عرض  إسم المودل/الجدول في صفحة
        verbose_name_plural = 'Associations Data'
            # 'A-Z' ترتيب تصاعدي 
        ordering = ['ASS_NameAssociation' , '-ASS_Mobile'] 

    # 
    # # 'A-Z' ترتيب تصاعدي 
    # class Meta:
    #     ordering = ['ASS_NameAssociation' , '-ASS_Mobile'] 
    #
    #        
    ### Display Detail Record By: ID
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('AssociationData_MODEL-detail', args=[str(self.id)])
    # path('associationdetailid/<int:pk>/'       , AssociationDetailViewID.as_view()   , name='AssociationData_MODEL-detail'),
    # <td><a href="{{ object_list_item.get_absolute_url }}">{{ object_list_item.ASS_NameAssociation }}</a> ({{object_list_item.ASS_Phone}})</td> <!-- This Link Is From The Database and usls.py File-->
# 
# 
# 
# 
# 
# 
# # البيانات المالية
# class  FinancialData_MODEL(models.Model):
#     # متغير لحفظ رموز طريقة الدقع'
#     CASH     = 'CA'
#     CHECK    = 'CH'
#     TRANSFER = 'TR'
#     # قائمة بطريقة الدفع/الاستلام 
#     METHOD_PAYMENT_CHOICES = [
#         (CASH,     'Cash'),
#         (CHECK,    'Check'),
#         (TRANSFER, 'Transfer'),
#     ]
#     # 
#     FIN_Association             = models.ForeignKey(AssociationData_MODEL , on_delete=models.CASCADE                                              , verbose_name="اسم الجمعية")
#     FIN_Customer                = models.OneToOneField(User                  , on_delete=models.CASCADE                                              , verbose_name="اسم المشترك")
#     FIN_ShareValue              = models.DecimalField(max_digits=8        , decimal_places=2         , db_index=True , blank=False  , null=False  , verbose_name="قيمة السهم")
#     FIN_NumberShares            = models.IntegerField(default=1                                      , db_index=True , blank=False  , null=False  , verbose_name="عدد الأسهم")
#     FIN_BankName                = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="إسم البنك")
#     FIN_BankAccount             = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="الحساب البنكي - الآيبان")
#     FIN_MethodPaymentCash       = models.BooleanField(default=True                                   , db_index=True , blank=False  , null=False  , verbose_name="طريقة سداد قيمة اﻷسهم _ نقدا")
#     FIN_MethodPaymentCheck      = models.BooleanField(                                                 db_index=True , blank=False  , null=False  , verbose_name="طريقة سداد قيمة اﻷسهم _ شيك")
#     FIN_MethodPaymentTransfer   = models.BooleanField(                                                 db_index=True , blank=False  , null=False  , verbose_name="طريقة سداد قيمة اﻷسهم _ حوالة")
#     FIN_MethodPayment           = models.CharField(max_length=2                                      , db_index=True , blank=False  , null=False  , verbose_name="طريقة إستلام قيمة اﻷسهم"         , choices=METHOD_PAYMENT_CHOICES , default=CASH)    
#     FIN_SalaryDisbursementDate  = models.DateField(                                                    db_index=True , blank=False  , null=False  , verbose_name="تاريخ صرف الراتب")
#     FIN_DateShareReceived       = models.DateField(                                                    db_index=True , blank=False  , null=False  , verbose_name="تاريخ استلام اﻷسهم/المشاركات/المستحقات")
#     # 
#     # 'admin'عرض إسم الحقل في صفحة
#     def __str__(self):
#         return str(self.FIN_Customer)
#     # 
#     # 'Z-A' ترتيب تنازلي
#     class Meta:
#         ordering = ['FIN_Customer'] 
#     #
#     #
# # 
# # 
# # 
# # 
# # 
# # بينانات السكن
# class  HousingData_MODEL(models.Model):
#     HOU_Association  = models.ForeignKey(AssociationData_MODEL  , on_delete=models.CASCADE                 ,verbose_name="اسم الجمعية")
#     HOU_Customer     = models.OneToOneField(User                   , on_delete=models.CASCADE                 ,verbose_name="اسم المشترك")
#     HOU_Region       = models.CharField(max_length=25           , db_index=True , blank=False , null=False ,verbose_name="المنطقة")
#     HOU_City         = models.CharField(max_length=25           , db_index=True , blank=False , null=False ,verbose_name="المدينة")
#     HOU_District     = models.CharField(max_length=25           , db_index=True , blank=False , null=False ,verbose_name="الحي")
#     HOU_HomeAddress  = models.CharField(max_length=100          , db_index=True , blank=False , null=False ,verbose_name="عنوان المنزل")
#     HOU_CurrentWork  = models.CharField(max_length=100          , db_index=True , blank=False , null=False ,verbose_name="العمل الحالي")
#     HOU_WorkAddress  = models.CharField(max_length=100          , db_index=True , blank=False , null=False ,verbose_name="عنوان العمل")
#     # 
#     # 'admin'عرض إسم الحقل في صفحة
#     def __str__(self):
#         return str(self.HOU_Customer) 
#     # 
#     # 'Z-A' ترتيب تنازلي
#     class Meta:
#         ordering = ['HOU_Customer'] 
# # 
# # 
# # 
# # 
# # 
# # 
# # البيانات الشخصية
# class PersonalData_MODEL(models.Model):
#     # متغير لحفظ رموز الجنسية
#     SAUDI    = 'SA'
#     BAHRAIN  = 'BA'
#     OMAN     = 'OM'
#     QATAR    = 'QA'
#     KUWAIT   = 'KU'
#     EMIRATES = 'EM'
#     YEMEN    = 'YE'
#     NATIONALITY_CHOICES = [
#         (SAUDI,    'Saudi'),
#         (BAHRAIN,  'Bahrain'),
#         (OMAN,     'Oman'),
#         (QATAR,    'Qatar'),
#         (KUWAIT,   'Kuwait'),
#         (EMIRATES, 'Emirates'),
#         (YEMEN,    'Yemen'),
# ]
# # 
# # 
# # 
#     PER_Association            = models.ForeignKey(AssociationData_MODEL           , on_delete=models.CASCADE                 , verbose_name="اسم الجمعية")
#     PER_Customer               = models.OneToOneField(User                            , on_delete=models.CASCADE                 , verbose_name="اسم المشترك")
#     PER_Avialable              = models.BooleanField(default=True                  , db_index=True , blank=False , null=False , verbose_name="حالة المشترك_نشط")
#     FER_Slug                   = models.SlugField(unique=True                      , db_index=True , blank=True  , null=False , verbose_name="الإسم التعريفي")
#     PER_FirstName              = models.CharField(max_length=50                    , db_index=True , blank=False , null=False , verbose_name="الإسم الأول")
#     PER_FatherName             = models.CharField(max_length=50                    , db_index=True , blank=False , null=False , verbose_name="إسم الاب")
#     PER_GrandFatherName        = models.CharField(max_length=50                    , db_index=True , blank=False , null=False , verbose_name="إسم الجد")
#     PER_FamilyName             = models.CharField(max_length=50                    , db_index=True , blank=False , null=False , verbose_name="إسم العائلة")
#     PER_ImgePersonal           = models.ImageField(upload_to='PersonalData_Image/' , db_index=True , blank=False , null=False , verbose_name="الصورة الشخصية"      ,default='Default_Image.png')
#     PER_IdNumber               = models.CharField(max_length=50                    , db_index=True , blank=False , null=False , verbose_name="رقم الهوية الشخصية")
#     PER_Nationality            = models.CharField(max_length=2                     , db_index=True , blank=False , null=False , verbose_name="الجنسية"             , choices=NATIONALITY_CHOICES, default=SAUDI)
#     PER_Mobile                 = models.CharField(max_length=10                    , db_index=True , blank=False , null=False , verbose_name="الجوال")
#     PER_SocialStatusMarried    = models.BooleanField(default=True                  , db_index=True , blank=False , null=False , verbose_name="الحالة الإجتماعية - أعزب")
#     PER_SocialStatusUnmarried  = models.BooleanField(                                db_index=True , blank=False , null=False , verbose_name="الحالة الإجتماعية -متزوج")
#     PER_Date_joined            = models.DateTimeField(                               db_index=True , auto_now_add=True,verbose_name="تاريخ الإنضمام للجمعية")
# 
#
# 
# 
# 
# 
