from django.views import generic


class Home(generic.ListView):
    template_name = 'index.html'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return


class Galery(generic.ListView):
    template_name = 'portfolio.html'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return


class About(generic.ListView):
    template_name = 'about.html'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return


class Services(generic.ListView):
    template_name = 'services.html'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return


class Pricing(generic.ListView):
    template_name = 'pricing.html'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return


class Contact(generic.ListView):
    template_name = 'contact.html'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return
