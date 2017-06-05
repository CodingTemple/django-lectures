from .models import Book
class BookRouter(router):
    def db_for_read(self,Book,**hints):
        if model._meta.app_label in ['bookstore_base','books']:
            return 'cs_books'
        return None


    def allow_migrate(self,db,model_name=None):
        if model._meta.app_label in ['bookstore_base','books']:
            return db == 'cs_books'
        return None

    def db_for_write(model,**hints):
        if model._meta.app_label in ['bookstore_base','books']:
            return 'cs_books'
        return None
