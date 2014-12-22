from django.shortcuts import render, redirect
from coaches.models import Coach
from django import forms


class CoachForm(forms.ModelForm):
	class Meta:
		model = Coach


def coaches_list(request):
    coaches = Coach.objects.all()
    return render(request, 'coaches/list.html', {'coaches': coaches},)

def coach_item(request, coach_id):
    coach = Coach.objects.get(id=coach_id)
    return render(request, 'coaches/item.html', {'coach': coach},)

def coach_edit(request, coach_id):
	title = 'Edit coach'
	coach = Coach.objects.get(id=coach_id)
	if request.method == 'POST':
		form = CoachForm(request.POST, instance=coach)
		if form.is_valid():
			coach = form.save()
			return redirect('coach_edit', coach.id,)
	else:
		form = CoachForm(instance=coach)

	return render(request, 'coaches/edit.html',
		                   {'form': form,
		                    'title': title,
		                    'coach': coach})

def coach_new(request):
	title = 'Add new coach'
	if request.method == "POST":
		form = CoachForm(request.POST)
		if form.is_valid():
			coach = form.save()
			return redirect('coaches_list')
	else:
		form = CoachForm()
	return render(request, 'coaches/edit.html', {'form': form,
												 'title': title})

def coach_delete(request, coach_id):
	coach = Coach.objects.get(id=coach_id)
	coach.delete()
	return redirect('coaches_list')
