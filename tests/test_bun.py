from praktikum.bun import Bun

def test_bun_creation():
    bun = Bun(name="Sesame Bun", price=50.0)
    assert bun.get_name() == "Sesame Bun"
    assert bun.get_price() == 50.0
