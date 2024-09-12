def test_load_image():
    
    import src.imageprocessing as ip
    I = ip.load_image("images/northwestern.jpg")

    assert I.dtype == 'float32',"Image should be of type float32"
    assert I.shape == (1200, 2265, 3), "Shape should be 1200, 2265, 3)"

def test_crop_chicago():
    
    import src.imageprocessing as ip
    I = ip.load_image("images/northwestern.jpg")
    
    I_Chicago = ip.crop_chicago_from_northwestern(I)

    assert I_Chicago.dtype == 'float32',"Image should be of type float32"
    assert I_Chicago.shape == (250, 1000, 3), "Shape should be 1200, 2265, 3)"


def test_rgb_to_gray():
    
    import src.imageprocessing as ip

    I = ip.load_image("tests/test.png")
    
    I_gray = ip.convert_rgb2gray(I)
    
    


