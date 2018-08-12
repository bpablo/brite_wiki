#from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SelectFieldForm, UploadFileForm
from django.views.generic import View
from .models import ObsRecords
#def Upload(request):
#    return HttpResponse("Upload Start Page")
class UploadView(View):
    def get(self, request):

        FormField = SelectFieldForm()
        file_upload_form = UploadFileForm()
        context = {
                    'FormField': FormField,
                    'file_upload_form': file_upload_form
                }
        return render(request, 'wiki/upload_field.html', context)

    def post(self, request):
        if request.method == 'POST':
         # necessary for post security
            FormField = SelectFieldForm(request.POST)#, request.FILES)
            file_upload_form = UploadFileForm(request.POST, request.FILES)
         # parse fileasj
            print (FormField.is_valid())
            print (file_upload_form.is_valid())
            print (file_upload_form.clean())
            print (file_upload_form['report'])
#            data=FileField.cleaned_data['report']
#            print("data", data)

#            print (request.FILES['report'].read())
        #    print(FileField['report'].read())
            if file_upload_form.is_valid():

    #            clean data
                report_file = file_upload_form.cleaned_data['report']
    #            print (report_file.read())
                data = report_file.read().decode("utf-8")#.split('\r\n')
                lines = data.split("\n")
                print (lines[0])
                lines = lines[1::]
                field_no = FormField['field'].value()
                for line in lines:
                    record = line.split(',')
                    print ("a single record", len(record))
                    if len(record) > 1:
                        record = ObsRecords().create_obsrecord(record=record,
                        field_no=field_no)
                        record.save()
    #            print ('report_file', report_file)
    #            print (FormField['field'].value())
    #            records = FileField.parse_file()
    #            records = request.Files['report'].read()
                return render(request, 'wiki/success.html')
            else:
                print ('false')
    #        if FormField.is_valid():
    #            handle_uploaded_file(request.FILES['file'])
    #            return HttpResponseRedirect('wiki/success.html')


            context = {
                        'FormField': FormField,
                        'file_upload_form': file_upload_form
                    }
            return render(request, 'wiki/upload_field.html', context)

        else:
            pass
        #form = UploadFieldForm()
