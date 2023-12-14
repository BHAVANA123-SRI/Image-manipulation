import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import io
from base64 import b64encode

st.markdown("<h1 style='text-align: center; font-size:40px; color: black;'>Image operations📸</h1>", unsafe_allow_html=True)
img_path = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
operation = st.selectbox("Select Operation", ["Enhance", "Filter", "Resize", "Crop"])


final_image = None  # Initialize final_image outside the if conditions

if img_path is not None:
    img = Image.open(img_path)

    if operation == "Enhance":
        enhancement_factor = st.slider("Select enhancement factor", 1.0, 3.0, 2.0)
        enhancer = ImageEnhance.Color(img)
        enhanced_image = enhancer.enhance(enhancement_factor)
        st.image(enhanced_image, caption="Enhanced Image", use_column_width=True)
        final_image = enhanced_image  # Set final_image after the operation

    elif operation == "Filter":
        selected_filter = st.selectbox("Select Filter", ["BLUR", "CONTOUR", "FIND_EDGES", "EMBOSS"])
        filter_image = img.filter(getattr(ImageFilter, selected_filter))
        st.image(filter_image, caption=f"{selected_filter} Filtered Image", use_column_width=True)
        final_image = filter_image  # Set final_image after the operation

    elif operation == "Resize":
        new_width = st.text_input("Enter new width")
        new_height = st.text_input("Enter new height")

        if new_width.isdigit() and new_height.isdigit():
            new_width = int(new_width)
            new_height = int(new_height)

            resized_image = img.resize((new_width, new_height))
            st.image(resized_image, caption="Resized Image", use_column_width=True)
            final_image = resized_image  # Set final_image after the operation

    elif operation == "Crop":
        left = st.number_input("Left:", 0, img.width, 0)
        top = st.number_input("Top:", 0, img.height, 0)
        right = st.number_input("Right:", 0, img.width, img.width)
        bottom = st.number_input("Bottom:", 0, img.height, img.height)

        cropped_image = img.crop((left, top, right, bottom))
        st.image(cropped_image, caption="Cropped Image", use_column_width=True)
        final_image = cropped_image  # Set final_image after the operation

    # Download button for the final processed image
    if final_image is not None:
        download_button_label = f"Download {operation} Image"
        download_button_key = f"download_{operation.lower()}_image"

        final_image_bytes = io.BytesIO()
        final_image.save(final_image_bytes, format='PNG')
        final_image_data = final_image_bytes.getvalue()

        st.markdown(f'<a href="data:file/png;base64,{b64encode(final_image_data).decode()}" download="{operation.lower()}_image.png">{download_button_label}</a>', unsafe_allow_html=True)
