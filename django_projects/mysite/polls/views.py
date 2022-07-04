from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# # function based view
# def index(request):
#     latest_question_list = Question.objects.all()
#     return render(request, "polls/index.html", {
#         "latest_question_list": latest_question_list 
#     })

# def detail(request, question_id):
#     # question = Question.objects.get(pk=question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {
#         'question': question
#     })

# def results(request, question_id):
#     """We will go to this view after executing vote view"""
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {
#         "question": question
#     })
    
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    # Here, we are going to get the user answer from the form (in polls/detail.html)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", { 
            "question": question,
            "error_message": "An answer was not provided"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save() # Save the current object state in the db
        
        # HttpResponseRedirect ensures that the user does not send the same
        # information twice
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
        