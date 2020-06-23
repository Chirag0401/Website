from django.contrib import admin
# Register your models here.
from .models import FE_sem1_note,FE_sem2_note,FE_sem1_qp,FE_sem2_qp,comp_sem3_note,comp_sem4_note,comp_sem5_note,comp_sem6_note,comp_sem7_note,comp_sem8_note,comp_sem3_qp,comp_sem4_qp,comp_sem5_qp,comp_sem6_qp,comp_sem7_qp,comp_sem8_qp,IT_sem3_note,IT_sem4_note,IT_sem5_note,IT_sem6_note,IT_sem7_note,IT_sem8_note,IT_sem3_qp,IT_sem4_qp,IT_sem5_qp,IT_sem6_qp,IT_sem7_qp,IT_sem8_qp,mech_sem3_note,mech_sem4_note,mech_sem5_note,mech_sem6_note,mech_sem7_note,mech_sem8_note,mech_sem3_qp,mech_sem4_qp,mech_sem5_qp,mech_sem6_qp,mech_sem7_qp,mech_sem8_qp,civil_sem3_note,civil_sem4_note,civil_sem5_note,civil_sem6_note,civil_sem7_note,civil_sem8_note,civil_sem3_qp,civil_sem4_qp,civil_sem5_qp,civil_sem6_qp,civil_sem7_qp,civil_sem8_qp,extc_sem3_note,extc_sem4_note,extc_sem5_note,extc_sem6_note,extc_sem7_note,extc_sem8_note,extc_sem3_qp,extc_sem4_qp,extc_sem5_qp,extc_sem6_qp,extc_sem7_qp,extc_sem8_qp,user_upload_notes,semester,branch

class user_upload_notesAmin(admin.ModelAdmin):
    list_display =['email','branch','semester']

class FE_sem1_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class FE_sem2_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class FE_sem1_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class FE_sem2_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class comp_sem3_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class comp_sem4_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class comp_sem5_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class comp_sem6_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class comp_sem7_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class comp_sem8_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class comp_sem3_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class comp_sem4_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class comp_sem5_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class comp_sem6_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class comp_sem7_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class comp_sem8_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class IT_sem3_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class IT_sem4_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class IT_sem5_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class IT_sem6_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class IT_sem7_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class IT_sem8_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class IT_sem3_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class IT_sem4_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class IT_sem5_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class IT_sem6_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class IT_sem7_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class IT_sem8_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class mech_sem3_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class mech_sem4_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class mech_sem5_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class mech_sem6_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class mech_sem7_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class mech_sem8_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class mech_sem3_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class mech_sem4_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class mech_sem5_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class mech_sem6_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class mech_sem7_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class mech_sem8_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class civil_sem3_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class civil_sem4_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class civil_sem5_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class civil_sem6_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class civil_sem7_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class civil_sem8_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class civil_sem3_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class civil_sem4_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class civil_sem5_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class civil_sem6_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class civil_sem7_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class civil_sem8_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']    

class extc_sem3_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class extc_sem4_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class extc_sem5_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class extc_sem6_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class extc_sem7_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class extc_sem8_noteAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class extc_sem3_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class extc_sem4_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class extc_sem5_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class extc_sem6_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class extc_sem7_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']

class extc_sem8_qpAdmin(admin.ModelAdmin):
    list_display =[ 'filename','subject','ser_no']



admin.site.register(FE_sem1_note, FE_sem1_noteAdmin)
admin.site.register(FE_sem2_note, FE_sem2_noteAdmin)
admin.site.register(FE_sem1_qp, FE_sem1_qpAdmin)
admin.site.register(FE_sem2_qp, FE_sem2_qpAdmin)

admin.site.register(semester)
admin.site.register(branch)

admin.site.register(comp_sem3_note, comp_sem3_noteAdmin)
admin.site.register(comp_sem4_note, comp_sem4_noteAdmin)
admin.site.register(comp_sem5_note, comp_sem5_noteAdmin)
admin.site.register(comp_sem6_note, comp_sem6_noteAdmin)
admin.site.register(comp_sem7_note, comp_sem7_noteAdmin)
admin.site.register(comp_sem8_note, comp_sem8_noteAdmin)

admin.site.register(comp_sem3_qp, comp_sem3_qpAdmin)
admin.site.register(comp_sem4_qp, comp_sem4_qpAdmin)
admin.site.register(comp_sem5_qp, comp_sem5_qpAdmin)
admin.site.register(comp_sem6_qp, comp_sem6_qpAdmin)
admin.site.register(comp_sem7_qp, comp_sem7_qpAdmin)
admin.site.register(comp_sem8_qp, comp_sem8_qpAdmin)





admin.site.register(IT_sem3_note, IT_sem3_noteAdmin)
admin.site.register(IT_sem4_note, IT_sem4_noteAdmin)
admin.site.register(IT_sem5_note, IT_sem5_noteAdmin)
admin.site.register(IT_sem6_note, IT_sem6_noteAdmin)
admin.site.register(IT_sem7_note, IT_sem7_noteAdmin)
admin.site.register(IT_sem8_note, IT_sem8_noteAdmin)

admin.site.register(IT_sem3_qp, IT_sem3_qpAdmin)
admin.site.register(IT_sem4_qp, IT_sem4_qpAdmin)
admin.site.register(IT_sem5_qp, IT_sem5_qpAdmin)
admin.site.register(IT_sem6_qp, IT_sem6_qpAdmin)
admin.site.register(IT_sem7_qp, IT_sem7_qpAdmin)
admin.site.register(IT_sem8_qp, IT_sem8_qpAdmin)



admin.site.register(mech_sem3_note, mech_sem3_noteAdmin)
admin.site.register(mech_sem4_note, mech_sem4_noteAdmin)
admin.site.register(mech_sem5_note, mech_sem5_noteAdmin)
admin.site.register(mech_sem6_note, mech_sem6_noteAdmin)
admin.site.register(mech_sem7_note, mech_sem7_noteAdmin)
admin.site.register(mech_sem8_note, mech_sem8_noteAdmin)

admin.site.register(mech_sem3_qp, mech_sem3_qpAdmin)
admin.site.register(mech_sem4_qp, mech_sem4_qpAdmin)
admin.site.register(mech_sem5_qp, mech_sem5_qpAdmin)
admin.site.register(mech_sem6_qp, mech_sem6_qpAdmin)
admin.site.register(mech_sem7_qp, mech_sem7_qpAdmin)
admin.site.register(mech_sem8_qp, mech_sem8_qpAdmin)

admin.site.register(user_upload_notes,user_upload_notesAmin)

admin.site.register(civil_sem3_note, civil_sem3_noteAdmin)
admin.site.register(civil_sem4_note, civil_sem4_noteAdmin)
admin.site.register(civil_sem5_note, civil_sem5_noteAdmin)
admin.site.register(civil_sem6_note, civil_sem6_noteAdmin)
admin.site.register(civil_sem7_note, civil_sem7_noteAdmin)
admin.site.register(civil_sem8_note, civil_sem8_noteAdmin)

admin.site.register(civil_sem3_qp, civil_sem3_qpAdmin)
admin.site.register(civil_sem4_qp, civil_sem4_qpAdmin)
admin.site.register(civil_sem5_qp, civil_sem5_qpAdmin)
admin.site.register(civil_sem6_qp, civil_sem6_qpAdmin)
admin.site.register(civil_sem7_qp, civil_sem7_qpAdmin)
admin.site.register(civil_sem8_qp, civil_sem8_qpAdmin)


admin.site.register(extc_sem3_note, extc_sem3_noteAdmin)
admin.site.register(extc_sem4_note, extc_sem4_noteAdmin)
admin.site.register(extc_sem5_note, extc_sem5_noteAdmin)
admin.site.register(extc_sem6_note, extc_sem6_noteAdmin)
admin.site.register(extc_sem7_note, extc_sem7_noteAdmin)
admin.site.register(extc_sem8_note, extc_sem8_noteAdmin)

admin.site.register(extc_sem3_qp, extc_sem3_qpAdmin)
admin.site.register(extc_sem4_qp, extc_sem4_qpAdmin)
admin.site.register(extc_sem5_qp, extc_sem5_qpAdmin)
admin.site.register(extc_sem6_qp, extc_sem6_qpAdmin)
admin.site.register(extc_sem7_qp, extc_sem7_qpAdmin)
admin.site.register(extc_sem8_qp, extc_sem8_qpAdmin)
