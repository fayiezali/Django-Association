#try:
    # الكود الذي قد يتسبب في الخطأ
#except:
    # الكود الذي تريد تنفيذه لمعالجة الخطأ
#else:
    # الكود الذي تريد تنفيذه في حال عدم حدوث خطأ
#finally:
    # الكود الذي تريد تنفيذه سواء حدث خطأ/لم يحدث
from django.contrib.auth import models
#
from django.contrib.auth.models import User
#
from django.shortcuts import render , Http404 , redirect ,get_object_or_404
# 
from django.contrib import messages
#---------------------------------------------------------------------------------
from association.forms import * #  استيراد كل الفورم/النماذج من التطبيق المطلوب
# 
from association.models import * #  استيراد كل المودل/الجداول من التطبيق المطلوب
#---------------------------------------------------------------------------------
# 
# 
# 
# AssociationData - فانكشس/وظائف الجدول
# 
#************************************************************************************
# الصفحة الرئيسية- Index/Home
def  index_home_FUNCTION(request):
    try:# الكود الذي قد يتسبب في الخطأ
        pass
        # لا يوجد كود قد يتسبب في وقوع خطأ
    except:# الكود الذي تريد تنفيذه لمعالجة الخطأ
        template_name='page_not_found.html' # صفحة HTML التي سوف تظهر فيها البيانات المطلوبة
        return render(request, template_name)# إعادة إرسال: طلب المستخدم + الصفحة + المتغيرات إلى المتصفح  
    else:# الكود الذي تريد تنفيذه في حال عدم حدوث خطأ
        messages.info(request, 'Welcome To The Home Page.')#ظهور رسالة للمتسخدم
        template_name='index_home.html' # صفحة HTML التي سوف تظهر فيها البيانات المطلوبة
        return render(request, template_name)# إعادة إرسال: طلب المستخدم + الصفحة + المتغيرات إلى المتصفح  
    finally:# الكود الذي تريد تنفيذه سواء حدث خطأ/لم يحدث    
        pass
        # messages.info(request, 'Welcome to: Finally event.'')#ظهور رسالة للمتسخدم
#************************************************************************************
# 
#
#
#
#
#
#************************************************************************************
# All- الجمعية - إظهار البيانات - الكل
def association_data_show_all_FUNCTION(request): 
    context = {}# إنشاء ديكشنري/قاموس  لتخزين البيانات القادمة من النموذج فيه
    try:# الكود الذي قد يتسبب في الخطأ
        context["dataset_all"] = AssociationData_MODEL.objects.all().order_by("ASS_NameAssociation")#تخزين البيانات الموجودة في المودل/الجدول المطلوب مرتبة حسب الحقل المطلوب في الديكشنري/القاموس  
    except:# الكود الذي تريد تنفيذه لمعالجة الخطأ
        messages.success(request, 'No Records Found.')#ظهور رسالة للمتسخدم
        template_name='association_data_show_all.html' # صفحة HTML التي سوف تظهر فيها البيانات المطلوبة
        return render(request, template_name)# إعادة إرسال: طلب المستخدم + الصفحة + المتغيرات إلى المتصفح  
    else:# الكود الذي تريد تنفيذه في حالة عدم حدوث خطأ
            context["dataset_all"] = AssociationData_MODEL.objects.all().order_by("ASS_NameAssociation")#تخزين البيانات الموجودة في المودل/الجدول المطلوب مرتبة حسب الحقل المطلوب في الديكشنري/القاموس  
            return render(request, "association_data_show_all.html", context)# إعادة إرسال: طلب المستخدم + الصفحة + المتغيرات إلى المتصفح  
    finally:# الكود الذي تريد تنفيذه سواء حدث خطأ/لم يحدث    
        pass
        # messages.info(request, 'Welcome to: Finally event.'')#ظهور رسالة للمتسخدم
#************************************************************************************
# 
# 
#
#
#
#
#************************************************************************************
def association_data_show_details_id_FUNCTION(request,id):
    context = {}# إنشاء ديكشنري/قاموس  لتخزين البيانات القادمة من النموذج فيه
    try:# الكود الذي قد يتسبب في الخطأ
            context["dataset_id"] = AssociationData_MODEL.objects.get(id=id)#تخزين بيانات السجل المطلوب حسب معيار:(أي دي) المحدد في الديكشنري/القاموس  
    except:# الكود الذي تريد تنفيذه لمعالجة الخطأ
        messages.success(request, 'No Records Found.')#ظهور رسالة للمتسخدم
        template_name='association_data_show_details_id.html' # صفحة HTML التي سوف تظهر فيها البيانات المطلوبة
        return render(request, template_name)# إعادة إرسال: طلب المستخدم + الصفحة + المتغيرات إلى المتصفح  
    else:# الكود الذي تريد تنفيذه في حالة عدم حدوث خطأ
            context["dataset_id"] = AssociationData_MODEL.objects.get(id=id)#تخزين بيانات السجل المطلوب حسب:أي دي المحدد في الديكشنري/القاموس  
            return render(request, "association_data_show_details_id.html", context)# إعادة إرسال: طلب المستخدم + الصفحة + المتغيرات إلى المتصفح      
    finally:# الكود الذي تريد تنفيذه سواء حدث خطأ/لم يحدث    
        pass
        # messages.info(request, 'Welcome to: Finally event.'')#ظهور رسالة للمتسخدم
#************************************************************************************
# 
# 
# 
# 
# 
# 
#************************************************************************************
# slug- الجمعية - إظهار البيانات - تفاصيل
def association_data_show_details_slug_FUNCTION(request,slug):
    context = {}# إنشاء ديكشنري/قاموس  لتخزين البيانات القادمة من النموذج فيه
    try:# الكود الذي قد يتسبب في الخطأ
            context["dataset_slug"] = AssociationData_MODEL.objects.get(ASS_Slug=slug)#تخزين بيانات السجل المطلوب حسب معيار:(السلق) المحدد في الديكشنري/القاموس   
    except:# الكود الذي تريد تنفيذه لمعالجة الخطأ
        messages.success(request, 'No Records Found.')#ظهور رسالة للمتسخدم
        template_name='association_data_show_details_slug.html' # صفحة HTML التي سوف تظهر فيها البيانات المطلوبة
        return render(request, template_name)# إعادة إرسال: طلب المستخدم + الصفحة + المتغيرات إلى المتصفح    
    else:# الكود الذي تريد تنفيذه في حالة عدم حدوث خطأ
            context["dataset_slug"] = AssociationData_MODEL.objects.get(ASS_Slug=slug)#تخزين بيانات السجل المطلوب حسب معيار:(السلق) المحدد في الديكشنري/القاموس    
            return render(request, "association_data_show_details_slug.html", context)# إعادة إرسال: طلب المستخدم + الصفحة + المتغيرات إلى المتصفح        
    finally:# الكود الذي تريد تنفيذه سواء حدث خطأ/لم يحدث    
        pass
        # messages.info(request, 'Welcome to: Finally event.'')#ظهور رسالة للمتسخدم
#************************************************************************************
# 
# 
# 
# 
# 
# 
#************************************************************************************
def association_data_new_FUNCTION(request):
    context ={}# إنشاء ديكشنري/قاموس  لتخزين البيانات القادمة من النموذج فيه
    try:# الكود الذي قد يتسبب في الخطأ
        if request.method == 'POST':# جملة شرطية للتحقق من ان البيانات مشفرة
            association_data_form_new_VARIABLE = AssociationData_FORM(request.POST or None , request.FILES or None)#تخزين البيانات المدخلة في الفورم/النموذج في المتغير المطلوب
            if association_data_form_new_VARIABLE.is_valid():# التحقق من صحة البيانات
                association_data_form_new_VARIABLE.save()# حفظ البيانات في القاعدة
                messages.success(request, 'Operation Successful.')#ظهور رسالة للمتسخدم
                return redirect('/association_data_show_all')#إعادة توجيه المستخدم إلى الصفحة المطلوبة
    except:#الكود الذي تريد تنفيذه لمعالجة الخطأ
        messages.success(request, 'Failed To Add Record.')#ظهور رسالة للمتسخدم
        return redirect('/association_data_new')#إعادة توجيه المستخدم إلى الصفحة المطلوبة
    else:#الكود الذي تريد تنفيذه في حال عدم حدوث خط أ 
        association_data_form_new_VARIABLE = AssociationData_FORM()#إعادة تحميل النموذج مرة اخرى فارغ
        context['association_data_form_new']= association_data_form_new_VARIABLE #تحميل/تخزين البيانات المدخلة عن طريق الفورم/النموذج في ليست/قائمة لكي يتم ارسالها إلى صفحة أتش تي أم إل/html
        return render(request, "association_data_new.html", context)# إعادة إرسال: طلب المستخدم + الصفحة + المتغيرات إلى المتصفح        
    finally:# الكود الذي تريد تنفيذه سواء حدث خطأ/لم يحدث    
        pass
        # messages.info(request, 'Welcome to: Finally event.'')#ظهور رسالة للمتسخدم
#************************************************************************************
#
#
#
#
#
#
#************************************************************************************
# Update -  الجمعية -ابديت/تعديل 
def association_data_update_FUNCTION(request,id):
    try:# الكود الذي قد يتسبب في الخطأ
        context ={}# إنشاء ديكشنري/قاموس  لتخزين البيانات القادمة من النموذج فيه
        record_to_be_updated_VARIABLE = AssociationData_MODEL.objects.get(id=id)
    except:#الكود الذي تريد تنفيذه لمعالجة الخطأ
        messages.success(request, 'No Records Found.')#ظهور رسالة للمتسخدم
        template_name='association_data_show_details_id.html' # صفحة HTML التي سوف تظهر فيها البيانات المطلوبة
        return render(request, template_name)# إعادة إرسال: طلب المستخدم + الصفحة إلى المتصفح        
    else:#الكود الذي تريد تنفيذه في حال عدم حدوث خط أ         
        association_data_form_update_VARIABLE = AssociationData_FORM(request.POST or None, instance = record_to_be_updated_VARIABLE)#تخزين البيانات المدخلة في الفورم/النموذج في المتغير المطلوب
        if association_data_form_update_VARIABLE.is_valid():# التحقق من صحة البيانات
            association_data_form_update_VARIABLE.save()# حفظ البيانات في القاعدة
            messages.success(request, 'Operation Successful.')#ظهور رسالة للمتسخدم
            return redirect('/association_data_show_all')#إعادة توجيه المستخدم إلى الصفحة المطلوبة
        context["association_data_form_update"] = association_data_form_update_VARIABLE #تحميل/تخزين البيانات المدخلة عن طريق الفورم/النموذج في ليست/قائمة لكي يتم ارسالها إلى صفحة أتش تي أم إل/html
        return render(request, "association_data_update.html", context)# إعادة إرسال: طلب المستخدم + الصفحة + المتغيرات إلى المتصفح   
    finally:# الكود الذي تريد تنفيذه سواء حدث خطأ/لم يحدث    
        pass
        # messages.info(request, 'Welcome to: Finally event.'')#ظهور رسالة للمتسخدم
#************************************************************************************
# # Delete -  الجمعية ديليت/حذف 
def association_data_delete_FUNCTION(request,id):
    context ={}# إنشاء ديكشنري/قاموس  لتخزين البيانات القادمة من النموذج فيه
    try:# الكود الذي قد يتسبب في الخطأ
        record_to_be_delete_VARIABLE = AssociationData_MODEL.objects.get(id=id) #تخزين بيانات السجل المطلوب حسب معيار:(أي دي) المحدد في الديكشنري/القاموس      
    except:# الكود الذي تريد تنفيذه لمعالجة الخطأ
            messages.success(request, 'Operation Failed.')#ظهور رسالة للمتسخدم
            return redirect('/association_data_show_all')#إعادة توجيه المستخدم إلى الصفحة المطلوبة
    else:# الكود الذي تريد تنفيذه في حالة عدم حدوث خطأ
        record_to_be_delete_VARIABLE = AssociationData_MODEL.objects.get(id=id) #تخزين بيانات السجل المطلوب حسب معيار:(أي دي) المحدد في الديكشنري/القاموس  
        if request.method =="POST":# جملة شرطية للتحقق من ان البيانات مشفرة
            record_to_be_delete_VARIABLE.delete() # حذف السجل المطلوب
            messages.success(request, 'The Deletion Was Successful.')#ظهور رسالة للمتسخدم
            return redirect('/association_data_show_all')# إعادة توجيه المستخدم إلى الصفحة المطلوبة
        context["association_data_form_delete"] = record_to_be_delete_VARIABLE #تحميل/تخزين البيانات المدخلة عن طريق الفورم/النموذج في ليست/قائمة لكي يتم ارسالها إلى صفحة أتش تي أم إل/html    
        return render(request, "association_data_delete.html", context)#عرض نموذج حذف السجل على المستخدم لاتخاذ قرار حذف/التراجع عن الحذف    
    finally:# الكود الذي تريد تنفيذه سواء حدث خطأ/لم يحدث    
        pass
        # messages.info(request, 'Welcome to: Finally event.'')#ظهور رسالة للمتسخدم
# 
# 
# 
# 
# 
# 
# 
# 
#
#
#
#
#
#
#
#
#
# 
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
# 
# 
#
#
#
#
#
#
#
#
#
#
#
#
#