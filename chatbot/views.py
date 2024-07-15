from django.shortcuts import render
from .forms import UserQueryForm
from .models import UserQuery
from meta_ai_api import MetaAI

def get_meta_ai_response(message):
    ai = MetaAI()
    prompt = f"{message}"
    response = ai.prompt(message=prompt)
    return response['message']

def chatbot_view(request):
    response = None
    if request.method == 'POST':
        form = UserQueryForm(request.POST)
        if form.is_valid():
            user_query = form.save(commit=False)
            user_query.user = request.user if request.user.is_authenticated else None
            user_query.response = get_meta_ai_response(user_query.query)
            user_query.save()
            response = user_query.response
    else:
        form = UserQueryForm()
    
    return render(request, 'chat.html', {'form': form, 'response': response, 'section':'chatbot'})
