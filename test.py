color_rgb={}
print("RGB to CMYK Converter")
r_val=int((input("Enter the Red Color Value: ")))
g_val=int((input("Enter the Green Color Value: ")))

b_val=int((input("Enter the Blue Color Value: ")))
color_rgb['Red']=r_val
color_rgb['Blue']=b_val
color_rgb['Green']=g_val
r_perc=(int(r_val)/255)
g_perc=(int(g_val)/255)
b_perc=(int(g_val/255))
k_perc=(1-max(r_perc,g_perc,b_perc))
c_val=((1-r_perc-k_perc)/(1-k_perc)*100)
m_val=((1-g_perc-k_perc)/(1-k_perc)*100)
y_val=((1-b_perc-k_perc)/(1-k_perc)*100)
k_val=k_perc*10
color_cmyk={}
color_cmyk['Cyan']=c_val
color_cmyk['Magenta']=m_val
color_cmyk['Yellow']=y_val
color_cmyk['Key (Black)']=k_val

print(color_rgb)
print(color_cmyk)