from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Club, Membership

def club_list(request):
	clubs = Club.objects.all()
	return render(request, 'clubs/club_list.html', {'clubs': clubs})

@login_required
def join_club(request, club_id):
	club = get_object_or_404(Club, id=club_id)
	membership, created = Membership.objects.get_or_create(user=request.user, club=club)
	if not created:
		messages.info(request, "Siz artıq bu kluba qoşulmusunuz.")
	else:
		messages.success(request, f"{club.name} klubuna qoşuldunuz!")
	return redirect('clubs')

@login_required
def my_clubs(request):
	memberships = Membership.objects.filter(user=request.user)
	return render(request, 'clubs/my_clubs.html', {'memberships': memberships})
