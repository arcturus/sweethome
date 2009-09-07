from django.shortcuts import render_to_response
from sweethome.bpsweethome.models import SearchForm, searchProperties


def index(request):
        """
                Handles the entry point to the widget.
        """
        return render_to_response('index.bp', {})

def search(request):
        """
                Handle search post petition
        """
        #Only process post petitions
        if request.method == 'POST':
                form = SearchForm(request.POST)
                if form.is_valid():
                        #Ok now we know the data provided by the user is valid, so perform the query
                        try:
                                search_results = searchProperties(form)
                                return render_to_response('listing.bp', {'results' : search_results})
                        except Exception ,e:
                                pass
                        return None
        else:
                #Get request, return to the page
                form = SearchForm()

        return render_to_response('index.bp', {'form' : form})
