import os

def test_index_exists():
    assert os.path.exists("index.html"), "File index.html tidak ditemukan."

def test_content():
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()
    assert "NIM" in content, "Halaman tidak memuat kata 'NIM'"
    assert "Nama" in content, "Halaman tidak memuat kata 'Nama'"

if __name__ == "__main__":
    test_index_exists()
    test_content()
    print("✅ Semua tes berhasil!")
