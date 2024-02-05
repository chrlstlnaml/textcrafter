from django.db import migrations, connection
import os


def create_publication_view(apps, schema_editor):
    current_path = os.path.abspath(__file__)
    sql_path = os.path.join(os.path.dirname(os.path.dirname(current_path)), 'sql', 'publication_view.sql')
    with open(sql_path, 'r') as f:
        sql = f.read()
    with connection.cursor() as cursor:
        cursor.execute(sql)


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_publication_view)
    ]
