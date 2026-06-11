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


class Darta(models.Model):
    main_category = models.ForeignKey(
        MainCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="dartas",
    )
    darta_number = models.PositiveIntegerField(unique=True)
    darta_date = models.DateField()
    khata_number = models.CharField(max_length=100, blank=True)
    pathaune = models.CharField(max_length=255, blank=True)
    current_area_branch = models.CharField(max_length=255, blank=True)
    current_branch_members = models.CharField(max_length=255, blank=True)
    kaifiyat = models.TextField(blank=True)
    subject = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    upload = models.FileField(upload_to="darta/uploads/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Darta {self.darta_number} - {self.subject}"


class Pariyojana(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    main_category = models.ForeignKey(
        MainCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="pariyojanas",
    )
    sub_category = models.ForeignKey(
        SubCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="pariyojanas",
    )
    project_name = models.CharField(max_length=255)
    project_code = models.CharField(max_length=100, unique=True)
    project_date = models.DateField()
    project_start_date = models.DateField(blank=True, null=True)
    project_end_date = models.DateField(blank=True, null=True)
    project_description = models.TextField(blank=True)
    project_budget = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    project_location = models.CharField(max_length=255, blank=True)
    project_manager = models.CharField(max_length=255, blank=True)
    project_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    project_documents = models.FileField(upload_to="pariyojana/documents/", blank=True, null=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.project_name} ({self.project_code})"


class RayakNo(models.Model):
    main_category = models.ForeignKey(
        MainCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="rayak_nos",
    )
    sub_category = models.ForeignKey(
        SubCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="rayak_nos",
    )
    rayak_no = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Rayak No"
        verbose_name_plural = "Rayak Nos"

    def __str__(self):
        return self.rayak_no


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

     

class Chalani(models.Model):

    chalani_no = models.PositiveIntegerField(
        unique=True
    )

    chalani_date = models.CharField(
        max_length=20
    )

    # पत्रको किसिम
    letter_type = models.CharField(
        max_length=255
    )

    # पत्र बुज्ने शाखा
    receiving_branch = models.CharField(
        max_length=255
    )

    # पत्र पाउने कार्यालय वा व्यक्तिको नाम
    receiver_name = models.CharField(
        max_length=255
    )

    # पत्र पाउने कार्यालय वा व्यक्तिको ठेगाना
    receiver_address = models.TextField()

    # विषय
    subject = models.TextField()

    # फाइल
    attachment = models.FileField(
        upload_to="chalani/",
        blank=True,
        null=True
    )

    # बोदार्थ
    bodartha = models.TextField(
        blank=True,
        null=True
    )

    # कैफियत
    remarks = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-chalani_no"]

    def __str__(self):
        return f"Chalani #{self.chalani_no}"

class KothaNumber(models.Model):
    """
    Digital File System - Kotha Number
    """

    kotha_no = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Kotha No."
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "kotha_number"
        ordering = ["kotha_no"]
        verbose_name = "Kotha Number"
        verbose_name_plural = "Kotha Numbers"

    def __str__(self):
        return self.kotha_no
    
class AarthikBarsa(models.Model):
    """
    Digital File System - Aarthik Barsa
    """

    aarthik_barsa = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Aarthik Barsa"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "aarthik_barsa"
        ordering = ["aarthik_barsa"]
        verbose_name = "Aarthik Barsa"
        verbose_name_plural = "Aarthik Barsa"

    def __str__(self):
        return self.aarthik_barsa
    
    

