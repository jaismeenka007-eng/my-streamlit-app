import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt  
#import seaborn as sns
#import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import base64

    # st.set_page_config(page_title="Diabetes Health Dashboard", layout="wide")

    # ========== 1. DATA LOAD ==========
@st.cache_data
def load_data():
    df = pd.read_csv("diabetes_dataset.csv") # file da naam same rakh
    df.columns = df.columns.str.strip().str.lower() # chote akhar kar ditte
    return df
st.set_page_config(page_title="Diabetes Health Indicator Analysis", page_icon=":bar_chart:", layout="wide")
df=pd.read_csv("diabetes_dataset.csv")
df.info()
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Data Overview", "Data Visualization","Dashboard","About"],
        icons=["house", "bar-chart","grid","graph-up","info-circle"],
        menu_icon="cast",
        default_index=0,
    )
  

import streamlit as st
import base64

def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("imgg.jpg")

st.markdown(f"""
<style>
/* Main Page */
.stApp {{
    background-image: url("data:image/jpeg;base64,{img}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

/* Sidebar Background */
[data-testid="stSidebar"] {{
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(12px);

    background-image: url("data:image/jpeg;base64,{img}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}

</style>
""", unsafe_allow_html=True)

if selected == "Home":
    st.markdown("<h1 style='color: black;'>🌎Diabetes Health Indicator Analysis</h1>", unsafe_allow_html=True)
    st.write("Diabetes Health Indicator Analysis is a data science project that analyzes health-related factors associated with diabetes using a real-world dataset. The project involves data cleaning, preprocessing, exploratory data analysis (EDA), and visualization to identify patterns and relationships between diabetes and indicators such as age, BMI, blood pressure, physical activity, smoking, and general health. The insights gained from the analysis can help improve awareness, support early risk identification, and assist healthcare professionals and policymakers in making informed decisions for diabetes prevention and management.")
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://cdn.vectorstock.com/i/1000v/98/20/diabetes-flat-infographics-vector-50749820.jpg",width=400)
    with col2:
        st.image("https://wallpaperaccess.com/full/3275630.jpg",width=400)
    st.subheader("🎯Objectives") 
    st.write("1. Analyze the relationship between various health indicators and diabetes risk.")
    st.write("2. Identify key factors that contribute to diabetes development.")    
    st.write("3. Provide actionable insights for diabetes prevention and management.")  
    st.subheader("✅Benefits")
    st.write("1. Early identification of at-risk individuals.")
    st.write("2. Improved understanding of diabetes risk factors.")
    st.write("3. Enhanced decision-making for healthcare professionals and policymakers.")
    
    st.subheader("📚Dataset Details:")
    st.write("Total Records: 253,680")
    st.write("Total Features: 22")
    st.write("Target Variable: Diabetes (0 = No Diabetes, 1 = Diabetes)")
    st.write("Data Type: Structured tabular data")
    st.write("Source: Kaggle Diabetes Health Indicators Dataset")

     
elif selected == "Data Overview":
    st.title("📈Data Overview")
    st.write("This section provides an overview of the diabetes dataset.")
    st.write("The dataset contains the following columns:")
    st.write(df.columns)
    st.write("The dataset contains", df.shape[0], "rows and", df.shape[1], "columns.")
    st.write("The dataset contains the following health indicators:")
    st.write(df.describe()) 
    st.dataframe(df,width="stretch")
    df=pd.read_csv("diabetes_dataset.csv")
    st.subheader("first 10 Records of the Dataset")
    st.dataframe(df.head(10),width="stretch")

    st.subheader("Data Cleaning")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Missing Values")
        missing_values = df.isnull().sum()
        st.dataframe(missing_values[missing_values > 0], width="stretch")

elif selected == "Data Visualization":
    st.title("Data Visualization")  
    st.set_page_config(page_title="Diabetes Dashboard", layout="wide")

    @st.cache_data
    def load_data():
     df = pd.read_csv("diabetes_dataset.csv")
     df.columns = df.columns.str.strip().str.lower()
     return df

    df = load_data()

    st.markdown("<h1>📊 Data Visualization</h1>", unsafe_allow_html=True)

    # 1. Age vs Diabetes Risk Score by Gender - Scatter Plot
    st.subheader("1. Age vs Diabetes Risk Score by Gender")
    fig1 = px.scatter(df, x='age', y='diabetes_risk_score', color='gender',
    color_discrete_sequence=['#FF6B6B', '#4ECDC4'], # Pink, Teal
    template="none", # background transparent rakhne ke liye
    size_max=10) # point ka size

    fig1.update_layout(
    paper_bgcolor='rgba(0,0,0,0)', 
    plot_bgcolor='rgba(0,0,0,0)', 
    font_color='black', # tera bg light aa isliye black
    xaxis_title="Age",
    yaxis_title="Diabetes Risk Score"
)
    st.plotly_chart(fig1, width='stretch')
    
    # 2. Age Distribution by Diabetes Stage - Box Plot
    st.subheader("2. Age Distribution by Diabetes Stage")
    fig2 = px.box(df, x='diabetes_stage', y='age', color='diabetes_stage',
    template="plotly_dark")
    fig2.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='white', showlegend=False)
    st.plotly_chart(fig2, width='stretch')


   # 3. correlation heatmap
    st.subheader("3. Correlation Heatmap")
    corr = df.select_dtypes(include='number').corr()
    fig3 = px.imshow(corr, text_auto=True, aspect="auto",
    color_continuous_scale='RdBu_r', template="plotly_dark")
    fig3.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color='white')
    st.plotly_chart(fig3, width='stretch')

    # 4. Alcohol Consumption vs Diabetes Risk by Gender - Scatter
    st.subheader("4. Alcohol Consumption vs Diabetes Risk Score by Gender")
    fig4 = px.scatter(df, x='alcohol_consumption_per_week', y='diabetes_risk_score', 
    color='gender', title="Alcohol vs Diabetes Risk Score by Gender",
    template="plotly_dark")
    fig4.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='white')
    st.plotly_chart(fig4, width='stretch')

   # 5. Smoking Status vs Diabetes Risk - Box Plot
    st.subheader("5. Smoking Status vs Diabetes Risk")
    fig5 = px.box(df, x='smoking_status', y='diabetes_risk_score', color='smoking_status',
    template="plotly_dark")
    fig5.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='white', showlegend=False)
    st.plotly_chart(fig5, width='stretch')

    # Graph 6: Scatterplot - Diabetes Stage vs Age by Gender
    st.subheader("6. Diabetes Stage vs Age by Gender")
    fig6 = px.scatter(df, x="diabetes_stage", y="age", color="gender",
    template="plotly_dark")
    fig6.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
    font_color='white', xaxis_tickangle=-45)
    st.plotly_chart(fig6, width='stretch')

    # Graph 7: Barplot - Alcohol vs Risk Score
    st.subheader("7. Alcohol Consumption vs Diabetes Risk Score")
    df_top10 = df.head(10) # tu .head(10) use kar rahi si
    fig7 = px.bar(df_top10, x="diabetes_risk_score", y="alcohol_consumption_per_week", color="gender",
    template="plotly_dark")
    fig7.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='white')
    st.plotly_chart(fig7, width='stretch')

   # Graph 8: Lineplot - Ethnicity vs Smoking Status
    st.subheader("8. Ethnicity vs Smoking Status")
    df_top10 = df.head(10)
    fig8 = px.line(df_top10, x="ethnicity", y="smoking_status", color="gender", markers=True,
    template="plotly_dark")
    fig8.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
    font_color='white', xaxis_tickangle=-45)
    st.plotly_chart(fig8, width='stretch')

   # Graph 9: Barplot - Diabetes Stage vs Risk Score by Gender
    st.subheader("9. Diabetes Stage vs Risk Score by Gender")
    fig9 = px.bar(df, x="diabetes_risk_score", y="diabetes_stage", color="gender",
    color_discrete_sequence=['#FF6B6B', '#4ECDC4', '#45B7D1'], # Pink, Teal, Blue
    template="none", # <-- plotly_white/dark hata de
    orientation='h',
    barmode="group")

    fig9.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',  # transparent
    plot_bgcolor='rgba(0,0,0,0)',   # transparent  
    font_color='black',             # text black rakh le taaki bg pe dikhe
    xaxis_title="Diabetes Risk Score",
    yaxis_title="Diabetes Stage"
)

    st.plotly_chart(fig9, width='stretch')

elif  selected== "Dashboard":
   st.set_page_config(page_title="Diabetes Health Dashboard", layout="wide")
   @st.cache_data
   def load_data():
     df = pd.read_csv("diabetes_dataset.csv")
     df.columns = df.columns.str.strip().str.lower()
     return df

   df = load_data()

   st.markdown("<h1>🏥 Diabetes Health Dashboard</h1>", unsafe_allow_html=True)

# ========== SIDEBAR - YEH LINE SAB TO ZARURI AA ==========
   st.sidebar.title("🔍 Controls")
   page = st.sidebar.radio("Go to Section:", # <-- YEH DEFINE KARNA HI PAUGA
   ["📊 Overview & Distribution", "👥 Demographics", "🏃 Lifestyle Factors", "📋 Full Data"])

   gender = st.sidebar.multiselect("Gender", df['gender'].unique(), default=df['gender'].unique())
   ethnicity = st.sidebar.multiselect("Ethnicity", df['ethnicity'].unique(), default=df['ethnicity'].unique())
   diabetes = st.sidebar.multiselect("Diabetes Stage", df['diabetes_stage'].unique(), default=df['diabetes_stage'].unique())

   df_f = df[
     (df['gender'].isin(gender)) &
     (df['ethnicity'].isin(ethnicity)) &
     (df['diabetes_stage'].isin(diabetes))
]

# ========== KPI ==========
   st.markdown("### 📊 Key Metrics")
   col1, col2, col3, col4 = st.columns(4)
   with col1: st.metric("Total Patients", f"{df_f.shape[0]:,}")
   with col2: st.metric("Average Age", f"{df_f['age'].mean():.1f} yrs")
   with col3:
     at_risk = df_f[df_f['diabetes_stage']!= 'No Diabetes'].shape[0]
     st.metric("% At Risk", f"{(at_risk/df_f.shape[0])*100:.1f}%" if df_f.shape[0]>0 else "0%")
   with col4: st.metric("Avg Diet Score", f"{df_f['diet_score'].mean():.1f}/10")

   st.divider()

# ========== SECTION 1: OVERVIEW ==========
   if page == "📊 Overview & Distribution": # <-- ab 'page' define aa
    st.markdown("### 📊 Overview & Distribution")
    col1, col2, col3 = st.columns(3) 

    with col1:
        fig1 = px.pie(df_f, names='diabetes_stage', hole=0.4, title="Diabetes Stage Distribution") # df_f use kar
        fig1.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color='white')
        st.plotly_chart(fig1,use_container_width=True)

    with col2:
        fig2 = px.histogram(df_f, x='age', color='diabetes_stage', nbins=15, title="Age Distribution") # df_f
        fig2.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color='white')
        st.plotly_chart(fig2,use_container_width=True)

# ========== SECTION 2: DEMOGRAPHICS ==========
   elif page == "👥 Demographics":
    st.markdown("### 👥 Demographics")
    col1, col2, col3 = st.columns(3)
    with col1:
        fig3 = px.bar(df_f['gender'].value_counts(), title="Gender")
        fig3.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color='white')
        st.plotly_chart(fig3, use_container_width=True)
    with col2:
        fig4 = px.bar(df_f['ethnicity'].value_counts(), title="Ethnicity")
        fig4.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color='white')
        st.plotly_chart(fig4, use_container_width=True)
    with col3:
        fig5 = px.bar(df_f['education_level'].value_counts(), title="Education")
        fig5.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color='white')
        st.plotly_chart(fig5, use_container_width=True)

# ========== SECTION 3: LIFESTYLE ==========
   elif page == "🏃 Lifestyle Factors":
    st.markdown("### 🏃 Lifestyle Factors")
    col1, col2 = st.columns(2)
    with col1:
        fig6 = px.pie(df_f, names='smoking_status', title="Smoking Status")
        fig6.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color='white')
        st.plotly_chart(fig6, use_container_width=True)
    with col2:
        fig7 = px.histogram(df_f, x='diet_score', nbins=10, title="Diet Score 0-10")
        fig7.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color='white')
        st.plotly_chart(fig7, use_container_width=True)

# ========== SECTION 4: DATA ==========
   elif page == "📋 Full Data":
    st.markdown("### 📋 Full Dataset")
    st.dataframe(df_f, use_container_width=True, height=500)

elif selected == "About":
   # ========== MAIN PAGE LOGIC ==========
   if selected == "Home": 
    st.title("🏠 Welcome to Diabetes Dashboard")
    st.write("Select any option from sidebar to start")

   elif selected == "Data Overview":
    # tere analysis wale charts/graph
    st.title("📊 Data Overview")
    
   elif selected == "Data Visualization":
    st.title("📈 Data Visualization")
    
   elif selected == "Dashboard":
    st.title("🏥 Dashboard")
    
   elif selected == "About": 
    st.title("ℹ️ About This Project")
    
    with st.container(border=True):
        st.markdown("### Diabetes Health Dashboard")
        st.write("""
        This interactive dashboard analyzes health indicators from a dataset of 100,000+ patient records 
        to identify key risk factors associated with diabetes. 
        
        The goal is to help understand how demographic and lifestyle factors contribute to diabetes risk.
        """)
        
        st.markdown("#### 🎯 Project Objectives")
        st.markdown("""
        - Visualize diabetes prevalence across different demographic groups
        - Analyze impact of lifestyle factors: Diet, Smoking, Physical Activity
        - Provide interactive filters to explore health data
        - Generate insights for preventive healthcare
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 📊 Features")
            st.markdown("""
            - **Home**: Project introduction
            - **Data Analysis**: Statistical insights
            - **Data Visualization**: Charts and graphs
            - **Dashboard**: Key metrics + filters
            - **About**: Project details
            """)
        with col2:
            st.markdown("#### 🛠️ Tech Stack")
            st.markdown("""
            - `Python`
            - `Pandas` for Data Processing  
            - `Streamlit` for Web App
            - `Plotly` / `Matplotlib` for Charts
            """)
        
        st.markdown("#### 🗃️ Dataset")
        st.write("- **Records**: 100,000+ patient entries")
        st.write("- **Features**: Age, Gender, Ethnicity, Diet, Smoking, etc")
        st.write("- **Source**: Public Health Indicators Dataset")
    
        st.divider()
        st.caption("© 2026 | Developed by [Jaismeen Kaur] | Data Visualization Project") 

  