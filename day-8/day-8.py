d = open('input').read().strip()

w = 25
h = 6
num_layers = len(d)//(w*h)
# get layers
layers = [d[w*h*i:w*h*(i+1)] for i in range(num_layers)]

# part 1
z = [s.count('0') for s in layers]
min_idx = z.index(min(z))
s = layers[min_idx]
print('part 1', s.count('1')*s.count('2'))

# part 2
from PIL import Image
img = Image.new('1', (w, h))
for c in reversed(layers):
    for y in range(h):
        for x in range(w):
            p = c[25*y+x]
            if p == '2': continue
            img.putpixel((x, y), int(p))
f = 'bios-pw.png'
img.save(f)
print('part 2', f)
