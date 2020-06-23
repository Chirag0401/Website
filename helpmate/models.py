from django.db import models

# Create your models here.


#models for comps note.
class comp_sem3_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/comp_notes/comp_sem3_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='comp_sem3_note'
		verbose_name_plural='comp_sem3_notes'      


	def __str__(self):
		return self.filename


class comp_sem4_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/comp_notes/comp_sem4_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='comp_sem4_note'
		verbose_name_plural='comp_sem4_notes'      


	def __str__(self):
		return self.filename    

class comp_sem5_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/comp_notes/comp_sem5_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='comp_sem5_note'
		verbose_name_plural='comp_sem5_notes'      


	def __str__(self):
		return self.filename 

class comp_sem6_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/comp_notes/comp_sem6_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='comp_sem6_note'
		verbose_name_plural='comp_sem6_notes'      


	def __str__(self):
		return self.filename 

class comp_sem7_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/comp_notes/comp_sem7_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='comp_sem7_note'
		verbose_name_plural='comp_sem7_notes'      


	def __str__(self):
		return self.filename    


class comp_sem8_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/comp_notes/comp_sem8_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='comp_sem8_note'
		verbose_name_plural='comp_sem8_notes'      


	def __str__(self):
		return self.filename                              

#models for comps qp.
class comp_sem3_qp(models.Model):
    available=models.BooleanField(default=True)
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)
    ser_no=models.IntegerField()      
    subject=models.CharField(max_length=200,default='i')
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/comp_qp/comp_sem3_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
        verbose_name='comp_sem3_qp'
        verbose_name_plural='comp_sem3_qps'      


    def __str__(self):
        return self.filename   


class comp_sem4_qp(models.Model):
    available=models.BooleanField(default=True)
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)      
    subject=models.CharField(max_length=200,default='i')
    ser_no=models.IntegerField()
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/comp_qp/comp_sem4_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
        verbose_name='comp_sem4_qp'
        verbose_name_plural='comp_sem4_qps'      


    def __str__(self):
        return self.filename                  

class comp_sem5_qp(models.Model):
    available=models.BooleanField(default=True)
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)      
    subject=models.CharField(max_length=200,default='i')
    ser_no=models.IntegerField()
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/comp_qp/comp_sem5_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
        verbose_name='comp_sem5_qp'
        verbose_name_plural='comp_sem5_qps'      


    def __str__(self):
        return self.filename 

class comp_sem6_qp(models.Model):
    available=models.BooleanField(default=True)
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)      
    subject=models.CharField(max_length=200,default='i')
    ser_no=models.IntegerField()
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/comp_qp/comp_sem6_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
        verbose_name='comp_sem6_qp'
        verbose_name_plural='comp_sem6_qps'      

class comp_sem7_qp(models.Model):
    available=models.BooleanField(default=True)
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)      
    subject=models.CharField(max_length=200,default='i')
    ser_no=models.IntegerField()
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/comp_qp/comp_sem7_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
        verbose_name='comp_sem7_qp'
        verbose_name_plural='comp_sem7_qps'      


    def __str__(self):
        return self.filename     

    def __str__(self):
        return self.filename 

class comp_sem8_qp(models.Model):
    available=models.BooleanField(default=True)
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)      
    subject=models.CharField(max_length=200,default='i')
    ser_no=models.IntegerField()
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/comp_qp/comp_sem8_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
        verbose_name='comp_sem8_qp'
        verbose_name_plural='comp_sem8_qps'      


    def __str__(self):
        return self.filename                             


#models for IT note.
class IT_sem3_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/IT_notes/IT_sem3_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='IT_sem3_note'
		verbose_name_plural='IT_sem3_notes'      


	def __str__(self):
		return self.filename


class IT_sem4_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/IT_notes/IT_sem4_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='IT_sem4_note'
		verbose_name_plural='comp_sem4_notes'      


	def __str__(self):
		return self.filename    

class IT_sem5_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/IT_notes/IT_sem5_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='IT_sem5_note'
		verbose_name_plural='IT_sem5_notes'      


	def __str__(self):
		return self.filename 

class IT_sem6_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/IT_notes/IT_sem6_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='IT_sem6_note'
		verbose_name_plural='IT_sem6_notes'      


	def __str__(self):
		return self.filename 

class IT_sem7_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/IT_notes/IT_sem7_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='IT_sem7_note'
		verbose_name_plural='IT_sem7_notes'      


	def __str__(self):
		return self.filename    


class IT_sem8_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/IT_notes/IT_sem8_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='IT_sem8_note'
		verbose_name_plural='IT_sem8_notes'      


	def __str__(self):
		return self.filename                              

#models for IT qp.
class IT_sem3_qp(models.Model):
    available=models.BooleanField(default=True)
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)      
    ser_no=models.IntegerField()
    subject=models.CharField(max_length=200,default='i')
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/IT_qp/IT_sem3_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
        verbose_name='IT_sem3_qp'
        verbose_name_plural='IT_sem3_qp'      

    def __str__(self):
        return self.filename


class IT_sem4_qp(models.Model):
    available=models.BooleanField(default=True)
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)                
    ser_no=models.IntegerField()
    subject=models.CharField(max_length=200,default='i')
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/IT_qp/IT_sem4_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
        verbose_name='IT_sem4_qp'
        verbose_name_plural='comp_sem4_qp'      

    def __str__(self):
        return self.filename    

class IT_sem5_qp(models.Model):
    available=models.BooleanField(default=True)
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)                
    ser_no=models.IntegerField()
    subject=models.CharField(max_length=200,default='i')
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/IT_qp/IT_sem5_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
        verbose_name='IT_sem5_qp'
        verbose_name_plural='IT_sem5_qp'      


    def __str__(self):
        return self.filename 

class IT_sem6_qp(models.Model):
    available=models.BooleanField(default=True)
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)                
    ser_no=models.IntegerField()
    subject=models.CharField(max_length=200,default='i')
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/IT_qp/IT_sem6_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
        verbose_name='IT_sem6_qp'
        verbose_name_plural='IT_sem6_qp'      

    def __str__(self):
        return self.filename 

class IT_sem7_qp(models.Model):
    available=models.BooleanField(default=True)
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)                
    ser_no=models.IntegerField()
    subject=models.CharField(max_length=200,default='i')
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/IT_qp/IT_sem7_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
        verbose_name='IT_sem7_qp'
        verbose_name_plural='IT_sem7_qp'      


    def __str__(self):
        return self.filename    


class IT_sem8_qp(models.Model):
    available=models.BooleanField(default=True)
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)               
    ser_no=models.IntegerField()
    subject=models.CharField(max_length=200,default='i')
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/IT_qp/IT_sem8_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
        verbose_name='IT_sem8_note'
        verbose_name_plural='IT_sem8_notes'      


    def __str__(self):
        return self.filename           

#models for Mech notes.
class mech_sem3_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/mech_note/mech_sem3_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='mech_sem3_note'
		verbose_name_plural='mech_sem3_notes'      


	def __str__(self):
		return self.filename


class mech_sem4_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/mech_note/mech_sem4_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='mech_sem4_note'
		verbose_name_plural='mech_sem4_notes'      


	def __str__(self):
		return self.filename    

class mech_sem5_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/mech_note/mech_sem5_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='mech_sem5_note'
		verbose_name_plural='mech_sem5_notes'      


	def __str__(self):
		return self.filename 

class mech_sem6_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/mech_note/mech_sem6_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='mech_sem6_note'
		verbose_name_plural='mech_sem6_notes'      


	def __str__(self):
		return self.filename 

class mech_sem7_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/mech_note/mech_sem7_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='mech_sem7_note'
		verbose_name_plural='mech_sem7_notes'      


	def __str__(self):
		return self.filename    


class mech_sem8_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/mech_note/mech_sem8_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='mech_sem8_note'
		verbose_name_plural='mech_sem8_notes'      


	def __str__(self):
		return self.filename              

#models for Mech qp.
class mech_sem3_qp(models.Model):
    available=models.BooleanField(default=True)
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)                
    ser_no=models.IntegerField()
    subject=models.CharField(max_length=200,default='i')
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/mech_qp/mech_sem3_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
        verbose_name='mech_sem3_qp'
    verbose_name_plural='mech_sem3_qp'      


    def __str__(self):
        return self.filename


class mech_sem4_qp(models.Model):
    available=models.BooleanField(default=True)
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)                
    ser_no=models.IntegerField()
    subject=models.CharField(max_length=200,default='i')
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/mech_qp/mech_sem4_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
        verbose_name='mech_sem4_qp'
    verbose_name_plural='mech_sem4_qp'      


    def __str__(self):
        return self.filename    

class mech_sem5_qp(models.Model):
    available=models.BooleanField(default=True)
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)                
    ser_no=models.IntegerField()
    subject=models.CharField(max_length=200,default='i')
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/mech_qp/mech_sem5_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
        verbose_name='mech_sem5_qp'
        verbose_name_plural='mech_sem5_qp'      


    def __str__(self):
        return self.filename 

class mech_sem6_qp(models.Model):
    available=models.BooleanField(default=True)
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)                
    ser_no=models.IntegerField()
    subject=models.CharField(max_length=200,default='i')
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/mech_qp/mech_sem6_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
        verbose_name='mech_sem6_qp'
        verbose_name_plural='mech_sem6_qp'      


    def __str__(self):
        return self.filename 

class mech_sem7_qp(models.Model):
    available=models.BooleanField(default=True)
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)                
    ser_no=models.IntegerField()
    subject=models.CharField(max_length=200,default='i')
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/mech_qp/mech_sem7_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
        verbose_name='mech_sem7_qp'
        verbose_name_plural='mech_sem7_qp'      


    def __str__(self):
        return self.filename    


class mech_sem8_qp(models.Model):
    available=models.BooleanField(default=True)
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)                
    ser_no=models.IntegerField()
    subject=models.CharField(max_length=200,default='i')
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/mech_qp/mech_sem8_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
        verbose_name='mech_sem8_qp'
        verbose_name_plural='mech_sem8_qp'      

    def __str__(self):
        return self.filename                      

#models for civil notes.
class civil_sem3_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/civil_note/civil_sem3_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='civil_sem3_note'
		verbose_name_plural='civil_sem3_notes'      


	def __str__(self):
		return self.filename


class civil_sem4_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/civil_note/civil_sem4_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='civil_sem4_note'
		verbose_name_plural='civil_sem4_notes'      


	def __str__(self):
		return self.filename    

class civil_sem5_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/civil_note/civil_sem5_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='civil_sem5_note'
		verbose_name_plural='civil_sem5_notes'      


	def __str__(self):
		return self.filename 

class civil_sem6_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/civil_note/civil_sem6_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='civil_sem6_note'
		verbose_name_plural='civil_sem6_notes'      


	def __str__(self):
		return self.filename 

class civil_sem7_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/civil_note/civil_sem7_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='civil_sem7_note'
		verbose_name_plural='civil_sem7_notes'      


	def __str__(self):
		return self.filename    


class civil_sem8_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/civil_note/civil_sem8_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='ciivl_sem8_note'
		verbose_name_plural='civil_sem8_notes'      


	def __str__(self):
		return self.filename

#models for civil qps.
class civil_sem3_qp(models.Model):
    available=models.BooleanField(default=True) 
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)               
    ser_no=models.IntegerField()
    subject=models.CharField(max_length=200,default='i')
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/civil_qp/civil_sem3_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
        verbose_name='civil_sem3_qp'
        verbose_name_plural='civil_sem3_qps'      


    def __str__(self):
        return self.filename


class civil_sem4_qp(models.Model):
    available=models.BooleanField(default=True)
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)                
    ser_no=models.IntegerField()
    subject=models.CharField(max_length=200,default='i')
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/civil_qp/civil_sem4_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
        verbose_name='civil_sem4_qp'
        verbose_name_plural='civil_sem4_qps'      

    def __str__(self):
        return self.filename    

class civil_sem5_qp(models.Model):
    available=models.BooleanField(default=True)
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)                
    ser_no=models.IntegerField()
    subject=models.CharField(max_length=200,default='i')
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/civil_qp/civil_sem5_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
        verbose_name='civil_sem5_qp'
        verbose_name_plural='civil_sem5_qps'      


    def __str__(self):
        return self.filename 

class civil_sem6_qp(models.Model):
    available=models.BooleanField(default=True)
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)                
    ser_no=models.IntegerField()
    subject=models.CharField(max_length=200,default='i')
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/civil_qp/civil_sem6_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
        verbose_name='civil_sem6_qp'
        verbose_name_plural='civil_sem6_qp'      


    def __str__(self):
        return self.filename 

class civil_sem7_qp(models.Model):
    available=models.BooleanField(default=True)
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)                
    ser_no=models.IntegerField()
    subject=models.CharField(max_length=200,default='i')
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/civil_qp/civil_sem7_qp')
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
	    verbose_name='civil_sem7_qp'
	    verbose_name_plural='civil_sem7_qp'      


    def __str__(self):
	    return self.filename    


class civil_sem8_qp(models.Model):
    available=models.BooleanField(default=True)
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)                
    ser_no=models.IntegerField()
    subject=models.CharField(max_length=200,default='i')
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/civil_qp/civil_sem8_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
	    verbose_name='ciivl_sem8_qp'
	    verbose_name_plural='civil_sem8_qp'      


    def __str__(self):
	    return self.filename                                                    

#models for extc notes.
class extc_sem3_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/extc_note/extc_sem3_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='extc_sem3_note'
		verbose_name_plural='extc_sem3_notes'      


	def __str__(self):
		return self.filename


class extc_sem4_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/extc_note/extc_sem4_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='extc_sem4_note'
		verbose_name_plural='extc_sem4_notes'      


	def __str__(self):
		return self.filename    

class extc_sem5_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/extc_note/extc_sem5_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='extc_sem5_note'
		verbose_name_plural='extc_sem5_notes'      


	def __str__(self):
		return self.filename 

class extc_sem6_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/extc_note/extc_sem6_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='extc_sem6_note'
		verbose_name_plural='extc_sem6_notes'      


	def __str__(self):
		return self.filename 

class extc_sem7_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/extc_note/extc_sem7_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='extc_sem7_note'
		verbose_name_plural='extc_sem7_notes'      


	def __str__(self):
		return self.filename    


class extc_sem8_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/extc_note/extc_sem8_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='extc_sem8_note'
		verbose_name_plural='extc_sem8_notes'      


	def __str__(self):
		return self.filename

#models for extc notes.
class extc_sem3_qp(models.Model):
    available=models.BooleanField(default=True)      
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)            
    ser_no=models.IntegerField()
    subject=models.CharField(max_length=200,default='i')
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/extc_qp/extc_sem3_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
	    verbose_name='extc_sem3_qp'
	    verbose_name_plural='extc_sem3_qps'      


    def __str__(self):
        return self.filename


class extc_sem4_qp(models.Model):
    available=models.BooleanField(default=True)      
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)            	
    ser_no=models.IntegerField()
    subject=models.CharField(max_length=200,default='i')
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/extc_qp/extc_sem4_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
	    verbose_name='extc_sem4_qp'
	    verbose_name_plural='extc_sem4_qp'      


    def __str__(self):
	    return self.filename    

class extc_sem5_qp(models.Model):
    available=models.BooleanField(default=True) 
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)                     
    ser_no=models.IntegerField()
    subject=models.CharField(max_length=200,default='i')
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/extc_qp/extc_sem5_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
	    verbose_name='extc_sem5_qp'
	    verbose_name_plural='extc_sem5_qp'      


    def __str__(self):
	    return self.filename 

class extc_sem6_qp(models.Model):
    available=models.BooleanField(default=True) 
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)                     
    ser_no=models.IntegerField()
    subject=models.CharField(max_length=200,default='i')
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/extc_qp/extc_sem6_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
	    verbose_name='extc_sem6_qp'
	    verbose_name_plural='extc_sem6_qp'      


    def __str__(self):
	    return self.filename 

class extc_sem7_qp(models.Model):
    available=models.BooleanField(default=True)    
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)                  
    ser_no=models.IntegerField()
    subject=models.CharField(max_length=200,default='i')
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/extc_qp/extc_sem7_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
	    verbose_name='extc_sem7_qp'
	    verbose_name_plural='extc_sem7_qp'      


    def __str__(self):
        return self.filename    


class extc_sem8_qp(models.Model):
    available=models.BooleanField(default=True)     
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)                 
    ser_no=models.IntegerField()
    subject=models.CharField(max_length=200,default='i')
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/extc_qp/extc_sem8_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
	    verbose_name='extc_sem8_qp'
	    verbose_name_plural='extc_sem8_qp'      


    def __str__(self):
	    return self.filename        

#models for FE notes       
class FE_sem1_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/FE_note/FE_sem1_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='FE_sem1_note'
		verbose_name_plural='FE_sem1_notes'      


	def __str__(self):
		return self.filename     

class FE_sem2_note(models.Model):
	available=models.BooleanField(default=True)      
	ser_no=models.IntegerField()
	subject=models.CharField(max_length=200,default='i')
	filename=models.CharField(max_length=100)
	file=models.FileField(upload_to='media/Docs/FE_note/FE_sem2_notes') 
	slug=models.SlugField(max_length=50,db_index=True,unique=True) 

	class Meta:
		verbose_name='FE_sem2_note'
		verbose_name_plural='FE_sem2_notes'      


	def __str__(self):
		return self.filename  

#models for FE qp
class FE_sem1_qp(models.Model):
    available=models.BooleanField(default=True)
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)                           
    ser_no=models.IntegerField()
    subject=models.CharField(max_length=200,default='i')
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/FE_qp/FE_sem1_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
	    verbose_name='FE_sem1_qp'
	    verbose_name_plural='FE_sem1_qp'      


    def __str__(self):
	    return self.filename     

class FE_sem2_qp(models.Model):
    available=models.BooleanField(default=True) 
    is_subject_1=models.BooleanField(default=True)
    is_subject_2=models.BooleanField(default=True)
    is_subject_3=models.BooleanField(default=True)
    is_subject_4=models.BooleanField(default=True)
    is_subject_5=models.BooleanField(default=True)
    is_subject_6=models.BooleanField(default=True)
    is_subject_7=models.BooleanField(default=True)                          
    ser_no=models.IntegerField()
    subject=models.CharField(max_length=200,default='i')
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='media/Docs/FE_qp/FE_sem2_qp') 
    slug=models.SlugField(max_length=50,db_index=True,unique=True) 

    class Meta:
	    verbose_name='FE_sem2_qp'
	    verbose_name_plural='FE_sem2_qp'      


    def __str__(self):
	    return self.filename  

class branch(models.Model):
    name=models.CharField(max_length=300)

    def __str__(self):
        return self.name

class semester(models.Model):
    name=models.CharField(max_length=300)

    def __str__(self):
        return self.name

class user_upload_notes(models.Model):
    email=models.EmailField(max_length=300)
    branch=models.ForeignKey('branch',on_delete=models.SET_NULL,null=True)
    semester=models.ForeignKey('semester',on_delete=models.SET_NULL,null=True)
    ufile=models.FileField(upload_to='media/user_uploads')
    text=models.TextField()

    def __str__(self):
        return self.email        