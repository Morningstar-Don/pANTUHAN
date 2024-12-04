import streamlit as st
from PIL import Image

# Title of the biography blog
st.title("Donna Biography Blog")
st.write("Welcome to my personal biography page! Learn more about me below.")

# Profile Section
st.header("About Me")
st.write("Hello! I'm **Donalyn S. Pantuhan**, a 19-year-old student currently pursuing a Bachelor of Science in Computer Engineering (BSCpE) in **1B**.")
st.write("I am passionate about technology, learning, and making meaningful contributions to my community.")

# Adding a placeholder for a profile picture (optional)
profile_pic = st.file_uploader("Upload Your Profile Picture", type=["jpg", "jpeg", "png"])
if profile_pic is not None:
    image = Image.open(profile_pic)
    st.image(image, caption="Donalyn S. Pantuhan", use_column_width=True)

# Skills and Hobbies
st.header("Skills and Hobbies")
st.write("- Coding and programming")
st.write("- Problem-solving and critical thinking")
st.write("- Volunteering in community service")
st.write("- Exploring new technologies")
st.write("- Creative writing and blogging")

# Achievements
st.header("Achievements")
st.write("- Graduated with **High Honors**")
st.write("- Active participant in **Community Service** projects and events")
st.write("- Recognized for leadership and teamwork skills")

# Biography Summary
st.header("Biography Summary")
st.write("""
Hi, I'm Donalyn, a dedicated Computer Engineering student with a strong passion for technology and a deep commitment to making a positive impact on my community. 
I have consistently excelled academically, graduating with high honors, and actively participating in community service initiatives. 
I enjoy learning new skills, tackling challenges, and collaborating with others to achieve meaningful results. 
My dream is to become a successful computer engineer, making a difference in the world through innovation and dedication.
""")

# Footer
st.write("---")
st.write("Thank you for visiting my biography blog! Feel free to reach out or connect with me.")
