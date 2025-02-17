from datetime import datetime, timezone
from io import BytesIO

import requests
from django.contrib.auth import get_user_model
from django.core import management
from django.core.files.images import ImageFile
from django.core.management.base import BaseCommand
from wagtail.core.rich_text import RichText
from wagtail.images.models import Image

import home.models as models

User = get_user_model()


class Command(BaseCommand):

    def clear(self):
        models.BannerPage.objects.all().delete()
        models.BannerIndexPage.objects.all().delete()
        models.Article.objects.all().delete()
        models.Section.objects.all().delete()
        models.SectionIndexPage.objects.all().delete()
        Image.objects.all().delete()

    def create_image(self):
        response = requests.get('https://via.placeholder.com/729x576.png?text=Youth')

        title = 'youth_banner.jpg'
        image_file = ImageFile(BytesIO(response.content), name=title)

        return Image.objects.create(title=title, file=image_file)

    def create(self, owner, home):
        article = models.Article(
            title='Do you know the person adding you?',
            body=[('paragraph',
                   RichText('Someone sent me a friend request - but I don’t know this person, what should I do?'))],
            owner=owner,
            first_published_at=datetime.now(timezone.utc)
        )
        internet_safety = models.Section(
            title='Internet Safety',
            show_in_menus=True,
        )
        youth = models.Section(
            title='Youth',
            show_in_menus=True,
            color='1CABE2'
        )
        section_index_page = models.SectionIndexPage(title='Sections')
        
        home.add_child(instance=section_index_page)
        section_index_page.add_child(instance=youth)
        youth.add_child(instance=internet_safety)
        internet_safety.add_child(instance=article)

        models.FeaturedContent.objects.create(source=home, content=youth)

        banner_index_page = models.BannerIndexPage(title='Banners')
        home.add_child(instance=banner_index_page)

        image = self.create_image()

        banner_page = models.BannerPage(title='Youth', banner_image=image, banner_link_page=youth)
        banner_index_page.add_child(instance=banner_page)

        models.HomePageBanner.objects.create(source=home, banner_page=banner_page)

        footer_index_page = models.FooterIndexPage(title='Footers')
        home.add_child(instance=footer_index_page)

        footer = models.FooterPage(
            title='Footer1?',
            body=[('paragraph',
                   RichText('Footer1 paragraph1'))],
            owner=owner,
            first_published_at=datetime.now(timezone.utc)
        )
        footer_index_page.add_child(instance=footer)

    def handle(self, *args, **options):
        self.clear()
        self.stdout.write('Existing site structure cleared')

        owner = User.objects.first()
        home = models.HomePage.objects.first()
        if home:
            self.stdout.write(f"Home page found, title={home.title}")
            self.create(owner, home)
        else:
            self.stdout.write('No home page found. Quitting.')

        management.call_command('create_default_site')
