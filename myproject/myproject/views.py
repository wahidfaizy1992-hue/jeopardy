from django.shortcuts import render, redirect
from jadmin.models import Category
from jadmin.models import Clue
from django.http import JsonResponse
from .forms import DisplayFilterForm, NewCategoryForm
from django.contrib.auth.decorators import login_required

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
            
            # list of category names
            cats=[]
            cats.append(catname1)
            cats.append(catname2)
            cats.append(catname3)
            cats.append(catname4)
            cats.append(catname5)
            cats.append(catname6)

            # list of category IDs
            cat_id = []
            cat_id.append(cat1)
            cat_id.append(cat2)
            cat_id.append(cat3)
            cat_id.append(cat4)
            cat_id.append(cat5)
            cat_id.append(cat6)
            print(cat_id)

            clue_num = 1
            cat_num = 1
            for cid in cat_id:
                clues = Clue.objects.filter(category_id=cid).order_by('value')
                print(clues)
                print("---------------------------------")
                for c in clues:
                    bkey = f"key_{clue_num}_{cat_num}"
                    bdata = {'text':c.text, 'answer':c.answer, 'value':c.value}
                    board[bkey] = bdata
                    clue_num += 1
                    if clue_num > 5:
                        clue_num = 1
                        cat_num += 1
                    
            # print(board)
            context = {
                'cats':cats,
                'board':board,
                'player_names': player_names
            }
            # print("-------------------------------------------")
            # print(context)
            # go to the gane board
            return render(request, 'wel_test.html', context)
    # Initial page load (GET request)
    return render(request, 'start.html', context)

@login_required
def new_category(request):
    print("In NEW CATEGORY VIEW")
    # form = NewCategoryForm(request.POST or None)
    # context = {'form': form}
    if request.method == 'POST':
        print("IN METHOD==POST") 
        # if form.is_valid():
        # get values and save to database
        category_name = request.POST.get('category_name')
        print(category_name)
        question_100 = request.POST.get('question_100')
        answer_100 = request.POST.get('answer_100')
        question_200 = request.POST.get('question_200')
        answer_200 = request.POST.get('answer_200')
        question_300 = request.POST.get('question_300')
        answer_300 = request.POST.get('answer_300')
        question_400 = request.POST.get('question_400')
        answer_400 = request.POST.get('answer_400')
        question_500 = request.POST.get('question_500')
        answer_500 = request.POST.get('answer_500')

        # check all fields filled in
        if category_name and question_100 and answer_100 and question_200 and answer_200 and \
            question_300 and answer_300 and question_400 and answer_400 and question_500 and answer_500:

            new_category, created = Category.objects.get_or_create(name=category_name)
            # Access the ID whether it was newly created or already existed
            new_category_id = new_category.id
            if created:
                new_clue1 = Clue.objects.create(category_id=new_category_id , text=question_100, 
                    answer=answer_100, value=100 )
                new_clue2 = Clue.objects.create(category_id=new_category_id , text=question_200, 
                    answer=answer_200, value=200 )
                new_clue3 = Clue.objects.create(category_id=new_category_id , text=question_300, 
                    answer=answer_300, value=300 )
                new_clue4 = Clue.objects.create(category_id=new_category_id , text=question_400, 
                    answer=answer_400, value=400 )
                new_clue5 = Clue.objects.create(category_id=new_category_id , text=question_500, 
                    answer=answer_500, value=500 )
            return redirect('home_view') 
        else:
            context = { 'error': 'Please fill out all fields' }
            return render(request, 'new_category.html', context )
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