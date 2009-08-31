from myproject.search.forms import SearchForm
from myproject.news.models import Entry

def search_site(request):
	form = SearchForm()
	items = []
	show_results = False
	if 'query' in request.GET:
		show_results = True
		query = request.GET['query'].strip()
		if query:
			form = SearchForm
			news = Entry.objects.filter(
				title__icontains=query
				)[:10]
	variables = RequestContext(request, {
			'form' : form,
			'news' : news,
			'show_results' : show_results
	})
	render_to_response('search/search.html', variables)

	

