from django.db import models
from django.conf import settings


from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)

    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("staff", "Staff"),
        ("citizen", "Citizen"),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="citizen"
    )

    def __str__(self):
        return self.username

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
    current_ward = models.IntegerField()
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
    rayak_khand_no = models.IntegerField()
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



# Settings model fields
class karmachari(models.Model):
    id = models.AutoField(primary_key=True)
    ward = models.CharField(max_length=255)
    prakar = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    padh = models.CharField(max_length=20)
    samparka = models.IntegerField()
    photo = models.ImageField(upload_to="identity_cards/photos/")
    action = models.CharField(max_length=50)


class woda(models.Model):
    id = models.AutoField(primary_key=True)
    woda_name = models.CharField(max_length=255)
    woda_no = models.IntegerField(max_length=255)
    address = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=20)
    karya = models.CharField(max_length=255)
    nagarpalika = models.CharField(max_length=50)


class pratinidhi(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255)
    padh = models.CharField(max_length=255)
    gender = models.CharField(max_length=20)
    dateOfBirth = models.DateField()    
    contact_no = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="identity_cards/photos/")
    rastriya_parichaya_patra = models.CharField(max_length=255)
    woda = models.ForeignKey(woda, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)

class patraKoKisim(models.Model):
    id = models.AutoField(primary_key=True)
    patra_ko_kisim = models.CharField(max_length=255)
    action = models.CharField(max_length=50)

class sakha_thapnuhos(models.Model):
    id = models.AutoField(primary_key=True)
    sakha = models.CharField(max_length=255)
    karya = models.CharField(max_length=50)

class sadasya_thapnuhos(models.Model):
    id = models.AutoField(primary_key=True)
    sadasya = models.CharField(max_length=255)
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
    


class Province(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class District(models.Model):
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
        related_name="districts"
    )
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ("province", "name")

    def __str__(self):
        return self.name


class Municipality(models.Model):

    MUNICIPALITY_TYPES = (
        ("mahanagarpalika", "Mahanagarpalika"),
        ("upamahanagarpalika", "Upa-Mahanagarpalika"),
        ("nagarpalika", "Nagarpalika"),
        ("gaupalika", "Gaupalika"),
    )

    district = models.ForeignKey(
        District,
        on_delete=models.CASCADE,
        related_name="municipalities"
    )

    name = models.CharField(max_length=150)

    municipality_type = models.CharField(
        max_length=30,
        choices=MUNICIPALITY_TYPES
    )

    def __str__(self):
        return f"{self.name} ({self.get_municipality_type_display()})"


class Ward(models.Model):
    municipality = models.ForeignKey(
        Municipality,
        on_delete=models.CASCADE,
        related_name="wards"
    )

    ward_no = models.PositiveIntegerField()

    class Meta:
        unique_together = ("municipality", "ward_no")

    def __str__(self):
        return f"{self.municipality.name} - Ward {self.ward_no}"
    
    

from django.db import models


# =========================
# 1. FARMER (USER ENTITY)
# =========================
class Farmer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    ward_no = models.IntegerField()

    def __str__(self):
        return self.name


# =========================
# 2. LAND / FARM FIELD
# =========================
class Land(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name="lands")
    location = models.CharField(max_length=200)
    area = models.FloatField(help_text="Area in ropani/hectare")
    soil_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.location} - {self.farmer.name}"


# =========================
# 3. CROP MASTER
# =========================
class Crop(models.Model):
    name = models.CharField(max_length=100)
    season = models.CharField(max_length=50)  # summer, winter, monsoon
    duration_days = models.IntegerField()
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


# =========================
# 4. CROP PRODUCTION
# =========================
class CropProduction(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    land = models.ForeignKey(Land, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)

    planting_date = models.DateField()
    expected_harvest_date = models.DateField()
    quantity_produced = models.FloatField(null=True, blank=True)

    STATUS_CHOICES = [
        ("planted", "Planted"),
        ("growing", "Growing"),
        ("harvested", "Harvested"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="planted")

    def __str__(self):
        return f"{self.crop.name} - {self.farmer.name}"


# =========================
# 5. INVENTORY (SEED, FERTILIZER, TOOL)
# =========================
class Inventory(models.Model):
    ITEM_TYPES = [
        ("seed", "Seed"),
        ("fertilizer", "Fertilizer"),
        ("tool", "Tool"),
    ]

    name = models.CharField(max_length=100)
    item_type = models.CharField(max_length=20, choices=ITEM_TYPES)
    quantity = models.FloatField()
    unit = models.CharField(max_length=20)  # kg, pcs, liter
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name


# =========================
# 6. LIVESTOCK MODULE
# =========================
class Livestock(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)

    animal_type = models.CharField(max_length=50)  # cow, goat, buffalo
    count = models.IntegerField()

    health_status = models.CharField(max_length=100, default="healthy")
    vaccination_done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.animal_type} - {self.farmer.name}"


# =========================
# 7. SOIL ANALYSIS
# =========================
class SoilReport(models.Model):
    land = models.ForeignKey(Land, on_delete=models.CASCADE)

    ph_level = models.FloatField()
    nitrogen = models.FloatField()
    phosphorus = models.FloatField()
    potassium = models.FloatField()

    recommendation = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)


# =========================
# 8. SALES / MARKET MODULE
# =========================
class Sale(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)

    quantity = models.FloatField()
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    sold_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.crop.name} - {self.farmer.name}"


# =========================
# 9. CROP DISEASE / PEST
# =========================
class CropDisease(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    symptoms = models.TextField()
    solution = models.TextField()

    def __str__(self):
        return self.name


# =========================
# 10. WEATHER DATA (SMART FEATURE)
# =========================
class WeatherData(models.Model):
    location = models.CharField(max_length=100)

    temperature = models.FloatField()
    humidity = models.FloatField()
    condition = models.CharField(max_length=100)

    recorded_at = models.DateTimeField(auto_now_add=True)


# =========================
# 11. RECOMMENDATION SYSTEM
# =========================
class Recommendation(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)

    crop_suggestion = models.TextField()
    fertilizer_suggestion = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

class DeviceToken(models.Model):
    DEVICE_CHOICES = (
        ('android', 'Android'),
        ('ios', 'iOS'),
        ('web', 'Web'),
    )
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='devices', null=True, blank=True)
    fcm_token = models.TextField(unique=True)
    device_type = models.CharField(max_length=10, choices=DEVICE_CHOICES, default='android')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email if self.user else 'Guest'} - {self.device_type}"


class NotificationLog(models.Model):
    TARGET_CHOICES = (
        ('broadcast', 'Broadcast to All'),
        ('single', 'Single Device Test'),
    )
    
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='notifications/', null=True, blank=True)
    target_type = models.CharField(max_length=15, choices=TARGET_CHOICES)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
