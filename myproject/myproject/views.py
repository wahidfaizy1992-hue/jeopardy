from django.shortcuts import render
from jadmin.models import Category
from jadmin.models import Clue
from django.http import JsonResponse
from .forms import DisplayFilterForm

board = {}

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def rules(request):
    return render(request, 'rules.html')

def start(request):
    form = DisplayFilterForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST': 
        if form.is_valid(): 
            # Extract the submitted, validated data 
            cat1 = form.cleaned_data['cat1']
            cat2 = form.cleaned_data['cat2']
            cat3 = form.cleaned_data['cat3']
            cat4 = form.cleaned_data['cat4']
            cat5 = form.cleaned_data['cat5']
            cat6 = form.cleaned_data['cat6'] 
            player1_name = form.cleaned_data['player1_name']
            player2_name = form.cleaned_data['player2_name']
            player3_name = form.cleaned_data['player3_name']
            context['cat1'] = cat1
            context['cat2'] = cat2
            context['cat3'] = cat3
            context['cat4'] = cat4
            context['cat5'] = cat5
            context['cat6'] = cat6
            context['player1_name'] = player1_name
            context['player2_name'] = player2_name
            context['player3_name'] = player3_name
            context['submitted'] = True
    return render(request, 'wel_test', context)

def new_category(request):
    return render(request, 'new_category.html')

def host(request):
    return render(request, 'host.html')  

def wel_test(request):
    categories = Category.objects.all().order_by('id')  # get categories
    # print(categories)
    cats=[]
    for c in categories:
        cats.append(c)
    query = "SELECT * from jadmin_clue WHERE category_id IN (1, 2, 3, 4, 5, 6) \
    ORDER BY category_id, value"
    clues = Clue.objects.raw(query)
    # board = {}
    clue_num = 1
    for c in clues:
        bkey = f"key_{clue_num}_{c.category_id}"
        bdata = {'text':c.text, 'answer':c.answer, 'value':c.value}
        clue_num=1 if clue_num==5 else clue_num+1
        board[bkey] = bdata
    # print(board)
    context = {
        'cats':cats,
        'board':board
    }
    return render(request, 'wel_test.html', context)

def get_clue_detail(request, clue_key):
        clue_key = "key_" + clue_key   # we only pass "1.1" or "4.5"
        print(clue_key)

        clue = board[clue_key]
        print(clue)
        return JsonResponse({
            'text': clue['text'],
            'value': clue['value'],
            'answer': clue['answer']
        })
