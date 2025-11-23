from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_number', models.CharField(max_length=50)),
                ('motto', models.CharField(max_length=200)),
                ('room', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LibraryCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.CharField(max_length=50)),
                ('issue_date', models.DateField()),
                ('expire_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Literature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lit_id', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=100)),
                ('publish_date', models.DateField()),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TakeBookProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.CharField(max_length=50)),
                ('literature_id', models.CharField(max_length=50)),
                ('take_date', models.DateField()),
                ('giver_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('student_id', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=models.SET_NULL, to='library_app.studentgroup')),
                ('library_card', models.ForeignKey(blank=True, null=True, on_delete=models.SET_NULL, to='library_app.librarycard')),
            ],
        ),
    ]
