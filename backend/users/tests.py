from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.test import TestCase

from .constants import (HELP_TEXT_ACTIVE_TEST, HELP_TEXT_EMAIL_TEST,
                        HELP_TEXT_FIRST_NAME_TEST, HELP_TEXT_ID_TEST,
                        HELP_TEXT_LAST_NAME_TEST, HELP_TEXT_PASSWORD_TEST,
                        HELP_TEXT_TEAM_TEST, INVALID_FIRST_NAME_TEST,
                        INVALID_LAST_NAME_TEST, SUPERUSER_EMAIL_TEST,
                        SUPERUSER_FIRST_NAME_TEST, SUPERUSER_LAST_NAME_TEST,
                        SUPERUSER_PASSWORD_TEST, VALID_EMAIL_1_TEST,
                        VALID_EMAIL_2_TEST, VALID_FIRST_NAME_1_TEST,
                        VALID_FIRST_NAME_2_TEST, VALID_LAST_NAME_1_TEST,
                        VALID_LAST_NAME_2_TEST, VALID_PASSWORD_1_TEST,
                        VALID_PASSWORD_2_TEST, VERBOSE_NAME_ACTIVE_TEST,
                        VERBOSE_NAME_EMAIL_TEST, VERBOSE_NAME_FIRST_NAME_TEST,
                        VERBOSE_NAME_ID_TEST, VERBOSE_NAME_LAST_NAME_TEST,
                        VERBOSE_NAME_PASSWORD_TEST, VERBOSE_NAME_TEAM_TEST)

from .models import (INVALID_FIELD_MSG, IS_SUPERUSER_ERROR_MSG,
                     IS_TEAM_ERROR_MSG, CustomUser)

FIRST_NAME = 'Имя'
LAST_NAME = 'Фамилия'


class UserModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        """Creating of test user in db."""
        super().setUpClass()
        cls.user = CustomUser.objects.create(
            email=VALID_EMAIL_1_TEST,
            password=VALID_PASSWORD_1_TEST,
            first_name=VALID_FIRST_NAME_1_TEST,
            last_name=VALID_LAST_NAME_1_TEST
        )

    @classmethod
    def tearDownClass(cls):
        """Clears data after all tests are done."""
        super().tearDownClass()
        cache.clear()

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
        """Test checks user with valid data can be created."""
        users_count = CustomUser.objects.count()
        new_user = CustomUser.objects.create(
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
        self.assertTrue(new_user.is_active)
        self.assertFalse(new_user.is_team)

    def test_user_has_unique_email_first_name_last_name(self):
        """Test checks new user has unique constraints for fields:
           email, first_name and last_name. IntegrityError is raised.
        """
        with self.assertRaises(IntegrityError):
            CustomUser.objects.create(
                email=self.user.email,
                password=self.user.password,
                first_name=self.user.first_name,
                last_name=self.user.last_name
            )

    def test_user_can_not_be_created_with_invalid_first_name(self):
        """Test checks that user with invalid first_name raises a
           ValidationError with specific error message.
        """
        expected_error_message = INVALID_FIELD_MSG.format(FIRST_NAME)
        with self.assertRaisesMessage(ValidationError, expected_error_message):
            invalid_user = CustomUser(
                email=VALID_EMAIL_2_TEST,
                password=VALID_PASSWORD_1_TEST,
                first_name=INVALID_FIRST_NAME_TEST,
                last_name=VALID_LAST_NAME_2_TEST
            )
            invalid_user.clean_fields()

    def test_user_can_not_be_created_with_invalid_last_name(self):
        """Test checks that user with invalid last_name raises a
           ValidationError with specific error message.
        """
        expected_error_message = INVALID_FIELD_MSG.format(LAST_NAME)
        with self.assertRaisesMessage(ValidationError, expected_error_message):
            invalid_user = CustomUser(
                email=VALID_EMAIL_2_TEST,
                password=VALID_PASSWORD_1_TEST,
                first_name=VALID_FIRST_NAME_1_TEST,
                last_name=INVALID_LAST_NAME_TEST
            )
            invalid_user.clean_fields()

    def test_superuser_creates_with_team_superuser_flags_true(self):
        """Test checks that superuser was created in db and
           fields is_team=True, is_superuser=True.
        """
        valid_superuser = CustomUser.objects.create_superuser(
                email=SUPERUSER_EMAIL_TEST,
                password=SUPERUSER_PASSWORD_TEST,
                first_name=SUPERUSER_FIRST_NAME_TEST,
                last_name=SUPERUSER_LAST_NAME_TEST
        )
        self.assertTrue(valid_superuser.is_team)
        self.assertTrue(valid_superuser.is_superuser)
        self.assertTrue(
            CustomUser.objects.filter(email=SUPERUSER_EMAIL_TEST).exists()
        )

    def test_superuser_with_is_team_flag_false_raises_error(self):
        """Test checks that superuser with is_team=False can not be created,
           Validation error is raised with specific message.
           Checking that regex pattern for the field last_name works correct.
        """
        with self.assertRaisesMessage(ValueError, IS_TEAM_ERROR_MSG):
            invalid_superuser = CustomUser.objects.create_superuser(
                email=SUPERUSER_EMAIL_TEST,
                password=SUPERUSER_PASSWORD_TEST,
                first_name=SUPERUSER_FIRST_NAME_TEST,
                last_name=SUPERUSER_LAST_NAME_TEST,
                is_team=False
            )
            invalid_superuser.full_clean()
        self.assertFalse(
            CustomUser.objects.filter(email=SUPERUSER_EMAIL_TEST).exists()
        )

    def test_superuser_with_is_superuser_flag_false_raises_error(self):
        """Test checks that superuser with is_superuser=False can not be
           created, Validation error is raised with specific message.
           Checking that regex pattern for the field last_name works correct.
        """
        with self.assertRaisesMessage(ValueError, IS_SUPERUSER_ERROR_MSG):
            invalid_superuser = CustomUser.objects.create_superuser(
                email=SUPERUSER_EMAIL_TEST,
                password=SUPERUSER_PASSWORD_TEST,
                first_name=SUPERUSER_FIRST_NAME_TEST,
                last_name=SUPERUSER_LAST_NAME_TEST,
                is_superuser=False
            )
            invalid_superuser.full_clean()
        self.assertFalse(
            CustomUser.objects.filter(email=SUPERUSER_EMAIL_TEST).exists()
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
