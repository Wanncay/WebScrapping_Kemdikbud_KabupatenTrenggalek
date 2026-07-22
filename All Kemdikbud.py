import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# Daftar kecamatan
kecamatan_links = {
    "Kec. Panggul": "https://dapo.dikdasmen.go.id/sp/3/051701",
    "Kec. Trenggalek": "https://dapo.dikdasmen.go.id/sp/3/051711",
    "Kec. Pule": "https://dapo.dikdasmen.go.id/sp/3/051706",
    "Kec. Dongko": "https://dapo.dikdasmen.go.id/sp/3/051705",
    "Kec. Watulimo": "https://dapo.dikdasmen.go.id/sp/3/051703",
    "Kec. Munjungan": "https://dapo.dikdasmen.go.id/sp/3/051702",
    "Kec. Durenan": "https://dapo.dikdasmen.go.id/sp/3/051709",
    "Kec. Gandusari": "https://dapo.dikdasmen.go.id/sp/3/051708",
    "Kec. Tugu": "https://dapo.dikdasmen.go.id/sp/3/051712",
    "Kec. Pogalan": "https://dapo.dikdasmen.go.id/sp/3/051710",
    "Kec. Karangan": "https://dapo.dikdasmen.go.id/sp/3/051707",
    "Kec. Bendungan": "https://dapo.dikdasmen.go.id/sp/3/051713",
    "Kec. Suruh": "https://dapo.dikdasmen.go.id/sp/3/051714",
    "Kec. Kampak": "https://dapo.dikdasmen.go.id/sp/3/051704",
}

all_data = []

# Pilih semester 2024/2025 Ganjil
def pilih_semester():
    try:
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "selectSemester"))
        )
        dropdown.click()
        opsi = driver.find_element(By.XPATH, '//select[@id="selectSemester"]/option[@value="20241"]')
        opsi.click()
        print("🗓️ Semester 2024/2025 Ganjil dipilih")
        time.sleep(2)
    except Exception as e:
        print(f"⚠️ Gagal pilih semester: {e}")

# Pilih semua jenjang
def pilih_semua_jenjang():
    try:
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "selectJenjang"))
        )
        dropdown.click()

        # Trigger dulu dengan pilih SMP
        smp_option = driver.find_element(By.XPATH, '//select[@id="selectJenjang"]/option[@value="smp"]')
        smp_option.click()
        time.sleep(1)

        # Lalu pilih "Semua Jenjang"
        semua_option = driver.find_element(By.XPATH, '//select[@id="selectJenjang"]/option[text()="Semua Jenjang"]')
        semua_option.click()
        time.sleep(2)

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'table#dataTables tbody tr'))
        )

        print("📚 Semua jenjang dipilih")
    except Exception as e:
        print(f"⚠️ Gagal pilih semua jenjang: {e}")

# Ambil daftar sekolah di tabel
def extract_sekolah_links(url, nama_kec):
    driver.get(url)
    pilih_semester()
    pilih_semua_jenjang()

    rows = driver.find_elements(By.CSS_SELECTOR, 'table#dataTables tbody tr')
    sekolah_list = []

    for index, row in enumerate(rows, 1):
        try:
            cols = row.find_elements(By.TAG_NAME, "td")
            nama_sekolah = cols[1].text.strip()
            npsn = cols[2].text.strip()
            bp = cols[3].text.strip()
            status = cols[4].text.strip()
            pd = cols[7].text.strip()
            rombel = cols[8].text.strip()
            guru = cols[9].text.strip()
            sekolah_link = cols[1].find_element(By.TAG_NAME, "a").get_attribute("href")

            sekolah_list.append({
                "Kecamatan": nama_kec,
                "Nama Sekolah": nama_sekolah,
                "NPSN": npsn,
                "BP": bp,
                "Status": status,
                "PD": pd,
                "Rombel": rombel,
                "Guru": guru,
                "URL": sekolah_link
            })
        except Exception as e:
            print(f"❌ Gagal ambil sekolah ke-{index} di {nama_kec}: {e}")
            continue

    return sekolah_list

# Ambil info detail dari tab Kontak
def extract_kontak(link):
    try:
        driver.get(link)
        kontak_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="#kontak"]'))
        )
        kontak_tab.click()
        time.sleep(2)

        panel = driver.find_element(By.CSS_SELECTOR, '#kontak .panel-body')
        raw_html = panel.get_attribute("innerHTML")

        def ambil_isi(label):
            try:
                start = raw_html.index(f"<strong>{label} : </strong>") + len(f"<strong>{label} : </strong>")
                end = raw_html.index("</p>", start)
                return raw_html[start:end].strip()
            except:
                return ""

        return {
            "Alamat Lengkap": ambil_isi("Alamat"),
            "RT/RW": ambil_isi("RT / RW"),
            "Dusun": ambil_isi("Dusun"),
            "Desa/Kelurahan": ambil_isi("Desa / Kelurahan"),
            "Kecamatan Detil": ambil_isi("Kecamatan"),
            "Kabupaten": ambil_isi("Kabupaten"),
            "Provinsi": ambil_isi("Provinsi"),
            "Kode Pos": ambil_isi("Kode Pos"),
            "Lintang": ambil_isi("Lintang"),
            "Bujur": ambil_isi("Bujur"),
        }
    except Exception as e:
        print(f"⚠️ Gagal ambil kontak dari {link}: {e}")
        return {}

# 🚀 Eksekusi utama
for nama_kec, url in kecamatan_links.items():
    print(f"➡️ Mengambil daftar sekolah di {nama_kec}")
    sekolah_list = extract_sekolah_links(url, nama_kec)

    for sekolah in sekolah_list:
        print(f"   🔍 Ambil detail: {sekolah['Nama Sekolah']}")
        detail = extract_kontak(sekolah["URL"])
        sekolah.update(detail)
        all_data.append(sekolah)
        time.sleep(1)

# 💾 Simpan ke Excel
df = pd.DataFrame(all_data)
df.to_excel("data_semua_sekolah_trenggalek_ganjil.xlsx", index=False)
print("✅ Data berhasil disimpan ke data_sekolah_trenggalek.xlsx")

# ❌ Tutup browser
driver.quit()
