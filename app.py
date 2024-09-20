from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS --- #
#
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "NBL-CV.pdf"
profile_pic_file = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS --- #
PAGE_TITLE = "Digital CV | Nicolás Barceló"
PAGE_ICON = ":wave:"
NAME = "Nicolás Barceló"
DESCRIPTION = "Software Developer | AI Engineer"
EMAIL = "ferreret@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/ferreret/",
    "GitHub": "https://www.github.com/ferreret",
}
# CERTIFICATIONS = {}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC --- #
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic_file)

# --- HERO SECTION --- #
col1, col2 = st.columns(2, gap="small")

with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)

    st.write(f"📧 {EMAIL}")

    # --- SOCIAL LINKS --- #
    # st.write("#")
    cols = st.columns(len(SOCIAL_MEDIA))

    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        with cols[index]:
            st.markdown(f"[{platform}]({link})")

    st.download_button(
        label=" 📃 Download CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )


# --- ABOUT ME --- #
st.subheader("About Me")
st.write("---")
st.write(
    """
    Professional with over 25 years of experience in designing and developing innovative technological solutions. 
    My specialization focuses on implementing projects using .NET and C#, encompassing the creation of APIs, 
    document management, and process automation (RPA). In recent years, I have directed my career towards artificial intelligence, 
    applying Python in data recognition and natural language processing (NLP), as well as leading quality prediction initiatives 
    in industrial processes. 
    """
)

# --- WORK EXPERIENCE --- #
st.write("\n")
st.subheader("Work Experience")
st.write("---")
st.write("**Data and Documentation Technology Specialist | Tecnomedia Sistemas**")
st.write("11/2002 - Present")
st.write(
    """
    - ▶️ Development of document management applications using .NET with C# and SQL Server.
    - ▶️ Creation of desktop applications in C# (WinForms, WPF) for extraction, recognition, and data entry in document management systems, CRM, and ERP.
    - ▶️ Implementation of process automation solutions using C# and Python.
    - ▶️ Integration of web APIs with other systems (Minimal API, FastAPI).
    - ▶️ Design and optimization of document workflows, including digitization, indexing, and data capture, using third-party libraries and Azure AI.
    - ▶️ Development of barcode recognition, OCR, and ICR solutions for industrial processes.
    - ▶️ Leadership of quality prediction projects in the chemical industry.
    - ▶️ Development of content-based text classification applications (NLP).
    """
)

st.write("\n")  # Add space between experiences

st.write("**Programmer - Programmer Analyst | NexTReT**")
st.write("12/2000 - 11/2002")
st.write(
    """
    - ▶️ Consulting, development, implementation, and maintenance of technological solutions.
    - ▶️ Development of desktop applications in Visual Basic 6.0 and SQL Server for document management of an international insurance company.
    - ▶️ Creation of an ASP application with VBScript and SQL Server for customer management in a management agency.
    - ▶️ Development of a payroll and human resources management solution using PowerBuilder.
    """
)

st.write("\n")  # Add space between experiences

st.write("**Consultant | Datasix Sistemas**")
st.write("10/1999 - 12/2000")
st.write(
    """
    - ▶️ Design, development, and implementation of Business Intelligence projects.
    - ▶️ Customization and implementation of query tools, reports, and office automation integration using VBA.
    - ▶️ Design of multidimensional analysis applications and EIS systems with Visual Basic 6.0.
    - ▶️ Development of Data Warehouses and Data Marts on SQL Server.
    - ▶️ Training and certification of users in BI tools.
    """
)

# --- EDUCATION --- #
st.write("\n")
st.subheader("Education")
st.write("---")
st.write(
    """
    - 🎓 **Bachelor's Degree in Pyshics | Universitat de Barcelona (1999)**)
    - 🎓 **Master's Degree in Data Science and Big Data | IEBS Business School (11/2022 - 10/2023)**
    """
)

# --- Certifications --- #
st.write("\n")
st.subheader("Certifications")
st.write("---")
st.write(
    """
    - 🧠 Tensorflow developer certificate (2024)
    - ☁️ AZ-900 Azure Fundamentals
    - 🤖 AI-900 Azure AI Fundamentals
    - 🐍 PCEP-30-02 – Certified Entry-Level Python Programmer
    - 🐍 PCEP-31-03 – Certified Associate in Python
    """
)

# --- SKILLS --- #
st.subheader("\n")
st.subheader("Skills")
st.write("---")
st.write(
    """
    - 💬 Languages: Native Spanish and Catalan; Professional proficiency in English.
    - 💻 Programming: C#, VB.NET, WinForms, WPF, Web API, Minimal API.
    - ☁️ Cloud: Azure Functions, Azure AI.
    - 🐳 Containers: Docker.
    - 🧠 Artificial Intelligence and Machine Learning: Python, Scikit-learn, TensorFlow, Streamlit, YOLO.
    - 🗄️ Databases: SQL Server, Access.
    - 🔮 Prompt Engineering.
    """
)
