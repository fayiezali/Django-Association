from django.db import models
#
from django.contrib.auth.models import User # إستيراد اسم المستخدم
#
from django.urls import reverse  # To generate URLS by reversing URL patterns
#
from django.db.models.signals import post_save
from django.dispatch import receiver
#
from saving.models import *
#
from django_countries.fields import CountryField
#
from django.utils.text import slugify
#
from django.db.models.signals import post_save
#
#
#
# البيانات الشخصية
class PersonalData_MODEL(models.Model):
    # متغير لحفظ رموز الجنسية
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
# 
# 
# 
    PER_Association            = models.ForeignKey(AssociationData_MODEL           , on_delete=models.CASCADE       , blank=True  , null=True  , verbose_name="اسم الجمعية")
    PER_Customer               = models.OneToOneField(User                         , on_delete=models.CASCADE                                  , verbose_name="اسم المشترك")
    PER_Avialable              = models.BooleanField(default=True                  , db_index=True                  , blank=False , null=False , verbose_name="حالة المشترك_نشط")
    PER_Slug                   = models.SlugField(unique=True                      , db_index=True                  , blank=True  , null=False , verbose_name="الإسم التعريفي")
    PER_FirstName              = models.CharField(max_length=50                    , db_index=True                  , blank=False , null=False , verbose_name="الإسم الأول")
    PER_FatherName             = models.CharField(max_length=50                    , db_index=True                  , blank=False , null=False , verbose_name="إسم الاب")
    PER_GrandFatherName        = models.CharField(max_length=50                    , db_index=True                  , blank=False , null=False , verbose_name="إسم الجد")
    PER_FamilyName             = models.CharField(max_length=50                    , db_index=True                  , blank=False , null=False , verbose_name="إسم العائلة")
    PER_ImgePersonal           = models.ImageField(upload_to='PersonalData_Image/' , db_index=True                  , blank=False , null=False , verbose_name="الصورة الشخصية"      ,default='Default_Image.png')
    PER_IdNumber               = models.CharField(max_length=50                    , db_index=True                  , blank=False , null=False , verbose_name="رقم الهوية الشخصية")
    # PER_Nationality            = models.CharField(max_length=2                     , db_index=True                  , blank=False , null=False , verbose_name="الجنسية"             , choices=NATIONALITY_CHOICES, default=SAUDI)
    PER_Nationality            = CountryField(blank_label='(Selet Country)'        , db_index=True                  , blank=False , null=False , verbose_name="الجنسية")
    PER_Mobile                 = models.CharField(max_length=10                    , db_index=True                  , blank=False , null=False , verbose_name="الجوال")
    PER_SocialStatusStudent    = models.BooleanField(default=True                  , db_index=True                  , blank=False , null=False , verbose_name="الحالة الإجتماعية - موظف")
    PER_SocialStatusEmployee  = models.BooleanField(default=True                   , db_index=True                  , blank=False , null=False , verbose_name="الحالة الإجتماعية -  طالب")
    PER_Date_joined            = models.DateTimeField(                               db_index=True                  , auto_now_add=True,verbose_name="تاريخ الإنضمام للجمعية")
    #
    #
        # 'admin'عرض إسم الحقل في صفحة
    def __str__(self):
        return str(self.PER_Customer)
    #
    # 
    #
    class Meta: 
        verbose_name = 'Personal Data'
        #'admin'طريقة عرض  إسم المودل/الجدول في صفحة
        verbose_name_plural = 'Personals Data'
            # 'A-Z' ترتيب تصاعدي 
        ordering = ['PER_Customer' , '-PER_Nationality'] 
    #
    # 
    # # 'A-Z' ترتيب تصاعدي 
    # class Meta:
    #     ordering = ['PER_Customer' , '-PER_Nationality'] 
    #
    # 
    #
    # self , *args , **kwargs):بارمترات تقوم بإستقبال البيانات المرسلة من سجل المستخدم
    #  slugify(self.user.username:
    def save(self , *args , **kwargs):
        if not self.PER_Slug: # نفذ الكود أدناه "slug"في حالة عدم إستقبال بيانات من قبل المستخدم لحقل 
            self.PER_Slug = slugify(self.PER_Customer.username) # "slug" ضع إسم المستخدم في الحقل 
            super(PersonalData_MODEL , self).save(*args , **kwargs)
    #
    #
    #
    # PersonalData_MODEL
    @receiver(post_save , sender=User)
    def create_user_personal_data(sender, instance , created , **kwargs):
        if created:
            PersonalData_MODEL.objects.create(PER_Customer=instance)
    #
    #
    #
    ## Display Detail Record By: ID
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('PersonalData_MODEL-detail', args=[str(self.id)])
    # path('Personaldetailid/<int:pk>/'       , PersonalDetailViewID.as_view()   , name='PersonalData_MODEL-detail'),
    # <td><a href="{{ object_list_item.get_absolute_url }}">{{ object_list_item.ASS_NameAssociation }}</a> ({{object_list_item.ASS_Phone}})</td> <!-- This Link Is From The Database and usls.py File-->
    #
    
#
#
#
#
#
#
# البيانات المالية
class  FinancialData_MODEL(models.Model):
    # متغير لحفظ رموز طريقة الدقع'
    CASH     = 'CA'
    CHECK    = 'CH'
    TRANSFER = 'TR'
    # قائمة بطريقة الدفع/الاستلام 
    METHOD_PAYMENT_CHOICES = [
        (CASH,     'Cash'),
        (CHECK,    'Check'),
        (TRANSFER, 'Transfer'),
    ]
    # 
    # FIN_Association             = models.ForeignKey(AssociationData_MODEL , on_delete=models.CASCADE                                              , verbose_name="اسم الجمعية")
    FIN_Customer                = models.OneToOneField(User                  , on_delete=models.CASCADE                                              , verbose_name="اسم المشترك")
    FIN_ShareValue              = models.DecimalField(max_digits=8        , decimal_places=2         , db_index=True , blank=False  , null=False  , verbose_name="قيمة السهم")
    FIN_NumberShares            = models.IntegerField(default=1                                      , db_index=True , blank=False  , null=False  , verbose_name="عدد الأسهم")
    FIN_BankName                = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="إسم البنك")
    FIN_BankAccount             = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="الحساب البنكي - الآيبان")
    FIN_MethodPaymentCash       = models.BooleanField(default=True                                   , db_index=True , blank=False  , null=False  , verbose_name="طريقة سداد قيمة اﻷسهم _ نقدا")
    FIN_MethodPaymentCheck      = models.BooleanField(                                                 db_index=True , blank=False  , null=False  , verbose_name="طريقة سداد قيمة اﻷسهم _ شيك")
    FIN_MethodPaymentTransfer   = models.BooleanField(                                                 db_index=True , blank=False  , null=False  , verbose_name="طريقة سداد قيمة اﻷسهم _ حوالة")
    FIN_MethodPayment           = models.CharField(max_length=2                                      , db_index=True , blank=False  , null=False  , verbose_name="طريقة إستلام قيمة اﻷسهم"         , choices=METHOD_PAYMENT_CHOICES , default=CASH)    
    FIN_SalaryDisbursementDate  = models.DateField(                                                    db_index=True , blank=False  , null=False  , verbose_name="تاريخ صرف الراتب")
    FIN_DateShareReceived       = models.DateField(                                                    db_index=True , blank=False  , null=False  , verbose_name="تاريخ استلام اﻷسهم/المشاركات/المستحقات")
    # 
    # 'admin'عرض إسم الحقل في صفحة
    def __str__(self):
        return str(self.FIN_Customer)
    # 
    # 'Z-A' ترتيب تنازلي
    class Meta:
        ordering = ['FIN_Customer'] 
    #
    #
# 
# 
# 
# 
# 
# بينانات السكن
class  HousingData_MODEL(models.Model):
    # HOU_Association  = models.ForeignKey(AssociationData_MODEL  , on_delete=models.CASCADE                 ,verbose_name="اسم الجمعية")
    HOU_Customer     = models.OneToOneField(User                   , on_delete=models.CASCADE                 ,verbose_name="اسم المشترك")
    HOU_Region       = models.CharField(max_length=25           , db_index=True , blank=False , null=False ,verbose_name="المنطقة")
    HOU_City         = models.CharField(max_length=25           , db_index=True , blank=False , null=False ,verbose_name="المدينة")
    HOU_District     = models.CharField(max_length=25           , db_index=True , blank=False , null=False ,verbose_name="الحي")
    HOU_HomeAddress  = models.CharField(max_length=100          , db_index=True , blank=False , null=False ,verbose_name="عنوان المنزل")
    HOU_CurrentWork  = models.CharField(max_length=100          , db_index=True , blank=False , null=False ,verbose_name="العمل الحالي")
    HOU_WorkAddress  = models.CharField(max_length=100          , db_index=True , blank=False , null=False ,verbose_name="عنوان العمل")
    # 
    # 'admin'عرض إسم الحقل في صفحة
    def __str__(self):
        return str(self.HOU_Customer) 
    # 
    # 'Z-A' ترتيب تنازلي
    class Meta:
        ordering = ['HOU_Customer'] 
# 
# 
# 
# 
# 
# 
