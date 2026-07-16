from django.shortcuts import render, redirect
from jadmin.models import Category
from jadmin.models import Clue
from django.http import JsonResponse
from .forms import DisplayFilterForm

board = {}
player_names = {}

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
            cat1 = form.cleaned_data['cat1'].id
            cat2 = form.cleaned_data['cat2'].id
            cat3 = form.cleaned_data['cat3'].id
            cat4 = form.cleaned_data['cat4'].id
            cat5 = form.cleaned_data['cat5'].id
            cat6 = form.cleaned_data['cat6'].id
            catname1 = form.cleaned_data['cat1'].name
            catname2 = form.cleaned_data['cat2'].name
            catname3 = form.cleaned_data['cat3'].name
            catname4 = form.cleaned_data['cat4'].name
            catname5 = form.cleaned_data['cat5'].name
            catname6 = form.cleaned_data['cat6'].name
            player1_name = form.cleaned_data['player1_name']
            player2_name = form.cleaned_data['player2_name']
            player3_name = form.cleaned_data['player3_name']
            player_names['player1_name'] = player1_name
            player_names['player2_name'] = player2_name
            player_names['player3_name'] = player3_name
            cats=[]
            cats.append(catname1)
            cats.append(catname2)
            cats.append(catname3)
            cats.append(catname4)
            cats.append(catname5)
            cats.append(catname6)

            cat_id = []
            cat_id.append(cat1)
            cat_id.append(cat2)
            cat_id.append(cat3)
            cat_id.append(cat4)
            cat_id.append(cat5)
            cat_id.append(cat6)
            cat_id.sort()

            print(cat_id)
            
            clues = Clue.objects.filter(category_id__in=cat_id).order_by('category_id','value')
            clue_num = 1
            cat_num = 1
            for c in clues:
                bkey = f"key_{clue_num}_{cat_num}"
                bdata = {'text':c.text, 'answer':c.answer, 'value':c.value}
                clue_num += 1
                if clue_num > 5:
                    clue_num = 1
                    cat_num += 1
                board[bkey] = bdata
            # print(board)
    
            context = {
                'cats':cats,
                'board':board,
                'player_names': player_names
            }
            print("-------------------------------------------")
            print(context)
            # 3. Render the success page directly with this context
            return render(request, 'wel_test.html', context)
    # 4. If it's a GET request (or form validation fails), render start.html (Notice: NO redirect here!)
    return render(request, 'start.html', context)

def new_category(request):
    return render(request, 'new_category.html')

def host(request):
    return render(request, 'host.html')  

def wel_test(request, context):
    if 1:
        return

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

def get_player_names(request):
        return JsonResponse({
            'player1_name': player_names['player1_name'],
            'player2_name': player_names['player2_name'],
            'player3_name': player_names['player3_name']
        })