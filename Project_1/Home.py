import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter

st.markdown("<h1 style='text-align: center; font-size:40px; color: black;'>Image operations📸</h1>", unsafe_allow_html=True)


img_path = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
operation = st.selectbox("Select Operation", ["Enhance", "Filter", "Resize", "Crop"])


final_image = None  # Initialize final_image outside the if conditions

if img_path is not None:
    img = Image.open(img_path)

    if operation == "Enhance":
        enhancement_factor = 2.5
        enhancer = ImageEnhance.Color(img)
        enhanced_image = enhancer.enhance(enhancement_factor)
        st.image(enhanced_image, caption="Enhanced Image", use_column_width=True)
        final_image = enhanced_image  # Set final_image after the operation

    elif operation == "Filter":
        blur_image = img.filter(ImageFilter.BLUR)
        contour_image = img.filter(ImageFilter.CONTOUR)
        find_edges_image = img.filter(ImageFilter.FIND_EDGES)
        emboss_enhance_image = img.filter(ImageFilter.EMBOSS)

        col1, col2 = st.columns(2)
        col1.image(blur_image, caption="Blur Filtered Image", use_column_width=True)
        col1.image(contour_image, caption="Contour Filtered Image", use_column_width=True)
        col2.image(find_edges_image, caption="Find Edges Filtered Image", use_column_width=True)
        col2.image(emboss_enhance_image, caption="Emboss Filtered Image", use_column_width=True)

        final_image = emboss_enhance_image  # Set final_image after the operations

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
    download_button = st.download_button(label="Download Final Processed Image", data=final_image.tobytes(), file_name="final_processed_image.png", key="download_final_image")
