from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django import forms
from django.contrib.auth.decorators import permission_required
import random
from django.core.exceptions import ValidationError

templater = get_renderer('homepage')


@view_function
def process_request(request):
	params = {}
	class colorForm(forms.Form):
		print("+++++++++++++++++++")
		Color = forms.CharField(required=True, max_length=7, widget=forms.TextInput(attrs={'class': 'form-control'}))
		def clean(self):
			print("////////////////////")
			color = (self.cleaned_data.get('Color'))
			print(len(color))
			print(color[0])
			print(len(color))
			if len(color) < 7 :
				raise forms.ValidationError("Incorrect format, input must be 7 characters long and be in this format #RRGGBB")
			if color[0] != "#":
				print(color[0])
				print("////////////////////")
				raise forms.ValidationError("Incorrect format, input must start with # and be in this format #RRGGBB")
			for x in range(1,6):
				#print(color[x])
				if color[x] != "0" and color[x] != "1" and color[x] != "2" and color[x] != "3" and color[x] != "4" and color[x] != "5" and color[x] != "6" and color[x] != "7" and color[x] != "8" and color[x] != "9" and color[x] != "A" and color[x] != "B" and color[x] != "C" and color[x] != "D" and color[x] != "E" and color[x] != "F" and color[x] != "a" and color[x] != "b" and color[x] != "c" and color[x] != "d" and color[x] != "e" and color[x] != "f":
					print(color[x])
					raise forms.ValidationError("Incorrect format, input must only contain numbers 0-9 and letters a-f and be in this format #RRGGBB")
			return self.cleaned_data

	form = colorForm()

	# def clean(self):
	# 	cleaned_data = super(colorForm, self).clean()
	# 	originalColor = cleaned_data.get("Color")

	# 	if len(originalColor) > 6 or len(originalColor) < 6:
	# 		raise forms.ValidationError("Did not send for 'help' in the subject despite CC'ing yourself.")

	if request.method == 'POST':
		form = colorForm(request.POST)
		#clean(form)
		if form.is_valid():

		#ProdSpec = hmod.ProductSpecification()
			rrggbb = form.cleaned_data['Color']
			print("+++++++++++++++++++")
			rrggbb = rrggbb.strip('#')
			print(rrggbb)
		#else:
		#	form = colorForm()
		#	params['form'] = form
		#	#params['error'] = "<h2>Incorrect format, input must be in this format #RRGGBB</h2>"
		#	return templater.render_to_response(request, 'select.html', params)
#
			#raise forms.ValidationError("Did not send for 'help' in the subject despite CC'ing yourself.")

		
			return HttpResponseRedirect('/homepage/color/{}/'.format(rrggbb))

	params['form'] = form
	#params['error'] = ""
	return templater.render_to_response(request, 'select.html', params)

@view_function
def random_color(request):
	params = {}
	color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
	print("---------------------")
	print(color)
	params['color'] = color
	return templater.render_to_response(request, 'randomRGB.html', params)