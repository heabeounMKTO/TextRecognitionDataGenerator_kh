from trdg.computer_text_generator import _generate_horizontal_text

font = "E:\\khocr\\fonts\\km\\NotoSansKhmer.ttf"
text = "ដួងចន្ទ្រ"
_img, _mask = _generate_horizontal_text(
    text,
    font,
    "black",
    32,
    1,
    3,
    False,
    True
)

_img.save(f"{text}.png", "png")