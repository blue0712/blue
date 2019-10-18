radius = 5
area = radius * radius * 3.14
str1 = 'radius=%d, area=%f'
print(str1 % (radius, area))
str2 = 'radius=%d, area=%.2f'
print(str2 % (radius, area))
str3 = 'radius={}, area={}'
print(str3.format(radius, area))
str4 = 'radius={}, area={:.2f}'
print(str4.format(radius, area))
str5 = 'radius={1:}, area={0:.3f}'
print(str5.format(area, radius))
str6 = 'radius={r:}, area={a:.2f}'
print(str6.format(r=radius, a=area))
print(f'radius={radius:}, area={area:.2f}')
x = True
y = 'OK'
z = 3.14
p = 5
q = 3 + 2j
print('x=%s,y=%s,z=%.3f,p=%d,q=%s' % (x, y, z, p, q))
print(f'x={x},y={y},z={z:.3f},p={p},q={q}')