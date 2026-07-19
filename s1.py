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
        options=["Home", "Data Analysis", "Data Visualization","Dashboard","About"],
        icons=["house", "bar-chart-line", "bar-chart"],
        menu_icon="cast",
        default_index=0,
    )
if selected == "Home":
    st.markdown("<h1 style='color: red;'>🌎Diabetes Health Indicator Analysis</h1>", unsafe_allow_html=True)
    st.write("Di  abetes Health Indicator Analysis is a data science project that analyzes health-related factors associated with diabetes using a real-world dataset. The project involves data cleaning, preprocessing, exploratory data analysis (EDA), and visualization to identify patterns and relationships between diabetes and indicators such as age, BMI, blood pressure, physical activity, smoking, and general health. The insights gained from the analysis can help improve awareness, support early risk identification, and assist healthcare professionals and policymakers in making informed decisions for diabetes prevention and management.")
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://cdn.vectorstock.com/i/1000v/98/20/diabetes-flat-infographics-vector-50749820.jpg",width=400)
    with col2:
        st.image("https://wallpaperaccess.com/full/3275630.jpg",width=400)
    st.subheader("Objectives") 
    st.write("1. Analyze the relationship between various health indicators and diabetes risk.")
    st.write("2. Identify key factors that contribute to diabetes development.")    
    st.write("3. Provide actionable insights for diabetes prevention and management.")  
    st.subheader("Benefits")
    st.write("1. Early identification of at-risk individuals.")
    st.write("2. Improved understanding of diabetes risk factors.")
    st.write("3. Enhanced decision-making for healthcare professionals and policymakers.")
    st.markdown("<h1 style='color: red;'>📂 Dataset Overview</h1>", unsafe_allow_html=True)
    st.subheader("Dataset Details:")
    st.write("Total Records: 253,680")
    st.write("Total Features: 22")
    st.write("Target Variable: Diabetes (0 = No Diabetes, 1 = Diabetes)")
    st.write("Data Type: Structured tabular data")
    st.write("Source: Kaggle Diabetes Health Indicators Dataset")

     
elif selected == "Data Analysis":
    st.title("Data Analysis")
    st.write("This section provides a detailed analysis of the health indicators of diabetes patients.")
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

    # Graph 1: Pie Chart - Distribution of Ethnicity
    st.subheader("1. Distribution of Ethnicity")
    figsize = (2, 2)
    fig1, ax1 = plt.subplots(figsize=figsize)
    df['ethnicity'].value_counts().plot.pie(autopct='%1.1f%%', colors=sns.color_palette('Set2'), ax=ax1)
    ax1.set_title("Distribution of Ethnicity")
    ax1.set_ylabel('')
    st.pyplot(fig1)

    # Graph 2: Barplot - Diabetes Risk Score by Age and Gender
    st.subheader("2. Diabetes Risk Score by Age and Gender")
    figsize = (10, 6)
    fig2, ax2 = plt.subplots(figsize=figsize)
    sns.barplot(data=df.head(100), x="age", y="diabetes_risk_score", hue="gender", palette="Set1", ax=ax2)
    ax2.set_title("Diabetes Risk Score by Age and Gender")
    plt.xticks(rotation=45 )
    st.pyplot(fig2)

    # Graph 3: Heatmap - Correlation
    st.subheader("3. Correlation Heatmap")
    fig3, ax3 = plt.subplots(figsize=(8,6))
    corr = df[['age', 'physical_activity_minutes_per_week', 'diabetes_risk_score']].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax3)
    ax3.set_title("Correlation between Age, Activity, Risk Score")
    st.pyplot(fig3)

    # Graph 4: Histogram - Distribution of Age
    st.subheader("4. Distribution of Age")
    fig4, ax4 = plt.subplots()
    ax4.hist(df['age'], bins=20, color='skyblue', edgecolor='black')
    ax4.set_xlabel('Age')
    ax4.set_ylabel('Frequency')
    ax4.set_title('Distribution of Age')
    st.pyplot(fig4)

    # Graph 5: Lineplot - Diabetes Risk Score by Age and Gender
    st.subheader("5. Diabetes Risk Trend by Age")
    fig5, ax5 = plt.subplots(figsize=(10,6))
    sns.lineplot(data=df.head(100), x="age", y="diabetes_risk_score", hue="gender", palette="Set1", ax=ax5)
    ax5.set_title("Diabetes Risk Score by Age and Gender")
    st.pyplot(fig5)

    # Graph 6: Scatterplot - Diabetes Stage vs Age
    st.subheader("6. Diabetes Stage vs Age by Gender")
    fig6, ax6 = plt.subplots(figsize=(10,6))
    sns.scatterplot(data=df, x="diabetes_stage", y="age", hue="gender", palette="Set1", ax=ax6)
    ax6.set_title("Age Distribution across Diabetes Stages")
    plt.xticks(rotation=45)
    st.pyplot(fig6)

    # Graph 7: Barplot - Alcohol vs Risk Score
    st.subheader("7. Alcohol Consumption vs Diabetes Risk Score")
    fig7, ax7 = plt.subplots(figsize=(10,6))
    sns.barplot(data=df.head(10), x="diabetes_risk_score", y="alcohol_consumption_per_week", hue="gender", palette="Set1", ax=ax7)
    ax7.set_title("Alcohol Consumption vs Risk Score")
    st.pyplot(fig7)

    # Graph 8: Lineplot - Ethnicity vs Smoking Status
    st.subheader("8. Ethnicity vs Smoking Status")
    fig8, ax8 = plt.subplots(figsize=(10,6))
    sns.lineplot(data=df.head(10), x="ethnicity", y="smoking_status", hue="gender", palette="Set1", ax=ax8)
    ax8.set_title("Smoking Status by Ethnicity")
    plt.xticks(rotation=45)
    st.pyplot(fig8)

    # Graph 9: Barplot - Diabetes Stage vs Risk Score
    st.subheader("9. Diabetes Stage vs Risk Score by Gender")
    fig9, ax9 = plt.subplots(figsize=(10,6))
    sns.barplot(data=df, x="diabetes_risk_score", y="diabetes_stage", hue="gender", ax=ax9)
    ax9.set_title("Risk Score across Diabetes Stages")
    st.pyplot(fig9)

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
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.pie(df_f, names='diabetes_stage', hole=0.4, title="Diabetes Stage Distribution") # df_f use kar
        fig1.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color='white')
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = px.histogram(df_f, x='age', color='diabetes_stage', nbins=15, title="Age Distribution") # df_f
        fig2.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color='white')
        st.plotly_chart(fig2, use_container_width=True)

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

   elif selected == "Data Analysis":
    # tere analysis wale charts/graph
    st.title("📊 Data Analysis")
    
   elif selected == "Data Visualization":
    st.title("📈 Data Visualization")
    
   elif selected == "Dashboard":
    st.title("🏥 Dashboard")
    
   elif selected == "About": # YE WALA NAVA PAGE AA
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
        st.caption("© 2025 | Developed by [Your Name] | Data Visualization Project") 

  