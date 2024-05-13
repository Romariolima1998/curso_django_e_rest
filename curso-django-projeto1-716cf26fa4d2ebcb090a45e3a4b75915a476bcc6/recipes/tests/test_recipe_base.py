from recipes.models import Category, Recipe, User
from django.test import TestCase


class RecipeTestBase(TestCase):

    def make_category(self, name='Category'):
        return Category.objects.create(name=name)

    def make_author(self, username='username',
                    password='123456',
                    first_name='first_name',
                    last_name='last_name',
                    email='email@email.com'):

        return User.objects.create_user(
            username='username',
            password='123456',
            first_name=first_name,
            last_name=last_name,
            email=email
        )

    def make_recipe(self, category_data=None, author_data=None,
                    title='recipe title', description='recipe description',
                    slug='recipe-slug', preparation_time=10,
                    preparation_time_unit='minutos', servings=5,
                    servings_unit='porçao',
                    preparation_steps='recipe preparations steps',
                    preparation_steps_is_html=False, is_published=True):

        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}

        return Recipe.objects.create(
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published
        )
