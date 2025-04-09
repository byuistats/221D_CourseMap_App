import streamlit as st

st.title("Introductory Statistics Course Map")

# Create tabs
tab1, tab2 = st.tabs(["Course Map", "Data Wrangling"])

# Tab 1: Decision Tree
with tab1:
    st.image("https://github.com/byuistats/221D_CourseMap_App/raw/main/images/statistics_decision_treeV2.png", caption="Statistics Decision Tree", use_container_width=True)

    # --- Decision 1: Response Variable Type ---
    response_type = st.radio("What is your Response variable?", ("Quantitative", "Categorical"))

    if response_type == "Quantitative":
        # --- Decision 2: Explanatory Variable Type (Quantitative Response) ---
        explanatory_type_quant = st.radio("What is your Explanatory Variable?", ("None", "Categorical", "Quantitative"))

        if explanatory_type_quant == "None":
            st.write("### Descriptive Statistics")
            st.write("Mean, Median, Mode, Standard Deviation, Percentiles")
            st.write("Graph: Histogram")
            st.image("https://github.com/byuistats/Math221D_Cannon/raw/master/Images/histogramggplotgallery1.png", caption="Histogram Example", width=200)
            st.write("R Code: ```\n summary(data)```")
            st.write("R Code: ```\n ggplot(data, aes(x = value)) + geom_histogram(binwidth = 1)```")
            st.write("### Inferential Statistics") 
            st.write("One-sample t-test")
            st.write("R Code: ```\n t.test(value)```")

        elif explanatory_type_quant == "Categorical":
            st.write("### Descriptive Statistics")
            st.write("Grouped Means, Medians, Standard Deviations, Percentiles")
            st.write("Graph: Side-by-side Boxplot")
            st.write("R Code: ```\n ggplot(data, aes(x = group, y = value)) + geom_boxplot()```")
            st.image("https://github.com/byuistats/Math221D_Cannon/raw/master/Images/boxplotggplotgallery1.png", caption="Boxplot Example", width=300)
            how_many_groups = st.radio("How Many Groups?", ("2 Dependent Groups", "2 Independent Groups", "3+ Independent Groups"))

            if how_many_groups == "2 Dependent Groups":
                st.write("### Inferential Statistics")
                st.write("Paired t-test")
                st.write("R Code: ```\n t.test(data$value1-data$value2, alternative = \"two.sided\")```")
                st.write("Matched Pairs t-test")
            elif how_many_groups == "2 Independent Groups":
                st.write("### Inferential Statistics")
                st.write("Independent 2-sample t-test")
                st.write("2-sample t-test")
                st.write("R Code: ```\n t.test(value ~ group, data = data)```")
            elif how_many_groups == "3+ Independent Groups":
                st.write("### Inferential Statistics")
                st.write("ANOVA")
                st.write("R Code: ```\n aov_output <- aov(value ~ group, data = data) \n summary(aov_output)```")
                st.write("F-Statistic")

        elif explanatory_type_quant == "Quantitative":
            st.write("### Descriptive Statistics")
            st.write("Graph: Scatter plot, geom_smooth(method = 'lm')")
            st.write("R Code: ```\n ggplot(data, aes(x = x, y = y)) + geom_point() + geom_smooth(method = 'lm')```")
            st.image("https://github.com/byuistats/Math221D_Cannon/raw/master/Images/Regression_Line_Example.png", caption="Boxplot Example", width=200)
            st.write("Correlation Coefficient (r)")
            st.write("R Code:  ```\n cor(data$x, data$y)```")
            st.write("### Inferential Statistics")
            st.write("Simple Linear Regression")
            st.write("R Code:  ```lm_output <- lm(y ~ x)  \n summary(lm_output)```")

    elif response_type == "Categorical":
        explanatory_type_cat = st.radio("What is your Explanatory Variable?", ("None", "2 Levels", "Multiple Levels"))

        if explanatory_type_cat == "None":
            st.write("### Descriptive Statistics")
            st.write("Frequency Table")
            st.write("Proportion (p)")
            st.write("Graphs: Bar chart")
            st.write("### Inferential Statistics")
            st.write("One-sample proportion test")
            st.write("R Code:  ```\n prop.test(x, n, p = NULL, alternative = \"two.sided\", conf.level = 0.95)```")

        elif explanatory_type_cat == "2 Levels":
            st.write("### Descriptive Statistics")
            st.write("Frequency Table")
            st.write("Proportions (p1, p2)")
            st.write("Graphs: Clustered bar chart")
            st.write("### Inferential Statistics")
            st.write("Two-sample proportion test")
            st.write("R Code:  ```\n prop.test(x=c(x1,x2), n=c(n1,n2), p = NULL, alternative = \"two.sided\", conf.level = 0.95)```")

        elif explanatory_type_cat == "Multiple Levels":
            st.write("### Descriptive Statistics")
            st.write("Frequency Table:  ```\n table(data$row_variable, data$column_variable)```")
            st.write("Row Percents:  ```\n prop.table(table(data$row_variable, data$column_variable), margin = 1)```")
            st.write("Column Percents:  ```\n prop.table(table(data$row_variable, data$column_variable), margin = 2)```")
            st.write("Overall Percents:  ```\n prop.table(table(data$row_variable, data$column_variable))```")
            st.write("Graphs: Clustered bar chart")
            st.write("R Code:  ```\n ggplot(data, aes(x = row_variable, fill = column_variable)) + geom_bar(position = \"dodge\")```")
            st.image('https://github.com/byuistats/221D_CourseMap_App/raw/main/images/dodged_bar_example.png', caption="Clustered Bar Chart Example", width=200)
            st.write("### Inferential Statistics")
            st.write("Chi-square test")
            st.write("R Code:  ```\n chisq.test(table)```")

# Tab 2: Tidyverse Commands
with tab2:
    st.write("### Tidyverse Commands for Data Wrangling")
    st.write("Use the options below to generate R commands for wrangling your data.")
    
    # Subsection: Data Exploration
    st.write("#### Data Exploration")
    data_exploration = st.radio(
        "Choose a data exploration operation:",
        [
            "Look at the dataset",
            "Check the levels of a categorical variable"
        ]
    )

    if data_exploration == "Look at the dataset":
        st.code("""
# Look at the dataset
library(dplyr)
glimpse(data)

# Or use View() in RStudio
View(data)
""", language="r")

    elif data_exploration == "Check the levels of a categorical variable":
        st.code("""
# Check the levels of a categorical variable
unique(data$category_column)
""", language="r")
        
            
    st.write("#### Removing Rows")

    # Categorical Filters
    st.write("#### Categorical Filters")
    categorical_filter = st.radio(
        "Choose a categorical filter operation:",
        [
            "Remove one level of a categorical variable",
            "Keep only one level of a categorical variable",
            "Keep specified levels of a categorical variable",
            "Remove specified levels of a categorical variable"
        ]
    )

    if categorical_filter == "Remove one level of a categorical variable":
        st.code("""
# Remove one level of a categorical variable
library(dplyr)
data %>% filter(category_column != "level_to_remove")
""", language="r")

    elif categorical_filter == "Keep only one level of a categorical variable":
        st.code("""
# Keep only one level of a categorical variable
library(dplyr)
data %>% filter(category_column == "level_to_keep")
""", language="r")

    elif categorical_filter == "Keep specified levels of a categorical variable":
        st.code("""
# Keep specified levels of a categorical variable
library(dplyr)
data %>% filter(category_column %in% c("level1", "level2"))
""", language="r")

    elif categorical_filter == "Remove specified levels of a categorical variable":
        st.code("""
# Remove specified levels of a categorical variable
library(dplyr)
data %>% filter(!category_column %in% c("level1", "level2"))
""", language="r")

    # Quantitative Filters
    st.write("#### Quantitative Filters")
    quantitative_filter = st.radio(
        "Choose a quantitative filter operation:",
        [
            "Remove values greater than a specified value",
            "Remove values less than a specified value",
            "Keep values within a specified range"
        ]
    )

    if quantitative_filter == "Remove values greater than a specified value":
        st.code("""
# Remove values greater than a specified value
library(dplyr)
data %>% filter(numeric_column >= specified_value)
""", language="r")

    elif quantitative_filter == "Remove values less than a specified value":
        st.code("""
# Remove values less than a specified value
library(dplyr)
data %>% filter(numeric_column <= specified_value)
""", language="r")

    elif quantitative_filter == "Keep values within a specified range":
        st.code("""
# Keep values within a specified range
library(dplyr)
data %>% filter(numeric_column >= lower_bound,
                numeric_column <= upper_bound)
""", language="r")

