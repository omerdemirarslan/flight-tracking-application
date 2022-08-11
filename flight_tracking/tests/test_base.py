import unittest


class TestBaseModelCase(unittest.TestCase):

    def test_model_meta_table_name(self):
        """
        This Test Method Controls Model Table Name By Meta.

        Expected From This Test Method:
            - Table name is correct.
            - Example: self.assertEqual(BaseModel._meta.table_name, "basemodel")
        """
        pass

    def test_create_instance(self):
        """
        This Test Method Controls Model Without Required Fields.

        Expected From This Test Method:
            - Are required fields not correct.
            - Like: If created_at field is none we'll wait an error.
        """
        pass

    def test_model_required_fields_default_properties_controls(self):
        """
        This Test Method Controls Model Required Fields Default Properties.

        Expected From This Test Method:
            - Are required fields default properties correct.
            - Like: Is id field content primary_key=True
        """
        pass

    def test_model_update_instance_field(self):
        """
        This Test Method Controls Instance Update By Base Model

        Expected From This Test Method:
            - Is instance update success.
        """
        pass

    def test_model_delete_instance(self):
        """
        This Test Method Controls Instance Delete (is active True or False) By Base Model

        Expected From This Test Method:
            - Is instance delete success.
        """
        pass


if __name__ == "__main__":
    unittest.main()
