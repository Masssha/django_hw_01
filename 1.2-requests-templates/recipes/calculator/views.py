from django.shortcuts import render
# from django.http import HttpResponse



DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def omlet(request):
    servings = int(request.GET.get("servings", 1))
    ings = {}
    for ing, number in DATA['omlet'].items():
        ings[ing] = round(number*servings, 2)
    context = {
        'recipe': ings
    }

    return render(request, 'calculator/index.html', context)

def pasta(request):
    servings = int(request.GET.get("servings", 1))
    ings = {}
    for ing, number in DATA['pasta'].items():
        ings[ing] = round(number*servings, 2)
    context = {
        'recipe': ings
    }

    return render(request, 'calculator/index.html', context)

def buter(request):
    servings = int(request.GET.get("servings", 1))
    ings = {}
    for ing, number in DATA['buter'].items():
        ings[ing] = round(number*servings, 2)
    context = {
        'recipe': ings
    }

    return render(request, 'calculator/index.html', context)


