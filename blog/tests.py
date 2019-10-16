import os

from django.contrib.auth.models import AnonymousUser, User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.utils import timezone

from .models import Post


class PostTest(TestCase):

    PHOTO_1 = SimpleUploadedFile(name='pobrane.jpg',
                                 content=open(os.path.join((os.path.dirname(__file__)),
                                                           'static\images\pobrane.jpg'), 'rb').read(),
                                 content_type='image/jpeg')

    PHOTO_2 = SimpleUploadedFile(name='pobrane2.jpg',
                                 content=open(os.path.join((os.path.dirname(__file__)),
                                                           'static\images\pobrane2.jpg'), 'rb').read(),
                                 content_type='image/jpeg')

    def setUp(self) -> None:
        self.user_johny = User.objects.create_user(
            username='Johny', email='johny@gmail.com', password='top_secret')
        self.user_barb = User.objects.create_user(
            username='Barb', email='ann@gmail.com', password='top_secret_2')

    def test_post_created(self):
        self.assertEqual(Post.objects.count(), 0)
        Post.objects.create(author=self.user_johny, title='Title 1', photo=PostTest.PHOTO_1,
                            published_date=timezone.now())
        self.assertEqual(Post.objects.count(), 1)


class CollectionTest(TestCase):

    def setUp(self) -> None:
        self.user_johny = User.objects.create_user(
            username='Johny', email='johny@gmail.com', password='top_secret')
        self.user_barb = User.objects.create_user(
            username='Barb', email='ann@gmail.com', password='top_secret_2')

    def test_collection_status_code(self):
        response= self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_collection_template(self):
        response = self.client.get('/')
        template = 'blog/collection.html'
        self.assertTemplateUsed(response, template)

    def test_post_list(self):
        Post.objects.create(author=self.user_johny, title='Title 0', photo=PostTest.PHOTO_1,
                            published_date=timezone.now())
        Post.objects.create(author=self.user_johny, title='Title 1', photo=PostTest.PHOTO_2,
                            published_date=timezone.now())
        Post.objects.create(author=self.user_barb, title='Title 2', photo=PostTest.PHOTO_1,
                            published_date=timezone.now())
        Post.objects.create(author=self.user_barb, title='Title 3', photo=PostTest.PHOTO_2,
                            published_date=timezone.now())
        correct_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        response = self.client.get('/')
        self.assertEqual(list(response.context[-1].get('posts')), list(correct_posts))


    def test_post_user_log_in_list(self):
        Post.objects.create(author=self.user_johny, title='Title 0', photo=PostTest.PHOTO_1,
                            published_date=timezone.now())
        Post.objects.create(author=self.user_johny, title='Title 1', photo=PostTest.PHOTO_2,
                            published_date=timezone.now())
        Post.objects.create(author=self.user_barb, title='Title 2', photo=PostTest.PHOTO_1,
                            published_date=timezone.now())
        Post.objects.create(author=self.user_johny, title='Title 3', photo=PostTest.PHOTO_2,
                            published_date=timezone.now())
        correct_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        response = self.client.get('/')
        self.assertEqual(list(response.context[-1].get('posts')), list(correct_posts))



