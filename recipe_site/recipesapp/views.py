from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import PermissionDenied


from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, DeleteView, ListView
from recipesapp.forms import RecipeForm, UserCreatForm
from recipesapp.models import Recipe, RecipeCategory


class RegisterView(UserPassesTestMixin, CreateView):
    form_class = UserCreatForm
    template_name = 'recipesapp/register.html'
    success_url = reverse_lazy('recipesapp:recipesapp')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(request=self.request, user=user, backend='django.contrib.auth.backends.ModelBackend')

        return response

    def test_func(self):
        if self.request.user.is_authenticated:
            # messages.info(self.request, 'Вы уже авторизованы. Вы не можете посетить эту страницу.')
            raise PermissionDenied
        return True




class AboutMeView(LoginRequiredMixin,TemplateView):
    template_name = 'recipesapp/about_me.html'
    # raise_exeption = True



class UpdateAboutMeView(UpdateView):
    model = User
    fields = 'username', 'email', 'first_name', 'last_name'
    template_name = 'recipesapp/about_me_update.html'

    def get_success_url(self):
        return reverse("recipesapp:about_me")


class RecipesView(TemplateView):
    template_name = 'recipesapp/recipesapp.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = Recipe.objects.select_related('author').all()
        return context


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = 'title', 'description', 'instructions', 'cooking_time', 'ingredients','cover', 'recipe_category'
    success_url = reverse_lazy('recipesapp:recipesapp')

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipesapp/recipe_detail.html'
    context_object_name = 'recipe'


class UpdateRecipeView(LoginRequiredMixin, UpdateView):
    model = Recipe
    # form_class = RecipeForm
    fields = 'title', 'description', 'instructions', 'cooking_time', 'ingredients', 'cover', 'recipe_category'
    template_name_suffix = '_update_form'


    def get_success_url(self):
        return reverse("recipesapp:recipe_details", kwargs={"pk": self.object.pk})


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipesapp:recipesapp')

def logout_view(request):
    logout(request)
    return redirect(reverse('recipesapp:recipesapp'))


class CategoriesView(ListView):
    template_name = 'recipesapp/categories.html'
    context_object_name = 'categories'
    queryset = RecipeCategory.objects.prefetch_related('recipes').all()

class CategoriesDetailView(DetailView):
    model = RecipeCategory
    template_name = 'recipesapp/categories_detail.html'
    context_object_name = 'categories'







