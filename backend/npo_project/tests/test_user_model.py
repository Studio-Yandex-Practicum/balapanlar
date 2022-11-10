from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.test import TestCase

from .constants import (FIRST_NAME, LAST_NAME, CustomUserHelpTexts,
                        CustomUserVerboseNames, TestSuperUser, TestUser1,
                        TestUser2, TestUser3, TestUser4)
from npo_project.models.user import (INVALID_FIELD_MSG, IS_SUPERUSER_ERROR_MSG,
                                     IS_TEAM_ERROR_MSG, CustomUser)


class CustomUserModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        """Creates a test user in db."""
        super().setUpClass()
        cls.user = CustomUser.objects.create(
            email=TestUser1.EMAIL.value,
            password=TestUser1.PASSWORD.value,
            first_name=TestUser1.FIRST_NAME.value,
            last_name=TestUser1.LAST_NAME.value
        )

    @classmethod
    def tearDownClass(cls):
        """Clears data after all tests are done."""
        super().tearDownClass()
        cache.clear()

    def test_users_model_has_correct_object_name(self):
        """CustomUser Model's method __str__ works correct."""
        user_str_method = __class__.user.__str__()
        expected_output = (
            f'Пользователь: {self.user.first_name} '
            f'{self.user.last_name}, '
            f'email: {self.user.email}'
        )
        self.assertEqual(expected_output, user_str_method)

    def test_user_with_valid_data_creates(self):
        """User with valid data can be created."""
        users_count = CustomUser.objects.count()
        new_user = CustomUser.objects.create(
            email=TestUser2.EMAIL.value,
            password=TestUser2.PASSWORD.value,
            first_name=TestUser2.FIRST_NAME.value,
            last_name=TestUser2.LAST_NAME.value
        )
        self.assertEqual(
            CustomUser.objects.count(), users_count + 1
        )
        self.assertTrue(
            CustomUser.objects.filter(
                email=TestUser2.EMAIL.value
            ).exists()
        )
        self.assertTrue(new_user.is_active)
        self.assertFalse(new_user.is_team)

    def test_user_has_unique_email_first_name_last_name(self):
        """
        New user has unique constraints for fields: email, first_name
        and last_name. IntegrityError is raised with error message.
        """
        expected_error_message = (
            'UNIQUE constraint failed: custom_user.email, '
            'custom_user.first_name, custom_user.last_name'
        )
        with self.assertRaisesMessage(IntegrityError, expected_error_message):
            CustomUser.objects.create(
                email=self.user.email,
                password=self.user.password,
                first_name=self.user.first_name,
                last_name=self.user.last_name
            )

    def test_user_can_not_be_created_with_invalid_first_name(self):
        """
        User with invalid first_name raises a ValidationError with
        specific error message.
        """
        expected_error_message = INVALID_FIELD_MSG.format(FIRST_NAME)
        with self.assertRaisesMessage(ValidationError, expected_error_message):
            invalid_user = CustomUser(
                email=TestUser3.EMAIL.value,
                password=TestUser3.PASSWORD.value,
                first_name=TestUser3.FIRST_NAME.value,
                last_name=TestUser3.LAST_NAME.value
            )
            invalid_user.clean_fields()

    def test_user_can_not_be_created_with_invalid_last_name(self):
        """
        User with invalid last_name raises a ValidationError with
        specific error message.
        """
        expected_error_message = INVALID_FIELD_MSG.format(LAST_NAME)
        with self.assertRaisesMessage(ValidationError, expected_error_message):
            invalid_user = CustomUser(
                email=TestUser4.EMAIL.value,
                password=TestUser4.PASSWORD.value,
                first_name=TestUser4.FIRST_NAME.value,
                last_name=TestUser4.LAST_NAME.value
            )
            invalid_user.clean_fields()

    def test_superuser_creates_with_team_superuser_flags_true(self):
        """
        Superuser was created in db and fields is_team=True,
        is_superuser=True.
        """
        valid_superuser = CustomUser.objects.create_superuser(
            email=TestSuperUser.EMAIL.value,
            password=TestSuperUser.PASSWORD.value,
            first_name=TestSuperUser.FIRST_NAME.value,
            last_name=TestSuperUser.LAST_NAME.value
        )
        self.assertIs(valid_superuser.is_team, True)
        self.assertIs(valid_superuser.is_superuser, True)
        self.assertIs(
            CustomUser.objects.filter(
                email=TestSuperUser.EMAIL.value
            ).exists(), True
        )

    def test_superuser_with_is_team_flag_false_raises_error(self):
        """
        Superuser with is_team=False can not be created,
        Validation error is raised with specific message.
        Regex pattern for the field last_name works correct.
        """
        with self.assertRaisesMessage(ValueError, IS_TEAM_ERROR_MSG):
            invalid_superuser = CustomUser.objects.create_superuser(
                email=TestSuperUser.EMAIL.value,
                password=TestSuperUser.PASSWORD.value,
                first_name=TestSuperUser.FIRST_NAME.value,
                last_name=TestSuperUser.LAST_NAME.value,
                is_team=False
            )
            invalid_superuser.full_clean()
        self.assertIs(
            CustomUser.objects.filter(
                email=TestSuperUser.EMAIL.value
            ).exists(), False
        )

    def test_superuser_with_is_superuser_flag_false_raises_error(self):
        """
        Superuser with is_superuser=False can not be created,
        Validation error is raised with specific message.
        Regex pattern for the field last_name works correct.
        """
        with self.assertRaisesMessage(ValueError, IS_SUPERUSER_ERROR_MSG):
            invalid_superuser = CustomUser.objects.create_superuser(
                email=TestSuperUser.EMAIL.value,
                password=TestSuperUser.PASSWORD.value,
                first_name=TestSuperUser.FIRST_NAME.value,
                last_name=TestSuperUser.LAST_NAME.value,
                is_superuser=False
            )
            invalid_superuser.full_clean()
        self.assertIs(
            CustomUser.objects.filter(
                email=TestSuperUser.EMAIL.value
            ).exists(), False
        )

    def test_users_model_correct_verbose_names(self):
        """CustomUser model's fields have correct verbose_names."""
        user = __class__.user
        for field in CustomUserVerboseNames:
            with self.subTest(field=field):
                self.assertEqual(
                    user._meta.get_field(field.name.lower()).verbose_name,
                    field.value
                )

    def test_users_model_correct_help_texts(self):
        """CustomUser model's fields have correct help_texts."""
        user = __class__.user
        for field in CustomUserHelpTexts:
            with self.subTest(field=field.name):
                self.assertEqual(
                    user._meta.get_field(field.name.lower()).help_text,
                    field.value
                )
