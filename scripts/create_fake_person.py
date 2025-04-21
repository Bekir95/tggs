from faker import Faker
from company.models import OrganizationalUnit, Person

fake = Faker()

# Mevcut tüm organizasyon birimlerini al
organizational_units = OrganizationalUnit.objects.all()

# Her bir organizasyon birimi için sahte kişiler oluştur
for unit in organizational_units:
    for _ in range(3):  # Her bir birime 3 kişi ekle
        Person.objects.create(
            full_name=fake.name(),
            title=fake.job(),
            unit=unit  # Bu kişinin birimi mevcut organizasyon birimi olacak
        )

print("Sahte kişiler başarıyla eklendi!")