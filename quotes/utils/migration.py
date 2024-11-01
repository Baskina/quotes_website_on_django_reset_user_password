import os
import django
from bson import ObjectId

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotes.settings")
django.setup()

from quotesapp.models import Quote, Tag
from authorsapp.models import Author

uri = "mongodb+srv://admin:qwertyu@cluster0.upbkmny.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.authors


def seed_authors():
    authors = db.author.find()

    for author in authors:
        # author_obj = Author(fullname=author["fullname"], born_date=author["born_date"],
        #                     born_location=author["born_location"], description=author["description"])
        # author_obj.save()
        exist_author = bool(len(Author.objects.filter(fullname=author["fullname"])))

        if not exist_author:
            Author.objects.get_or_create(
                fullname=author.get("fullname"),
                born_date=author.get("born_date"),
                born_location=author.get("born_location"),
                description=author.get("description"),
            )


# def seed_tags():
#     quotes = db.quote.find()
#
#     for quote in quotes:
#         for tag in quote["tags"]:
#             Tag.objects.get_or_create(name=tag)
#
#
# seed_tags()


def seed_quotes():
    quotes = db.quote.find()

    for quote in quotes:
        tags = []
        for tag in quote["tags"]:
            t, *_ = Tag.objects.get_or_create(name=tag)
            tags.append(t)
        exist_quote = bool(len(Quote.objects.filter(quote=quote["quote"])))
        # quote_obj = Quote(quote=quote["quote"], tags=tags, author_id=quote["author"])
        # quote_obj.save()
        print(quote["author"], type(quote["author"]))
        if not exist_quote:
            author = db.author.find_one({"_id": quote["author"]})
            print('1', author)
            aut = Author.objects.get(fullname=author["fullname"]) if author is not None else None
            quot = Quote.objects.create(
                quote=quote["quote"],
                author=aut,
            )
            for tag in tags:
                quot.tags.add(tag)


seed_authors()
seed_quotes()
