from django.shortcuts import  render, redirect
from .forms import CsvModelForm, NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate 
from django.contrib.auth.decorators import login_required
from core.models import Teacher, Csv
import csv
from core import forms
from .resources import PersonResource

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("core:login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("core:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


# @login_required(login_url = 'login')
def homepage(request):
    
    data=Teacher.objects.all()
    context={'data' : data }

    return render(request,'homepage.html',context)



# def upload_file_view(request):
#     form = CsvModelForm(request.POST, request.FILES)
#     if form.is_valid():
#         form.save()
#         form = CsvModelForm()
#         # obj = Cvs.objects.get(activated=False)
#         # with open(obj.file_name.path, 'r') as f:
#         #     reader = csv.reader(f)

#         #     for i, row in enumetate(reader):
#         #         if i==0:
#         #             pass
#         #         else:
#         #             row = "".join(row)
#         #             row = row.replace(";"," ")
#         #             row = row.split()
#         #             first_name = row[0].upper() 
#         #             Teacher.objects.create(
#         #                 first_name = first_name,
#         #                 last_name = upper(row[1]), 
#         #                 profile_picture =  row[2],
#         #                 email = row[3],
#         #                 phone_number = row[4],
#         #                 room_number = row[5],
#         #                 Subject_1 = row[6],
#         #                 Subject_2 = row[7],
#         #                 Subject_3 = row[8],
#         #                 Subject_4 = row[9],
#         #                 Subject_5 = row[10],

#         #             )
            
#         #     obj.activated =True
#         #     obj.save()

#     return render(request, 'upload.html', {'form': form})

from tablib import Dataset

def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'upload.html')