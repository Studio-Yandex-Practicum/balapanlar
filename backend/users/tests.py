from django.db.utils import IntegrityError
from django.test import TestCase

from .constants import (HELP_TEXT_ACTIVE_TEST, HELP_TEXT_EMAIL_TEST,
                        HELP_TEXT_FIRST_NAME_TEST, HELP_TEXT_ID_TEST,
                        HELP_TEXT_LAST_NAME_TEST, HELP_TEXT_PASSWORD_TEST,
                        HELP_TEXT_TEAM_TEST, VALID_EMAIL_1_TEST,
                        VALID_EMAIL_2_TEST, VALID_FIRST_NAME_1_TEST,
                        VALID_FIRST_NAME_2_TEST, VALID_LAST_NAME_1_TEST,
                        VALID_LAST_NAME_2_TEST, VERBOSE_NAME_PASSWORD_TEST,
                        VALID_PASSWORD_1_TEST, VALID_PASSWORD_2_TEST,
                        VERBOSE_NAME_ACTIVE_TEST, VERBOSE_NAME_EMAIL_TEST,
                        VERBOSE_NAME_FIRST_NAME_TEST,
                        VERBOSE_NAME_LAST_NAME_TEST, VERBOSE_NAME_TEAM_TEST,
                        VERBOSE_NAME_ID_TEST)
from .models import CustomUser


class UserModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        """Creating of test db."""
        super().setUpClass()
        cls.user = CustomUser.objects.create(
            email=VALID_EMAIL_1_TEST,
            password=VALID_PASSWORD_1_TEST,
            first_name=VALID_FIRST_NAME_1_TEST,
            last_name=VALID_LAST_NAME_1_TEST
        )

    def test_users_model_has_correct_object_name(self):
        """Test checks that model's method __str__ works correct."""
        user_str_method = __class__.user.__str__()
        expected_output = (
            f'Пользователь {self.user.first_name} '
            f'{self.user.last_name}, '
            f'email: {self.user.email}'
        )
        self.assertEqual(expected_output, user_str_method)

    def test_user_with_valid_data_creates(self):
        """Test checks user with valid data creates."""
        users_count = CustomUser.objects.count()
        CustomUser.objects.create(
            email=VALID_EMAIL_2_TEST,
            password=VALID_PASSWORD_2_TEST,
            first_name=VALID_FIRST_NAME_2_TEST,
            last_name=VALID_LAST_NAME_2_TEST
        )
        self.assertEqual(
            CustomUser.objects.count(), users_count + 1
        )
        self.assertTrue(
            CustomUser.objects.filter(
                email=VALID_EMAIL_2_TEST
            ).exists()
        )

    def test_user_has_unique_email_first_name_last_name(self):
        """Test checks new user has unique fields:
           email, first_name and last_name.
        """
        with self.assertRaises(IntegrityError):
            CustomUser.objects.create(
                email=self.user.email,
                password=self.user.password,
                first_name=self.user.first_name,
                last_name=self.user.last_name
            )

    def test_users_model_correct_verbose_names(self):
        """Test checks CustomUser model fields have correct verbose_names."""
        user = __class__.user
        valid_verbose_names = {
            'id': VERBOSE_NAME_ID_TEST,
            'email': VERBOSE_NAME_EMAIL_TEST,
            'password': VERBOSE_NAME_PASSWORD_TEST,
            'first_name': VERBOSE_NAME_FIRST_NAME_TEST,
            'last_name': VERBOSE_NAME_LAST_NAME_TEST,
            'is_team': VERBOSE_NAME_TEAM_TEST,
            'is_active': VERBOSE_NAME_ACTIVE_TEST
        }
        for field, expected_value in valid_verbose_names.items():
            with self.subTest(field=field):
                self.assertEqual(
                    user._meta.get_field(field).verbose_name,
                    expected_value
                )

    def test_users_model_correct_help_texts(self):
        """Test checks CustomUser model fields have correct help_texts."""
        user = __class__.user
        valid_help_texts = {
            'id': HELP_TEXT_ID_TEST,
            'email': HELP_TEXT_EMAIL_TEST,
            'password': HELP_TEXT_PASSWORD_TEST,
            'first_name': HELP_TEXT_FIRST_NAME_TEST,
            'last_name': HELP_TEXT_LAST_NAME_TEST,
            'is_team': HELP_TEXT_TEAM_TEST,
            'is_active': HELP_TEXT_ACTIVE_TEST
        }
        for field, expected_value in valid_help_texts.items():
            with self.subTest(field=field):
                self.assertEqual(
                    user._meta.get_field(field).help_text,
                    expected_value
                )
