from django.shortcuts import render
from django.core.mail import send_mail
from decouple import config
# from .models import Post
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import ListView 
from django.views.generic.edit import CreateView # new


def index(request):
	if request.method == 'POST':
		message_name  = request.POST['message-name']
		message_email = request.POST['message-email']
		# subject= request.POST['subject']
		tel=request.POST['tel']
		message = request.POST['message']

		#send mail
		#localhost server ---python -m smtpd -n -c DebuggingServer localhost:1025
		appointment_mail = (f'''
		                    ... Name:-     {message_name} 
		                    ... Phone:-    {tel}
		                    ... Email:-    {message_email}
		                    ... Message:-  {message}
		                    
		                    
		                    ''') 
 

		send_mail( 

          'Appointment Request',
          appointment_mail,
          message_email,
          ['kmrvinayak28@gmail.com'],
		    )
		
		return render(request, 'index.html', {'message_name': message_name })

	else:
		return render(request, 'index.html', {})


def contact(request):
	if request.method == 'POST':
		message_name  = request.POST['message-name']
		message_email = request.POST['message-email']
		subject= request.POST['subject']
		tel=request.POST['tel']
		
		message = request.POST['message']

		#send mail
		#localhost server ---python -m smtpd -n -c DebuggingServer localhost:1025

		appointment_mail = (f'''
		                    ... Name:-     {message_name} 
		                    ... Phone:-    {tel}
		                    ... Email:-    {message_email}
							
		                    ... Message:-  {message}
		                    
		                    
		                    ''') 
 

		send_mail( 

          'Appointment Request',
          appointment_mail,
          message_email,
          ['kmrvinayak28@gmail.com'],
		    )
		# send_mail( 
		#     'Message from ---- ' + message_name , #subject
		#     'Message --- '+ message + "\n " + 'Sender Email --- ' + message_email + "\n" + 'Subject ---'+ subject + "\n" + 'Tel --- ' + tel, #message
		#     message_email, #from email
		#     #['config(EMAIL_HOST_USER)' ] , #to mail, 2nd copy
		#     ['kmrvinayak28@gmail.com']

		#      )
		return render(request, 'contact.html', {'message_name': message_name })

	else:
		return render(request, 'contact.html', {})



def about(request):
	return render(request, 'about.html', {})


# def blog_single(request):
# 	return render(request, 'blog-single.html', {})


# def blog(request):
# 	return render(request, 'blog.html', {})


# def cases(request):
# 	return render(request, 'cases.html', {})


def services(request):
	return render(request, 'services.html', {})


# def cards(request):
# 	return render(request, 'cards.html', {})


def WebDevelopment(request):
    	return render(request, 'WebDevelopment.html', {})

def AI(request):
    	return render(request, 'AI.html', {})

def AppDevelopment(request):
    	return render(request, 'AppDevelopment.html', {})

def DigitalMarketing(request):
    	return render(request, 'DigitalMarketing.html', {})

def NetworkSecurity(request):
    	return render(request, 'NetworkSecurity.html', {})

def SoftwareDevelopment(request):
    	return render(request, 'SoftwareDevelopment.html', {})

def UI(request):
    	return render(request, 'UI.html', {})


def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'myapp/error_404.html', data)

	# Error 404 page




# def appointment(request):
# 	if request.method == 'POST':
# 		your_name = request.POST['your-name']
# 		your_phone = request.POST['your-phone']
# 		your_email = request.POST['your-email']
# 		your_address = request.POST['your-address']
# 		your_schedule = request.POST['your-schedule']
# 		your_time = request.POST['your-time']
# 		your_message = request.POST['your-message']
	
# 		appointment_mail = (f'''
# 		                    ... Name:-     {your_name} 
# 		                    ... Message:-  {your_message}
# 		                    ... Phone:-    {your_phone}
# 		                    ... Email:-    {your_email}
# 		                    ... Address:-  {your_address}
# 		                    ... Schedule:- {your_schedule}
# 		                    ... Time:-     {your_time}
# 		                    ''') 
 

# 		send_mail( 

#           'Appointment Request',
#           appointment_mail,
#           your_email,
#           ['kmrvinayak28@gmail.com'],
# 		    )
		   
# 		return render(request, 'appointment.html', {
# 		              'your_name' : your_name,
# 		              'your_phone' : your_phone,
# 		              'your_email' : your_email, 
# 		              'your_address' : your_address,
# 		              'your_schedule' : your_schedule,
# 		              'your_time' : your_time,
# 		              'your_message' : your_message,
# 		              })

# 	else:
# 		return render(request, 'appointment.html', {})


# # def booking(request):
# # 	return render(request, 'booking.html', {})



# def booking(request):
# 		args = {'user': request.user}
# 		return render(request, 'booking.html', args,{})


# class BlogListView(ListView): 
# 	model = Post
# 	template_name = 'booking.html'


# class BlogCreateView(CreateView): 
# 	model = Post
# 	template_name = 'post_new.html' 
# 	fields = '__all__'












