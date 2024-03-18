def RGB_to_CMYK():
    while True:
        color_rgb={}
        print("RGB to CMYK Converter")
        r_val=((input("Enter the Red Color Value: ")))
        g_val=((input("Enter the Green Color Value: ")))
        b_val=((input("Enter the Blue Color Value: ")))
        color_rgb['Red']=int(r_val)
        color_rgb['Blue']=int(b_val)
        color_rgb['Green']=int(g_val)

        r_perc=(color_rgb['Red']/255)
        g_perc=(color_rgb['Green']/255)
        b_perc=(color_rgb['Blue']/255)
        k_perc=(1-max(r_perc,g_perc,b_perc))

        c_val=((1-r_perc-k_perc)/(1-k_perc)*100)
        m_val=((1-g_perc-k_perc)/(1-k_perc)*100)
        y_val=((1-b_perc-k_perc)/(1-k_perc)*100)
        k_val=k_perc*100

        color_cmyk={}
        color_cmyk['Cyan']=int(c_val)
        color_cmyk['Magenta']=int(m_val)
        color_cmyk['Yellow']=int(y_val)
        color_cmyk['Key (Black)']=int(k_val)

        print("CMYK Values:")
        print(f"Cyan: {color_cmyk['Cyan']}")
        print(f"Magenta: {color_cmyk['Magenta']}")
        print(f"Yellow: {color_cmyk['Yellow']}")
        print(f"Key (Black) : {color_cmyk['Key (Black)']}")
        cont=input("Continue? ")
        if cont in ['q','quit','Q']:
            break

RGB_to_CMYK()


        

