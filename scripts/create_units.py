from company.models import OrganizationalUnit

def create_units():
    mutevelli = OrganizationalUnit.objects.create(name="Mutevelli Heyeti")

    danismanlar = OrganizationalUnit.objects.create(name="Danismanlar Kurulu", parent=mutevelli)
    yonetim = OrganizationalUnit.objects.create(name="Yonetim Kurulu", parent=mutevelli)
    hukuk = OrganizationalUnit.objects.create(name="Hukuk Musavirligi", parent=mutevelli)

    yuksek_istisare = OrganizationalUnit.objects.create(name="Yuksek Istisare Kurulu", parent=danismanlar)

    genel_mudurluk = OrganizationalUnit.objects.create(name="Genel Mudurluk", parent=yonetim)

    komisyonlar = OrganizationalUnit.objects.create(name="Komisyonlar", parent=genel_mudurluk)
    genel_sekreterlik = OrganizationalUnit.objects.create(name="Genel Sekreterlik", parent=genel_mudurluk)
    denetim_kurulu = OrganizationalUnit.objects.create(name="Denetim Kurulu", parent=genel_mudurluk)
    disiplin_kurulu = OrganizationalUnit.objects.create(name="Disiplin Kurulu", parent=genel_mudurluk)
    ic_denetim = OrganizationalUnit.objects.create(name="Ic Denetim ve Risk Yonetim Kurulu", parent=genel_mudurluk)

    OrganizationalUnit.objects.create(name="TUGGEV Gelisim Komisyonu", parent=komisyonlar)
    OrganizationalUnit.objects.create(name="TUGGEV Genclik Komisyonu", parent=komisyonlar)
    OrganizationalUnit.objects.create(name="TUGGEV Kadinlar Birligi Komisyonu", parent=komisyonlar)

    OrganizationalUnit.objects.create(name="On Büro", parent=genel_sekreterlik)
    OrganizationalUnit.objects.create(name="Evrak Kayit", parent=genel_sekreterlik)

    OrganizationalUnit.objects.create(name="Teftis Kurulu", parent=denetim_kurulu)
    OrganizationalUnit.objects.create(name="Ic Denetim", parent=denetim_kurulu)

    OrganizationalUnit.objects.create(name="Strateji", parent=ic_denetim)

    print("✅ Organizasyon yapisi basariyla olusturuldu!")

# Fonksiyonu dogrudan cagır:
if __name__ == "__main__":
    create_units()