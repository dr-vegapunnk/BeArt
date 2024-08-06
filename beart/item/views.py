from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect
from .models import Item,Category
from django.db.models import Q
from .forms import newItemForm,EditItemForm
import logging

logging.basicConfig(level = logging.INFO)

logger = logging.getLogger('django')

# Create your views here.
def browse(request):
    item= Item.objects.filter(id_sold=False)
    query = request.GET.get('query','')
    category_id = request.GET.get('category',0)
    category = Category.objects.all()

    if query:
        item = Item.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    if category_id:
        item = Item.objects.filter(Category_id = category_id)
    return render(request,'item/browse.html',{
        'item': item,
        'query': query,
        'category':category,    
        'category_id':int(category_id),
    })
def detail(request,pk):
    item = get_object_or_404(Item,pk=pk)
    related_items = Item.objects.filter(Category =item.Category, id_sold=False).exclude(pk=pk)[0:6]
    return render (request,'item/detail.html',{
        'item': item,    
        'related_items': related_items,
    })

@login_required
def newItem(request):
    if request.method == 'POST':
        form = newItemForm(request.POST,request.FILES)

        if form.is_valid():
            item = form.save(commit = False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail',pk=item.id)
    else:
        form = newItemForm()

    return render (request,'item/newitem.html',{
        'form': form,
        'title': 'new Item'
    })

@login_required
def delete(request,pk):
    item = get_object_or_404(Item,pk=pk,created_by = request.user)
    item.delete()
    
    return redirect('dashboard:index')

@login_required
def editItem(request,pk):
    item = get_object_or_404(Item,pk=pk,created_by = request.user)
    logger.info(f"item is received {item}")

    if request.method == 'POST':
        logger.info("post request received")
        form = EditItemForm(request.POST,request.FILES,instance=item)

        if form.is_valid():
            logger.info("is valid")
            item = form.save(commit=False)
            item.save()
            logger.info("saving the form")
            return redirect('item:detail',pk=pk)
        else:
            print(form.errors)  # Debugging line
    else:
        form = EditItemForm(instance=item)
        logger.info("Form initialized with instance data")

    return render (request,'item/newitem.html',{
        'form': form,
    })