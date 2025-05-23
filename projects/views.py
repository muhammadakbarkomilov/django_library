from django.shortcuts import render
from .models import Project, Category

def portfolio_view(request):
    category_id = request.GET.get('category')
    categories = Category.objects.all()

    if category_id:
        projects = Project.objects.filter(categories__id=category_id)
    else:
        projects = Project.objects.all()

    context = {
        'categories': categories,
        'projects': projects,
        'selected_category': int(category_id) if category_id else None,
    }
    return render(request, 'index.html', context)