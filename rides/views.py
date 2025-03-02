from django.shortcuts import render, redirect
from .models import Person
from .forms import SearchForm, NewRideForm
from django.db.models import Q
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    return render(request, 'index.html', {
        'new_ride_form': NewRideForm()
    })

def ride_search(request):
    form = SearchForm()
    results = None

    if request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            origin = form.cleaned_data.get('origin', '').strip()
            destination_city = form.cleaned_data.get('destination_city', '').strip()
            destination_state = form.cleaned_data.get('destination_state', '').strip().upper()

            query = Q()
            
            # Build OR conditions
            if origin:
                query |= Q(origination__icontains=origin)
            if destination_city:
                query |= Q(destination_city__icontains=destination_city)
            if destination_state:
                query |= Q(destination_state__iexact=destination_state)

            # Search if at least one field is filled
            if query:  # This will be empty if no fields were filled
                results = Person.objects.filter(query).order_by(
                    '-taking_passengers',
                    '-seats_available'
                )

    return render(request, "rides.html", {
        "form": form,
        "results": results
    })

def create(request):
    if request.method == "POST":
        new_ride = NewRideForm(request.POST)
        if new_ride.is_valid():
            try:
                ride = new_ride.save()
                messages.success(request, 'Thank you! Your ride has been successfully added.')
                # Return a fresh form
                return redirect('rides:create')
            except Exception as e:
                print(f"Error saving ride: {str(e)}")  # Debug print
                messages.error(request, f'Error saving ride: {str(e)}')
        else:
            print("Form errors:", new_ride.errors)  # Debug print
            error_messages = []
            for field, errors in new_ride.errors.items():
                error_messages.append(f"{field}: {', '.join(errors)}")
            messages.error(request, 'Please correct the following errors: ' + '; '.join(error_messages))
    
    # Always provide a fresh form
    new_ride = NewRideForm()
    return render(request, 'create.html', {
        'new_ride_form': new_ride
    })

def rides(request):
    print("DEBUG: Rendering rides page")  # Add this debug print
    form = SearchForm()
    return render(request, 'rides.html', {'form': form})
