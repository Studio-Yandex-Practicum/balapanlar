import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404

from npo_project.models import (
    Benefit,
    Course,
    CourseCategory,
    CoursePrice,
    CourseTag,
    FAQ,
    IncludedInCoursePrice,
    Location,
    NotIncludedInCoursePrice,
    Partner,
    Principle,
    Program,
    ProgramCharacteristic,
    Requisite,
    TeamMember,
)

MODEL_NAME_FILE = {
    'benefit': (Benefit, 'benefit.csv'),
    'course': (Course, 'course.csv'),
    'course_category': (CourseCategory, 'course_category.csv'),
    'course_price': (CoursePrice, 'course_price.csv'),
    'course_tag': (CourseTag, 'course_tag.csv'),
    'faq': (FAQ, 'faq.csv'),
    'included_in_course_price': (
        IncludedInCoursePrice, 'incl_in_course_price.csv'
    ),
    'location': (Location, 'location.csv'),
    'not_included_in_course_price': (
        NotIncludedInCoursePrice, 'not_incl_in_course_price.csv'
    ),
    'partner': (Partner, 'partner.csv'),
    'principle': (Principle, 'principle.csv'),
    'program': (Program, 'program.csv'),
    'program_characteristic': (
        ProgramCharacteristic, 'program_characteristic.csv'
    ),
    'requisite': (Requisite, 'requisite.csv'),
    'team_member': (TeamMember, 'team_member.csv'),
}


class Command(BaseCommand):
    help = 'Load data from a csv file to the corresponding db table'

    @staticmethod
    def get_csv_file(filename):
        return os.path.join(
            settings.BASE_DIR, 'npo_project', 'csv_data', filename
        )

    @staticmethod
    def clear_model(model):
        model.objects.all().delete()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def print_to_terminal(self, message):
        self.stdout.write(self.style.SUCCESS(message))

    def load_model(self, model_name, field_names):
        model, file_path = MODEL_NAME_FILE.get(model_name)
        with open(self.get_csv_file(file_path)) as file:
            reader = csv.reader(file, delimiter=',')
            self.clear_model(model)
            line = 0
            for row in reader:
                if row != '' and line > 0:
                    params = dict(zip(field_names, row))
                    _, created = model.objects.get_or_create(**params)
                line += 1
        self.print_to_terminal(
            f'{line - 1} objects added to "{model_name}" table'
        )

    def connecting_related_models(self,
                                  main_model,
                                  related_model,
                                  relational_field: str,
                                  through_model_name: str):

        with open(self.get_csv_file(f'_{through_model_name}.csv')) as file:
            reader = csv.reader(file, delimiter=',')
            line = 0
            for row in reader:
                if row != '' and line > 0:
                    main_object = get_object_or_404(
                        main_model, pk=row[1])
                    related_object = get_object_or_404(
                        related_model, pk=row[2])
                    main_obj_attr = getattr(main_object, relational_field)
                    main_obj_attr.add(related_object)
                line += 1
        self.print_to_terminal(
            f'{line - 1} objects added to intermediate table '
            f'"{through_model_name}"'
        )

    def load_course_category(self):
        self.load_model(
            'course_category',
            ['id', 'name', 'description']
        )

    def load_course_tag(self):
        self.load_model(
            'course_tag',
            ['id', 'name']
        )

    def load_course(self):
        self.load_model(
            'course',
            ['id', 'name', 'age_groups', 'duration', 'description',
             'skills', 'category_id']
        )
        self.connecting_related_models(
            Course, CourseTag,
            relational_field='tags',
            through_model_name='course_tags'
        )

    def load_incl_in_course_price(self):
        self.load_model(
            'included_in_course_price',
            ['id', 'text']
        )

    def load_not_incl_in_course_price(self):
        self.load_model(
            'not_included_in_course_price',
            ['id', 'text']
        )

    def load_course_price(self):
        self.load_model(
            'course_price',
            ['id', 'price', 'payment_url']
        )
        self.connecting_related_models(
            CoursePrice, IncludedInCoursePrice,
            relational_field='included_in_price',
            through_model_name='course_price_included_in_price'
        )
        self.connecting_related_models(
            CoursePrice, NotIncludedInCoursePrice,
            relational_field='not_included_in_price',
            through_model_name='course_price_not_included_in_price'
        )

    def load_benefit(self):
        self.load_model(
            'benefit',
            ['id', 'text', 'beneficial_to', 'image']
        )

    def load_program_characteristic(self):
        self.load_model(
            'program_characteristic',
            ['id', 'text']
        )

    def load_program(self):
        self.load_model(
            'program',
            ['id', 'name', 'image', 'description', 'location']
        )
        self.connecting_related_models(
            Program, ProgramCharacteristic,
            relational_field='characteristics',
            through_model_name='program_characteristics'
        )

    def load_principle(self):
        self.load_model(
            'principle',
            ['id', 'text', 'image']
        )

    def load_team_member(self):
        self.load_model(
            'team_member',
            ['id', 'name', 'last_name', 'role', 'image']
        )

    def load_faq(self):
        self.load_model(
            'faq',
            ['id', 'question', 'answer']
        )

    def load_partner(self):
        self.load_model(
            'partner',
            ['id', 'name', 'description', 'image', 'url']
        )

    def load_location(self):
        self.load_model(
            'location',
            ['id', 'center_name', 'address', 'additional_info']
        )

    def load_requisite(self):
        self.load_model(
            'requisite',
            ['id', 'text']
        )

    def handle(self, *args, **kwargs):
        self.load_course_category()
        self.load_course_tag()
        self.load_course()
        self.load_incl_in_course_price()
        self.load_not_incl_in_course_price()
        self.load_course_price()
        self.load_benefit()
        self.load_program_characteristic()
        self.load_program()
        self.load_principle()
        self.load_team_member()
        self.load_faq()
        self.load_partner()
        self.load_location()
        self.load_requisite()
