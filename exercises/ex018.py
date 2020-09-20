from math import sin, cos, radians, tan

degree = int(input('Type a value in degree :'))

print('Value of sin {:.4f}, cos {:.4f} and tg {:.4f} of {} degree'.format(sin(radians(degree)), \
    cos(radians(degree)), tan(radians(degree)), degree))
