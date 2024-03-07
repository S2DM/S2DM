import imageio.v3 as iio
from pathlib import Path

folder = Path("./")

for file in folder.glob("*.gif"):
    img = iio.imread(file)
    print(img.shape)
    iio.imwrite(file.name, img, loop=0)