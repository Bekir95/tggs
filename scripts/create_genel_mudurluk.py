from company.models import OrganizationalUnit

def create_genel_mudurluk_yapisi():
    genel_mudurluk = OrganizationalUnit.objects.create(name="GENEL MUDURLUK")
    
    genel_mudur = OrganizationalUnit.objects.create(name="GENEL MUDUR", parent=genel_mudurluk)
    genel_mudur_yardimcisi = OrganizationalUnit.objects.create(name="GENEL MUDUR YARDIMCISI", parent=genel_mudurluk)
    ozel_kalem = OrganizationalUnit.objects.create(name="OZEL KALEM MUDURU", parent=genel_mudurluk)

    # Genel Mudur alti
    idari_daire = OrganizationalUnit.objects.create(name="IDARI YONETIM VE GELISIM DAIRE BASKANLIGI", parent=genel_mudur)
    OrganizationalUnit.objects.create(name="IDARI YONETIM VE GELISIM DAIRE BASKANI", parent=idari_daire)
    OrganizationalUnit.objects.create(name="YONETIM HIZMETLERI", parent=idari_daire)

    teskilat_daire = OrganizationalUnit.objects.create(name="TESKILAT DAIRE BASKANLIGI", parent=genel_mudur)
    OrganizationalUnit.objects.create(name="TESKILAT DAIRE BASKANI", parent=teskilat_daire)
    OrganizationalUnit.objects.create(name="TEMSILCI LIKLER", parent=teskilat_daire)
    OrganizationalUnit.objects.create(name="SUBELER", parent=teskilat_daire)
    OrganizationalUnit.objects.create(name="IRTIBAT BUROLARI", parent=teskilat_daire)

    kultur_daire = OrganizationalUnit.objects.create(name="KULTUR, SANAT VE TURIZM DAIRE BASKANLIGI", parent=genel_mudur)
    OrganizationalUnit.objects.create(name="KULTUR, SANAT VE TURIZM DAIRE BASKANI", parent=kultur_daire)

    proje_daire = OrganizationalUnit.objects.create(name="PROJE VE YATIRIM DAIRE BASKANLIGI", parent=genel_mudur)
    OrganizationalUnit.objects.create(name="PROJE VE YATIRIM DAIRE BASKANI", parent=proje_daire)
    OrganizationalUnit.objects.create(name="PROJE MUDURU", parent=proje_daire)
    OrganizationalUnit.objects.create(name="YATIRIM UZMANI", parent=proje_daire)
    OrganizationalUnit.objects.create(name="AR-GE UZMANI", parent=proje_daire)

    personel_daire = OrganizationalUnit.objects.create(name="PERSONEL DAIRE BASKANLIGI", parent=genel_mudur)
    OrganizationalUnit.objects.create(name="PERSONEL DAIRE BASKANI", parent=personel_daire)
    OrganizationalUnit.objects.create(name="INSAN KAYNAKLARI UZMANI", parent=personel_daire)

    # Genel Mudur Yardimcisi alti
    disiliskiler_daire = OrganizationalUnit.objects.create(name="DIS ILISKILER DAIRE BASKANLIGI", parent=genel_mudur)
    OrganizationalUnit.objects.create(name="DIS ILISKILER DAIRE BASKANI", parent=disiliskiler_daire)
    OrganizationalUnit.objects.create(name="YURTDISI PROJE UZMANI", parent=disiliskiler_daire)
    OrganizationalUnit.objects.create(name="YURTDISI TURK TOPLULUKLARI", parent=disiliskiler_daire)
    OrganizationalUnit.objects.create(name="YURTDISI MUSLUMAN TOPLULUKLARI", parent=disiliskiler_daire)
    OrganizationalUnit.objects.create(name="YURTDISI KULTUREL HIZMETLER UZMANI", parent=disiliskiler_daire)

    strateji_daire = OrganizationalUnit.objects.create(name="STRATEJI GELISTIRME DAIRE BASKANLIGI", parent=genel_mudur)
    OrganizationalUnit.objects.create(name="STRATEJI GELISTIRME DAIRE BASKANI", parent=strateji_daire)
    OrganizationalUnit.objects.create(name="STRATEJIK PLAN UZMANI", parent=strateji_daire)

    mali_daire = OrganizationalUnit.objects.create(name="MALI ISLER DAIRE BASKANLIGI", parent=genel_mudur)
    OrganizationalUnit.objects.create(name="MALI ISLER DAIRE BASKANI", parent=mali_daire)
    OrganizationalUnit.objects.create(name="MUHASEBE UZMANI", parent=mali_daire)
    OrganizationalUnit.objects.create(name="GENEL TAHSILAT UZMANI", parent=mali_daire)

    isletme_daire = OrganizationalUnit.objects.create(name="ISLETME ISLERI DAIRE BASKANLIGI", parent=genel_mudur)
    OrganizationalUnit.objects.create(name="ISLETME ISLERI DAIRE BASKANI", parent=isletme_daire)
    OrganizationalUnit.objects.create(name="ISLETME MUDURU", parent=isletme_daire)
    OrganizationalUnit.objects.create(name="ISLETME UZMANI", parent=isletme_daire)

    kalite_daire = OrganizationalUnit.objects.create(name="KALITE YONETIMI DAIRE BASKANLIGI", parent=genel_mudur)
    OrganizationalUnit.objects.create(name="KALITE YONETIMI DAIRE BASKANI", parent=kalite_daire)
    OrganizationalUnit.objects.create(name="KALITE YONETIM UZMANI", parent=kalite_daire)
    OrganizationalUnit.objects.create(name="KALITE KONTROL UZMANI", parent=kalite_daire)

    sivil_daire = OrganizationalUnit.objects.create(name="SIVIL TOPLUM ILISKILERI DAIRE BASKANLIGI", parent=genel_mudur)
    OrganizationalUnit.objects.create(name="VAKIFLAR", parent=sivil_daire)
    OrganizationalUnit.objects.create(name="DERNEKLER, FEDERASYONLAR, KONFEDERASYONLAR", parent=sivil_daire)
    OrganizationalUnit.objects.create(name="SIYASI PARTILER", parent=sivil_daire)
    OrganizationalUnit.objects.create(name="MULKI IDARE AMIRLERI", parent=sivil_daire)

    spor_daire = OrganizationalUnit.objects.create(name="SPOR VE SOSYAL HIZMETLER DAIRE BASKANLIGI", parent=genel_mudur)
    OrganizationalUnit.objects.create(name="SPOR BILIMLERI DAIRE BASKANI", parent=spor_daire)
    OrganizationalUnit.objects.create(name="SOSYAL HIZMETLER DAIRE BASKANI", parent=spor_daire)
    OrganizationalUnit.objects.create(name="SPORTIF VE SOSYAL HIZMETLER PROJE UZMANI", parent=spor_daire)

    basin_daire = OrganizationalUnit.objects.create(name="BASIN VE HALKLA ILISKILER DAIRE BASKANLIGI", parent=genel_mudur)
    OrganizationalUnit.objects.create(name="BASIN VE HALKLA ILISKILER DAIRE BASKANI", parent=basin_daire)
    OrganizationalUnit.objects.create(name="BASIN VE YAYIN UZMANI", parent=basin_daire)
    OrganizationalUnit.objects.create(name="HALKLA ILISKILER UZMANI", parent=basin_daire)

    bilisim_daire = OrganizationalUnit.objects.create(name="BILISIM TEKNOLOJILERI DAIRE BASKANLIGI", parent=genel_mudur)
    OrganizationalUnit.objects.create(name="BILISIM TEKNOLOJILERI DAIRE BASKANI", parent=bilisim_daire)
    OrganizationalUnit.objects.create(name="BILISIM UZMANI", parent=bilisim_daire)
    OrganizationalUnit.objects.create(name="TANITIM VE MEDYA UZMANI", parent=bilisim_daire)

    print("✅ TUM organizasyon yapisi basariyla olusturuldu!")




# Fonksiyonu dogrudan cagır:
if __name__ == "__main__":
    create_genel_mudurluk_yapisi()