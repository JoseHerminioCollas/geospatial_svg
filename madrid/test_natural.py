from madrid.natural import natural
# extent = (-4.0699641, -3.2300143, 40.170042, 40.6499669)
#     -4.0, 40.3 
data_path = 'data/Madrid-shp/shape/natural.shp'


def test_natural():
    n = natural(1, 2000, data_path, '', -4.0, 40.3, 0.2)
    assert n
