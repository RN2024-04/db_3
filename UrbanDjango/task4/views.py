from django.shortcuts import render
from django.views.generic import TemplateView



# Create your views here.
def platform_templates(request):
    game_dict = {'games': ["Cyperpunk 2077", "Mario", "Hitman"]}
    game_dict2 = {'games': ["Game of the year", "Old game", "Who kills Mark?"]}
    context = {
        'game_dict': game_dict,
        'game_dict2': game_dict2,

    }

    return render(request, 'fourth_task/platform.html', context)

def games_templates(request):
    game_dict = {'games': ["Cyperpunk 2077", "Mario", "Hitman"]}
    game_dict2 = {'games': ["Game of the year", "Old game", "Who kills Mark?"]}
    context = {
        'game_dict': game_dict,
        'game_dict2': game_dict2,

    }

    return render(request, 'fourth_task/games.html', context)

def cart_templates(request):
    return render(request, "fourth_task/cart.html")