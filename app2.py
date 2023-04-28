import qrcode
from PIL import Image
import streamlit as st

st.set_page_config(
    page_title="Generador QR | Serviplus",
    page_icon="⭐️")
col1, col2, col3 = st.columns((1,5,1))
col2.title("Generador de Codigos Qr")
def generate_qr_code():
    
    col2.write("")
    nombre = col2.text_input(label="Ingrese el nombre del Personal aqui:", value="", max_chars=None, key=None)
    if nombre == "":
        col2.write("Por favor introduce el nombre del Personal")
    else:
        Logo_link = 'Logo SP.png'
        logo = Image.open(Logo_link)
    
        basewidth = 65
        wpercent = (basewidth/float(logo.size[0]))
        hsize = int((float(logo.size[1])*float(wpercent)))
        logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
        QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    
        QRcode.add_data(nombre)
        QRcode.make()
        
        QRcolor = 'black'
        QRimg = QRcode.make_image(fill_color=QRcolor, back_color="white").convert('RGB')
    
        pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)
        QRimg.paste(logo, pos)
        
        col2.image(QRimg, width=300)
        col2.write(f"QR generado para {nombre}")
        img = f'{nombre}.png'
        QRimg.save(img)
        if col2.download_button("Descargar QR", open(img, 'rb').read(), file_name=f'{nombre}.png', mime='image/png'):
            col2.success("QR generado y descargado!")
            
generate_qr_code()
st.write("#")
st.write("#")
st.caption("APP creada por Gustavo Boada Coord de Datos.")
st.caption("Contactame [Linkdein](https://www.linkedin.com/in/gboada23/)")