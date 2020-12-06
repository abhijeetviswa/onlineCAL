# Generated by Django 3.0.2 on 2020-12-06 14:23

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=50)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('desc', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('sup_dept', models.CharField(max_length=75)),
                ('sample_from_outside', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('origin_of_sample', models.CharField(max_length=75)),
                ('req_discussed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
            ],
            options={
                'verbose_name': 'User Detail',
                'verbose_name_plural': 'User Details',
            },
        ),
        migrations.CreateModel(
            name='AAS',
            fields=[
                ('userdetails_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='booking_portal.UserDetails')),
                ('sample_code', models.CharField(max_length=75)),
                ('elements', models.CharField(max_length=75)),
                ('other_remarks', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'AAS',
                'verbose_name_plural': 'AAS',
            },
            bases=('booking_portal.userdetails',),
        ),
        migrations.CreateModel(
            name='BET',
            fields=[
                ('userdetails_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='booking_portal.UserDetails')),
                ('sample_code', models.CharField(max_length=75)),
                ('pretreatment_conditions', models.CharField(max_length=75)),
                ('precautions', models.CharField(max_length=75)),
                ('adsorption', models.CharField(max_length=75)),
                ('surface_area', models.CharField(max_length=75)),
                ('other_remarks', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'BET',
                'verbose_name_plural': 'BET',
            },
            bases=('booking_portal.userdetails',),
        ),
        migrations.CreateModel(
            name='CDSpectrophotometer',
            fields=[
                ('userdetails_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='booking_portal.UserDetails')),
                ('sample_code', models.CharField(max_length=75)),
                ('wavelength_scan_start', models.CharField(max_length=75)),
                ('wavelength_scan_end', models.CharField(max_length=75)),
                ('wavelength_fixed', models.CharField(max_length=75)),
                ('temp_range_scan_start', models.CharField(max_length=75)),
                ('temp_range_scan_end', models.CharField(max_length=75)),
                ('temp_range_fixed', models.CharField(max_length=75)),
                ('concentration', models.CharField(max_length=75)),
                ('cell_path_length', models.CharField(max_length=75)),
                ('other_remarks', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'CDSpectrophotometer',
                'verbose_name_plural': 'CDSpectrophotometer',
            },
            bases=('booking_portal.userdetails',),
        ),
        migrations.CreateModel(
            name='DSC',
            fields=[
                ('userdetails_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='booking_portal.UserDetails')),
                ('sample_code', models.CharField(max_length=75)),
                ('chemical_composition', models.CharField(max_length=75)),
                ('sample_amount', models.CharField(max_length=75)),
                ('heating_program', models.CharField(choices=[('Dynamic', 'Dynamic'), ('Isothermal', 'Isothermal')], max_length=15)),
                ('temp_range', models.CharField(max_length=75)),
                ('atmosphere', models.CharField(choices=[('N2', 'N2'), ('Ar', 'Ar'), ('Air', 'Air')], max_length=5)),
                ('heating_rate', models.CharField(max_length=75)),
                ('other_remarks', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'DSC',
                'verbose_name_plural': 'DSC',
            },
            bases=('booking_portal.userdetails',),
        ),
        migrations.CreateModel(
            name='EDXRF',
            fields=[
                ('userdetails_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='booking_portal.UserDetails')),
                ('sample_code', models.CharField(max_length=75)),
                ('sample_nature', models.CharField(choices=[('Powder', 'Powder'), ('Metal', 'Metal'), ('Film', 'Film'), ('Biological', 'Biological'), ('Concrete', 'Concrete')], max_length=15)),
                ('elements_present', models.CharField(max_length=75)),
                ('other_remarks', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'EDXRF',
                'verbose_name_plural': 'EDXRF',
            },
            bases=('booking_portal.userdetails',),
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='faculties', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('department', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'faculty',
                'verbose_name_plural': 'faculties',
                'default_related_name': 'faculties',
            },
            bases=('booking_portal.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='FESEM',
            fields=[
                ('userdetails_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='booking_portal.UserDetails')),
                ('sample_code', models.CharField(max_length=75)),
                ('sample_nature', models.CharField(choices=[('Metal', 'Metal'), ('Film', 'Film'), ('Crystal', 'Crystal'), ('Powder', 'Powder'), ('Biological', 'Biological'), ('Ceramic', 'Ceramic'), ('Tissue', 'Tissue'), ('Others', 'Others')], max_length=15)),
                ('analysis_nature', models.CharField(max_length=75)),
                ('sputter_required', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('other_remarks', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'FESEM',
                'verbose_name_plural': 'FESEM',
            },
            bases=('booking_portal.userdetails',),
        ),
        migrations.CreateModel(
            name='FTIR',
            fields=[
                ('userdetails_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='booking_portal.UserDetails')),
                ('sample_code', models.CharField(max_length=75)),
                ('composition', models.CharField(max_length=75)),
                ('state', models.CharField(choices=[('Solid', 'Solid'), ('Liquid', 'Liquid')], max_length=10)),
                ('solvent', models.CharField(max_length=75)),
                ('other_remarks', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'FTIR',
                'verbose_name_plural': 'FTIR',
            },
            bases=('booking_portal.userdetails',),
        ),
        migrations.CreateModel(
            name='GC',
            fields=[
                ('userdetails_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='booking_portal.UserDetails')),
                ('sample_code', models.CharField(max_length=75)),
                ('appearance', models.CharField(max_length=75)),
                ('no_of_gc_peaks', models.IntegerField()),
                ('solvent_solubility', models.CharField(max_length=75)),
                ('column_details', models.CharField(max_length=75)),
                ('exp_mol_wt', models.CharField(max_length=75)),
                ('mp_bp', models.CharField(max_length=75)),
                ('sample_source', models.CharField(choices=[('Natural', 'Natural'), ('Synthesis', 'Synthesis'), ('Waste', 'Waste')], max_length=15)),
                ('other_remarks', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'GC',
                'verbose_name_plural': 'GC',
            },
            bases=('booking_portal.userdetails',),
        ),
        migrations.CreateModel(
            name='HPLC',
            fields=[
                ('userdetails_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='booking_portal.UserDetails')),
                ('sample_code', models.CharField(max_length=75)),
                ('sample_information', models.CharField(max_length=75)),
                ('mobile_phase', models.CharField(max_length=75)),
                ('column_for_lc', models.CharField(max_length=75)),
                ('detection_wavelength', models.CharField(max_length=75)),
                ('other_information', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'HPLC',
                'verbose_name_plural': 'HPLC',
            },
            bases=('booking_portal.userdetails',),
        ),
        migrations.CreateModel(
            name='LabAssistant',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='labassistants', serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'lab assistant',
                'default_related_name': 'labassistants',
            },
            bases=('booking_portal.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='LCMS',
            fields=[
                ('userdetails_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='booking_portal.UserDetails')),
                ('sample_code', models.CharField(max_length=75)),
                ('composition', models.CharField(max_length=75)),
                ('phase', models.CharField(max_length=75)),
                ('no_of_lc_peaks', models.IntegerField()),
                ('solvent_solubility', models.CharField(max_length=75)),
                ('exact_mass', models.CharField(max_length=75)),
                ('mass_adducts', models.CharField(max_length=75)),
                ('analysis_mode', models.CharField(choices=[('Positive', 'Positive'), ('Negative', 'Negative')], max_length=10)),
                ('other_remarks', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'LCMS',
                'verbose_name_plural': 'LCMS',
            },
            bases=('booking_portal.userdetails',),
        ),
        migrations.CreateModel(
            name='LSCM',
            fields=[
                ('userdetails_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='booking_portal.UserDetails')),
                ('sample_description', models.CharField(max_length=75)),
                ('dye', models.CharField(max_length=75)),
                ('excitation_wavelength', models.CharField(max_length=75)),
                ('emission_range', models.CharField(max_length=75)),
                ('analysis_details', models.CharField(max_length=75)),
            ],
            options={
                'verbose_name': 'LSCM',
                'verbose_name_plural': 'LSCM',
            },
            bases=('booking_portal.userdetails',),
        ),
        migrations.CreateModel(
            name='NMR',
            fields=[
                ('userdetails_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='booking_portal.UserDetails')),
                ('sample_code', models.CharField(max_length=75)),
                ('sample_nature', models.CharField(choices=[('Solid', 'Solid'), ('Liquid', 'Liquid')], max_length=10)),
                ('quantity', models.CharField(max_length=75)),
                ('solvent', models.CharField(max_length=75)),
                ('analysis', models.CharField(max_length=75)),
                ('experiment', models.CharField(max_length=75)),
                ('spectral_range', models.CharField(max_length=75)),
                ('other_remarks', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'NMR',
                'verbose_name_plural': 'NMR',
            },
            bases=('booking_portal.userdetails',),
        ),
        migrations.CreateModel(
            name='PXRD',
            fields=[
                ('userdetails_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='booking_portal.UserDetails')),
                ('sample_code', models.CharField(max_length=75)),
                ('chemical_composition', models.CharField(max_length=75)),
                ('sample_description', models.CharField(choices=[('Film', 'Film'), ('Powder', 'Powder'), ('Pellet', 'Pellet')], max_length=10)),
                ('range', models.CharField(max_length=75)),
                ('scanning_rate', models.CharField(max_length=75)),
                ('any_remarks', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'PXRD',
                'verbose_name_plural': 'PXRD',
            },
            bases=('booking_portal.userdetails',),
        ),
        migrations.CreateModel(
            name='Rheometer',
            fields=[
                ('userdetails_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='booking_portal.UserDetails')),
                ('sample_code', models.CharField(max_length=75)),
                ('ingredient_details', models.CharField(max_length=75)),
                ('physical_characteristics', models.CharField(max_length=75)),
                ('chemical_nature', models.CharField(max_length=75)),
                ('origin', models.CharField(choices=[('Natural', 'Natural'), ('Synthetic', 'Synthetic')], max_length=10)),
                ('analysis_required', models.CharField(max_length=75)),
                ('other_remarks', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Rheometer',
                'verbose_name_plural': 'Rheometer',
            },
            bases=('booking_portal.userdetails',),
        ),
        migrations.CreateModel(
            name='SCXRD',
            fields=[
                ('userdetails_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='booking_portal.UserDetails')),
                ('sample_code', models.CharField(max_length=75)),
                ('chemical_composition', models.CharField(max_length=75)),
                ('scanning_rate', models.CharField(max_length=75)),
                ('source', models.CharField(choices=[('Cu', 'Cu'), ('Mo', 'Mo')], max_length=5)),
                ('any_remarks', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'SCXRD',
                'verbose_name_plural': 'SCXRD',
            },
            bases=('booking_portal.userdetails',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='students', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('id_number', models.CharField(max_length=20)),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='students', to='booking_portal.Faculty')),
            ],
            options={
                'verbose_name': 'student',
                'default_related_name': 'students',
            },
            bases=('booking_portal.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='TCSPC',
            fields=[
                ('userdetails_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='booking_portal.UserDetails')),
                ('sample_code', models.CharField(max_length=75)),
                ('sample_nature', models.CharField(choices=[('Metal', 'Metal'), ('Film', 'Film'), ('Crystal', 'Crystal'), ('Powder', 'Powder'), ('Biological', 'Biological'), ('Ceramic', 'Ceramic'), ('Tissue', 'Tissue'), ('Others', 'Others')], max_length=15)),
                ('chemical_composition', models.CharField(max_length=75)),
                ('other_remarks', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'TCSPC',
                'verbose_name_plural': 'TCSPC',
            },
            bases=('booking_portal.userdetails',),
        ),
        migrations.CreateModel(
            name='TGA',
            fields=[
                ('userdetails_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='booking_portal.UserDetails')),
                ('sample_code', models.CharField(max_length=75)),
                ('chemical_composition', models.CharField(max_length=75)),
                ('sample_amount', models.CharField(max_length=75)),
                ('heating_program', models.CharField(choices=[('Dynamic', 'Dynamic'), ('Isothermal', 'Isothermal')], max_length=15)),
                ('temperature', models.CharField(max_length=75)),
                ('atmosphere', models.CharField(choices=[('N2', 'N2'), ('Ar', 'Ar'), ('Air', 'Air')], max_length=5)),
                ('heating_rate', models.CharField(max_length=75)),
                ('sample_solubility', models.CharField(max_length=75)),
                ('other_remarks', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'TGA',
                'verbose_name_plural': 'TGA',
            },
            bases=('booking_portal.userdetails',),
        ),
        migrations.CreateModel(
            name='UVSpectrophotometer',
            fields=[
                ('userdetails_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='booking_portal.UserDetails')),
                ('sample_code', models.CharField(max_length=75)),
                ('sample_composition', models.CharField(max_length=75)),
                ('molecular_weight', models.CharField(max_length=75)),
                ('analysis_mode', models.CharField(choices=[('Solid', 'Solid'), ('Liquid', 'Liquid'), ('Thin Film', 'Thin Film')], max_length=10)),
                ('wavelength', models.CharField(max_length=75)),
                ('ordinate_mode', models.CharField(max_length=75)),
                ('other_remarks', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'UVSpectrophotometer',
                'verbose_name_plural': 'UVSpectrophotometer',
            },
            bases=('booking_portal.userdetails',),
        ),
        migrations.CreateModel(
            name='XPS',
            fields=[
                ('userdetails_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='booking_portal.UserDetails')),
                ('sample_name', models.CharField(max_length=75)),
                ('sample_nature', models.CharField(max_length=75)),
                ('chemical_composition', models.CharField(max_length=75)),
                ('sample_property', models.CharField(choices=[('Conducting', 'Conducting'), ('Semi Conducting', 'Semi Conducting'), ('Insulating', 'Insulating')], max_length=20)),
                ('analysed_elements', models.CharField(max_length=75)),
                ('scan_details', models.CharField(max_length=75)),
                ('other_remarks', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'XPS',
                'verbose_name_plural': 'XPS',
            },
            bases=('booking_portal.userdetails',),
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('S1', 'Empty'), ('S2', 'In Process'), ('S3', 'Filled'), ('S4', 'Passed')], max_length=50)),
                ('date', models.DateField()),
                ('time', models.TimeField(null=True)),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='booking_portal.Instrument')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('R1', 'Waiting for faculty approval.'), ('R2', 'Waiting for lab assistant approval.'), ('R3', 'Approved'), ('R4', 'Rejected'), ('R5', 'Cancelled')], max_length=50)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType')),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='booking_portal.Instrument')),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_portal.Slot')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='booking_portal.Faculty')),
                ('lab_assistant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='booking_portal.LabAssistant')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='booking_portal.Student')),
            ],
        ),
        migrations.CreateModel(
            name='EmailModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.EmailField(max_length=254, null=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=500, null=True)),
                ('subject', models.CharField(max_length=100, null=True)),
                ('request', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='booking_portal.Request')),
            ],
        ),
        migrations.AddField(
            model_name='userdetails',
            name='sup_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_portal.Faculty'),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_portal.Student'),
        ),
    ]
