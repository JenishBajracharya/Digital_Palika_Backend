from django.db import models


class MainCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    main_category = models.ForeignKey(
        MainCategory,
        on_delete=models.CASCADE,
        related_name="subcategories"
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class IdentityCardBase(models.Model):

    category = models.ForeignKey(
        MainCategory,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)

    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)
    ward_no = models.PositiveIntegerField()
    tole = models.CharField(max_length=255)

    father_first_name = models.CharField(max_length=100)
    father_middle_name = models.CharField(max_length=100, blank=True)
    father_last_name = models.CharField(max_length=100)

    mother_first_name = models.CharField(max_length=100)
    mother_middle_name = models.CharField(max_length=100, blank=True)
    mother_last_name = models.CharField(max_length=100)

    grandfather_first_name = models.CharField(max_length=100)
    grandfather_middle_name = models.CharField(max_length=100, blank=True)
    grandfather_last_name = models.CharField(max_length=100)

    date_of_birth = models.DateField()

    photo = models.ImageField(
        upload_to="identity_cards/photos/"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        abstract = True



class MahilaIdentityCard(IdentityCardBase):

    MARITAL_STATUS = [
        ("single", "Single"),
        ("married", "Married"),
        ("widow", "Widow"),
        ("divorced", "Divorced"),
    ]

    mobile_no = models.CharField(max_length=20)

    marital_status = models.CharField(
        max_length=20,
        choices=MARITAL_STATUS
    )

    citizenship_document = models.FileField(
        upload_to="mahila/documents/"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class BalbalikaIdentityCard(IdentityCardBase):

    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    birth_registration = models.FileField(
        upload_to="balbalika/documents/"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class ApangaIdentityCard(IdentityCardBase):

    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]

    BLOOD_GROUPS = [
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-"),
    ]

    citizenship_no = models.CharField(
        max_length=100,
        unique=True
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    mobile_no = models.CharField(max_length=20)

    blood_group = models.CharField(
        max_length=5,
        choices=BLOOD_GROUPS
    )

    disability_type = models.CharField(
        max_length=100
    )

    disability_nature = models.CharField(
        max_length=100
    )

    disability_severity = models.CharField(
        max_length=100
    )

    citizenship_document = models.FileField(
        upload_to="apanga/documents/"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class JanmaDarta(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    sifaris_prakar = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=20)
    status = models.CharField(max_length=50)


class mrituDarta(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    sifaris_prakar = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=20)
    status = models.CharField(max_length=50)

class biwahaDarta(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    sifaris_prakar = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=20)
    status = models.CharField(max_length=50)

class migration_suchana(models.Model):
    id = models.AutoField(primary_key=True)
    applicants_name = models.CharField(max_length=255)
    application_date = models.DateField()
    citizen_no = models.CharField(max_length=255)
    current_ward = models.IntegerField(max_length=20)
    verified = models.CharField(max_length=50)
    action = models.CharField(max_length=50)


class fileBhitra(models.Model):
    id = models.AutoField(primary_key=True)
    file_bhitra = models.CharField(max_length=255)
    action = models.CharField(max_length=50)
    

class file_prakar(models.Model):
    id = models.AutoField(primary_key=True)
    file_prakar = models.CharField(max_length=255)
    action = models.CharField(max_length=50)

class rayak_khand_no(models.Model):
    id = models.AutoField(primary_key=True)
    rayak_khand_no = models.IntegerField(max_length=255)
    action = models.CharField(max_length=50)

class file_record(models.Model):
    id = models.AutoField(primary_key=True)
    record_code = models.CharField(max_length=255)
    arthik_barsa = models.DateTimeField()
    file_prakar = models.ForeignKey(file_prakar, on_delete=models.CASCADE)
    raik_khand = models.CharField(max_length=255)
    raik_number = models.CharField(max_length=255)
    file_bhitra = models.ForeignKey(fileBhitra, on_delete=models.CASCADE)
    kotha_no = models.CharField(max_length=255)
    pariyojana = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="identity_cards/photos/")
    action = models.CharField(max_length=50)


class file_chalani(models.Model):
    id = models.AutoField(primary_key=True)
    file_record = models.ForeignKey(file_record, on_delete=models.CASCADE)
    chalani_bujhiline = models.CharField(max_length=255)
    chalani_date = models.DateTimeField()
    chalani_firta_miti = models.DateTimeField()
    chalani_status = models.CharField(max_length=50)
    action = models.CharField(max_length=50)

     