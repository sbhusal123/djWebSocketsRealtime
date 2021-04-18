from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.http import HttpResponse


from .models import Messages, Room

class RoomView(generic.DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    template_name = "room.html"
    model = Room

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        messages = Messages.objects.filter(room__id=self.kwargs.get('pk'))
        context['messages'] = messages
        return context

    def dispatch(self, request, *args, **kwargs):
        try:
            room = Room.objects.get(id=self.kwargs.get('pk'))
        except Exception:
            return HttpResponse("404 Room Not Found")

        if self.request.user in [room.user1, room.user2]:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse("500 Not allowed")
    
    
    