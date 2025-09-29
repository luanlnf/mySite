from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User

class PostModelTest(TestCase):
    def test_criacao_post(self):
        user = User.objects.create_user(username="testeuser", password="12345")
        post = Post.objects.create(
            title="Teste",
            content="Conteúdo de exemplo",
            author=user,
            slug="teste-post"
        )
        self.assertEqual(post.title, "Teste")
