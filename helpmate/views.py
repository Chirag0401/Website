from django.shortcuts import render,redirect
# Create your views here.
from .models import FE_sem1_note,FE_sem2_note,FE_sem1_qp,FE_sem2_qp,comp_sem3_note,comp_sem4_note,comp_sem5_note,comp_sem6_note,comp_sem7_note,comp_sem8_note,comp_sem3_qp,comp_sem4_qp,comp_sem5_qp,comp_sem6_qp,comp_sem7_qp,comp_sem8_qp,IT_sem3_note,IT_sem4_note,IT_sem5_note,IT_sem6_note,IT_sem7_note,IT_sem8_note,IT_sem3_qp,IT_sem4_qp,IT_sem5_qp,IT_sem6_qp,IT_sem7_qp,IT_sem8_qp,mech_sem3_note,mech_sem4_note,mech_sem5_note,mech_sem6_note,mech_sem7_note,mech_sem8_note,mech_sem3_qp,mech_sem4_qp,mech_sem5_qp,mech_sem6_qp,mech_sem7_qp,mech_sem8_qp,civil_sem3_note,civil_sem4_note,civil_sem5_note,civil_sem6_note,civil_sem7_note,civil_sem8_note,civil_sem3_qp,civil_sem4_qp,civil_sem5_qp,civil_sem6_qp,civil_sem7_qp,civil_sem8_qp,extc_sem3_note,extc_sem4_note,extc_sem5_note,extc_sem6_note,extc_sem7_note,extc_sem8_note,extc_sem3_qp,extc_sem4_qp,extc_sem5_qp,extc_sem6_qp,extc_sem7_qp,extc_sem8_qp,user_upload_notes
from .form import userForm

def home(request):
    form=userForm()
    if request.method == "POST":
        form=userForm(request.POST,request.FILES)
        if form.is_valid():
            myform=user_upload_notes(
                email=form.cleaned_data['email'],
                branch=form.cleaned_data['branch'],
                semester=form.cleaned_data['semester'],
                ufile=form.cleaned_data['ufile'],
                text=form.cleaned_data['text']
            )
            myform.save()
            return redirect('home')
    else:
        form=userForm()        
        return render(request,"index.html",{'form':form})

def FE_sem1_notev(request):
    notes=FE_sem1_note.objects.filter(available=True)
    context={
        'notes':notes,
    }
    return render(request,"fe sem1 notes.html",context)

def FE_sem2_notev(request):
    notes=FE_sem2_note.objects.filter(available=True)
    context={
        'notes':notes,
    }
    return render(request,"fe sem2 notes.html",context)

def FE_sem1_qpv(request):
    qp=FE_sem1_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }
    return render(request,"fe sem1 qps.html",context)

def FE_sem2_qpv(request):
    qp=FE_sem2_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }
    return render(request,"fe sem2 qps.html",context)  

#------------------------------------------------------------------------------------------------      

def comp_sem3_notev(request):
    notes=comp_sem3_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"comps sem3 notes.html",context)

def comp_sem8_notev(request):
    notes=comp_sem8_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"comps sem8 notes.html",context)

def comp_sem4_notev(request):
    notes=comp_sem4_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"comps sem4 notes.html",context)

def comp_sem5_notev(request):
    notes=comp_sem5_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"comps sem5 notes.html",context)

def comp_sem6_notev(request):
    notes=comp_sem6_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"comps sem6 notes.html",context)

def comp_sem7_notev(request):
    notes=comp_sem7_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"comps sem7 notes.html",context)

def comp_sem3_qpv(request):
    qp=comp_sem3_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"comps sem3 qps.html",context)

def comp_sem4_qpv(request):
    qp=comp_sem4_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"comps sem4 qps.html",context)    

def comp_sem5_qpv(request):
    qp=comp_sem5_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"comps sem5 qps.html",context)

def comp_sem6_qpv(request):
    qp=comp_sem6_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"comps sem6 qps.html",context)

def comp_sem7_qpv(request):
    qp=comp_sem7_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"comps sem3 qps.html",context)    

def comp_sem8_qpv(request):
    qp=comp_sem8_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"comps sem8 qps.html",context)    

# ------------------------------------------------------------------------------------------    
def civil_sem3_notev(request):
    notes=civil_sem3_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"civil sem3 notes.html",context)

def civil_sem4_notev(request):
    notes=civil_sem4_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"civil sem4 notes.html",context)

def civil_sem5_notev(request):
    notes=civil_sem5_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"civil sem5 notes.html",context)

def civil_sem6_notev(request):
    notes=civil_sem6_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"civil sem6 notes.html",context)

def civil_sem7_notev(request):
    notes=civil_sem7_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"civil sem7 notes.html",context)

def civil_sem8_notev(request):
    notes=civil_sem8_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"civil sem8 notes.html",context)

def civil_sem3_qpv(request):
    qp=civil_sem3_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"civil sem3 qps.html",context)

def civil_sem4_qpv(request):
    qp=civil_sem4_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"civil sem4 qps.html",context)

def civil_sem8_qpv(request):
    qp=civil_sem8_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"civil sem8 qps.html",context)

def civil_sem5_qpv(request):
    qp=civil_sem5_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"civil sem5 qps.html",context)

def civil_sem6_qpv(request):
    qp=civil_sem6_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"civil sem6 qps.html",context)

def civil_sem7_qpv(request):
    qp=civil_sem7_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"civil sem7 qps.html",context)

# ---------------------------------------------------------------------------------------------------
def extc_sem3_notev(request):
    notes=extc_sem3_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"extc sem3 notes.html",context)

def extc_sem4_notev(request):
    notes=extc_sem4_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"extc sem4 notes.html",context)
def extc_sem5_notev(request):
    notes=extc_sem5_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"extc sem5 notes.html",context)
def extc_sem6_notev(request):
    notes=extc_sem6_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"extc sem6 notes.html",context)
def extc_sem7_notev(request):
    notes=extc_sem7_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"extc sem7 notes.html",context)
def extc_sem8_notev(request):
    notes=extc_sem8_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"extc sem8 notes.html",context)
             
def extc_sem3_qpv(request):
    qp=extc_sem3_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"extc sem3 qps.html",context)

def extc_sem4_qpv(request):
    qp=extc_sem4_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"extc sem4 qps.html",context)
def extc_sem5_qpv(request):
    qp=extc_sem5_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"extc sem5 qps.html",context)

def extc_sem6_qpv(request):
    qp=extc_sem6_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"extc sem6 qps.html",context)

def extc_sem7_qpv(request):
    qp=extc_sem7_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"extc sem7 qps.html",context)

def extc_sem8_qpv(request):
    qp=extc_sem8_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"extc sem8 qps.html",context)

# ---------------------------------------------------------------------------------------
def mech_sem3_notev(request):
    notes=mech_sem3_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"mech sem3 notes.html",context)

def mech_sem4_notev(request):
    notes=mech_sem4_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"mech sem4 notes.html",context)
def mech_sem5_notev(request):
    notes=mech_sem5_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"mech sem5 notes.html",context)
def mech_sem6_notev(request):
    notes=mech_sem6_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"mech sem6 notes.html",context)
def mech_sem7_notev(request):
    notes=mech_sem7_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"mech sem7 notes.html",context)
def mech_sem8_notev(request):
    notes=mech_sem8_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"mech sem8 notes.html",context)
             
def mech_sem3_qpv(request):
    qp=mech_sem3_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"mech sem3 qps.html",context)

def mech_sem4_qpv(request):
    qp=mech_sem4_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"mech sem4 qps.html",context)
def mech_sem5_qpv(request):
    qp=mech_sem5_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"mech sem5 qps.html",context)

def mech_sem6_qpv(request):
    qp=mech_sem6_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"mech sem6 qps.html",context)

def mech_sem7_qpv(request):
    qp=mech_sem7_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"mech sem7 qps.html",context)

def mech_sem8_qpv(request):
    qp=mech_sem8_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"mech sem8 qps.html",context)

#-------------------------------------------------------------------------------------
def IT_sem3_notev(request):
    notes=IT_sem3_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"it sem3 notes.html",context)

def IT_sem4_notev(request):
    notes=IT_sem4_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"it sem4 notes.html",context)
def IT_sem5_notev(request):
    notes=IT_sem5_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"it sem5 notes.html",context)
def IT_sem6_notev(request):
    notes=IT_sem6_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"it sem6 notes.html",context)
def IT_sem7_notev(request):
    notes=IT_sem7_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"it sem7 notes.html",context)
def IT_sem8_notev(request):
    notes=IT_sem8_note.objects.filter(available=True)
    context={
        'notes':notes,
    }        
    return render(request,"it sem8 notes.html",context)
             
def IT_sem3_qpv(request):
    qp=IT_sem3_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"it sem3 qps.html",context)

def IT_sem4_qpv(request):
    qp=IT_sem4_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"it sem4 qps.html",context)
def IT_sem5_qpv(request):
    qp=IT_sem5_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"it sem5 qps.html",context)

def IT_sem6_qpv(request):
    qp=IT_sem6_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"it sem6 qps.html",context)

def IT_sem7_qpv(request):
    qp=IT_sem7_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"it sem7 qps.html",context)

def IT_sem8_qpv(request):
    qp=IT_sem8_qp.objects.filter(available=True)
    context={
        'qp':qp,
    }        
    return render(request,"it sem8 qps.html",context)
