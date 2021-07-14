from category.models import Category


# the menu links will be available in all templates after setting it in settings
def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)
