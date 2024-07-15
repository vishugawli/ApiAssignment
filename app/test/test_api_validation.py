from app.utility.baseutility import Baseutility
import logging


class Testapivalidation(Baseutility):

    def test_validate(self, request_processor_user, request_processor_todo):
        val_a = request_processor_user
        val_b = request_processor_todo

        # Fetching value based on key comparison between two dictionaries
        for key in val_a:
            if key in val_b:
                logging.info(val_a[key])
