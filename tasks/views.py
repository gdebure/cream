from django.shortcuts import render_to_response, get_object_or_404

from django.template import Context, loader
from tasks.models import Task
from django.http import HttpResponse



def index(request):
    tasks_list = Task.objects.all()
    t = loader.get_template('tasks/index.html')
    c = Context({
        'tasks_list': tasks_list,
    })
    return HttpResponse(t.render(c))



def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render_to_response('tasks/detail.html', {'task': task})