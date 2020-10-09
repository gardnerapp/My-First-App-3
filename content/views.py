from django.shortcuts import get_object_or_404, render
from .models import Essay

essayList = Essay.objects.order_by('-pub_date'[0:])

def home(request):
   latest_essays = essayList[:5]

   essay_url = Essay.essay
   context = {"latest_essays": latest_essays,
              "essay_url": essay_url,

              }
   return render(request, "content/home.html", context)

def essay(request, title):
        essay = get_object_or_404(Essay, pk=title)
        title = essay.title
        text = essay.essay.read()
        text = str(text)
        text = text[1:] #gets rid of bytes
        context = {"title": title,
                   "text": text,
        }
        return render(request, "content/essay.html", context)


def essayIndex(request):
    context = {"essayList" : essayList}
    return render(request,"content/essay_index.html", context)

# make the text for the body not red

