from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase
from unittest import skip


class RecipeViewTest(RecipeTestBase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', args=(1,)))
        self.assertIs(view.func, views.category)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', args=(1,)))
        self.assertIs(view.func, views.recipe)

    def test_recipe_home_view_return_status_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_category_view_return_404_if_recipes_not_found(self):
        response = self.client.get(reverse('recipes:category', args=(1,)))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_return_404_if_recipes_not_found(self):
        response = self.client.get(reverse('recipes:recipe', args=(1,)))
        self.assertEqual(response.status_code, 404)

    def test_recipe_home_view_loads_correct_temlplate(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'No recipes found here',
            response.content.decode('utf-8')
        )

    def test_recipe_home_templates_loads_recipes(self):
        self.make_recipe()

        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        context_recipes = response.context['recipes']

        self.assertIn('recipe title', content)
        self.assertIn('10 minutos', content)
        self.assertIn('5 porçao', content)
        self.assertEqual(len(context_recipes), 1)

    @skip('esse e apenas um modelo de exemplo')
    def test_for_test_fail(self):
        # if for exemple is test dont end
        self.fail('para que eu termine de digitalo')
        # skip test too
