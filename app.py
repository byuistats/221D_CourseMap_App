import streamlit as st

# Main app content
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
            with st.expander("Descriptive Statistics"):
                st.write("Mean, Median, Mode, Standard Deviation, Percentiles")
                st.write("Graph: Histogram")
                st.image("https://github.com/byuistats/Math221D_Cannon/raw/master/Images/histogramggplotgallery1.png", caption="Histogram Example", width=200)
                st.code("""
                        ggplot(data, aes(x = value)) + 
                            geom_histogram() +
                            labs(
                                x = "Temperature",
                                y = "Number of Days",
                                title = "La Guardia Airport Daily Mean Temperature"
                                ) +
                                theme_bw()""", language="r")

            with st.expander("Inferential Statistics"):
                st.write("One-sample t-test")
                st.code("""
                        t.test(data$response_variable, mu = mu0, alternative = \"two.sided\")""", language="r")
                st.image('https://github.com/byuistats/221D_CourseMap_App/raw/main/images/one_sample_t_test_statistic.png', caption="One-Sample t-test", width=100)

        elif explanatory_type_quant == "Categorical":
            with st.expander("Descriptive Statistics"):
                st.write("Grouped Means, Medians, Standard Deviations, Percentiles")
                st.write("Graph: Side-by-side Boxplot")
                st.code("""
                        ggplot(data, aes(x = group, y = value)) + 
                            geom_boxplot()""", language="r")
                st.image("https://github.com/byuistats/Math221D_Cannon/raw/master/Images/boxplotggplotgallery1.png", caption="Boxplot Example", width=300)

            with st.expander("Inferential Statistics"):
                how_many_groups = st.radio("How Many Levels?", ("2 Dependent Samples", "2 Independent Samples", "3+ Levels"))

                if how_many_groups == "2 Dependent Samples":
                    st.write("Paired t-test")
                    st.code("""
                            t.test(data$value1-data$value2, alternative = \"two.sided\")""", language="r")
                    st.write("Matched Pairs t-test")
                    st.image('https://github.com/byuistats/221D_CourseMap_App/raw/main/images/matched_pairs_test_stat.png', caption="Matched Pairs Test Statistic", width=100)

                elif how_many_groups == "2 Independent Samples":
                    st.write("Independent 2-sample t-test")
                    st.write("2-sample t-test")
                    st.code("""
                            t.test(value ~ group, data = data)""", language="r")
                    st.image('https://github.com/byuistats/221D_CourseMap_App/raw/main/images/two_sample_t_test_statistic.png', caption="2-sample t-test statistic", width=100)

                elif how_many_groups == "3+ Levels":
                    st.write("ANOVA")
                    st.code("""
                            aov_output <- aov(value ~ group, data = data)
                            summary(aov_output)""", language="r")
                    st.write("F-Statistic")
                    st.image('https://github.com/byuistats/221D_CourseMap_App/raw/main/images/F_statistic.png.png', caption="F-Statistic", width=210)

        elif explanatory_type_quant == "Quantitative":
            with st.expander("Descriptive Statistics"):
                st.write("Graph: Scatter plot")
                st.code("""
                        ggplot(data, aes(x = x, y = y)) + 
                            geom_point() + 
                            geom_smooth(method = 'lm')""", language="r")
                st.image("https://github.com/byuistats/Math221D_Cannon/raw/master/Images/Regression_Line_Example.png", caption="Scatterplot Example", width=200)
                st.write("Correlation Coefficient (r)")
                st.code("""cor(data$x, data$y)""", language="r")

            with st.expander("Inferential Statistics"):
                st.write("Simple Linear Regression")
                st.code("""
                        lm_output <- lm(data$y ~ data$x)
                        summary(lm_output)""", language="r")

    elif response_type == "Categorical":
        explanatory_type_cat = st.radio("What is your Explanatory Variable?", ("None", "2 Levels", "Multiple Levels"))

        if explanatory_type_cat == "None":
            with st.expander("Descriptive Statistics"):
                st.write("Frequency Table")
                st.write("Proportion (p)")
                st.write("Graphs: Bar chart")
            with st.expander("Inferential Statistics"):
                st.write("One-sample proportion test")
                st.code("""
                        # One-sample proportion test
                        # x = number of successes in the sample
                        # n = sample size
                        prop.test(x, n, p = p0, alternative = \"two.sided\", conf.level = 0.95)
                        
                        # Confidence Interval
                        prop.test(x,n)$conf.int
                        """, language="r")

        elif explanatory_type_cat == "2 Levels":
            with st.expander("Descriptive Statistics"):
                st.write("Frequency Table")
                st.write("Proportions (p1, p2)")
                st.write("Graphs: Clustered bar chart")
            with st.expander("Inferential Statistics"):
                st.write("Two-sample proportion test")
                st.code("""
                        # Two-sample proportion test
                        # x1 = number of successes in group 1
                        prop.test(x=c(x1,x2), n=c(n1,n2), alternative = \"two.sided\", conf.level = 0.95)
                        
                        # Confidence Interval for difference p1-p2
                        prop.test(x=c(x1,x2), n=c(n1,n2), conf.level = 0.95)$conf.int
                        """, language="r")

        elif explanatory_type_cat == "Multiple Levels":
            with st.expander("Descriptive Statistics"):
                st.write("Frequency Table:  ```\n table(data$row_variable, data$column_variable)```")
                st.write("Row Percents:  ```\n prop.table(table(data$row_variable, data$column_variable), margin = 1)```")
                st.write("Column Percents:  ```\n prop.table(table(data$row_variable, data$column_variable), margin = 2)```")
                st.write("Overall Percents:  ```\n prop.table(table(data$row_variable, data$column_variable))```")
                st.write("Graphs: Clustered bar chart")
                st.code("""
                        ggplot(data, aes(x = row_variable, fill = column_variable)) + 
                            geom_bar(position = \"dodge\")""", language="r")
                st.image('https://github.com/byuistats/221D_CourseMap_App/raw/main/images/dodged_bar_example.png', caption="Clustered Bar Chart Example", width=200)
            with st.expander("Inferential Statistics"):
                st.write("Chi-square test")
                st.image('https://github.com/byuistats/221D_CourseMap_App/raw/main/images/chi2_test_statistic.png', caption="Chi-Square Test Statistic", width=200)
                st.image('https://github.com/byuistats/221D_CourseMap_App/raw/main/images/chi2_expected_counts.png', caption="Expected Counts", width=400)
                st.code("""
                        tbl <- table(data$row_variable, data$column_variable)
                        chisq.test(tbl)""", language="r")
                st.code("""
                        # Check test requirements counts: 
                        chisq.test(tbl)$expected >= 5
                        """, language="r")

# Tab 2: Tidyverse Commands
with tab2:
    st.write("## Tidyverse Commands for Data Wrangling")
    st.write("Use the options below to generate R commands for wrangling your data.")
    
    # Subsection: Data Exploration
    st.write("### Data Exploration")
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
        
            
    st.write("### Removing Rows")

    # Categorical Filters
    st.write("#### Categorical Filters")
    categorical_filter = st.radio(
        "Choose a categorical filter operation:",
        [
            "Remove only one level of a categorical variable",
            "Keep only one level of a categorical variable",
            "Keep specified levels of a categorical variable",
            "Remove specified levels of a categorical variable"
        ]
    )

    if categorical_filter == "Remove only one level of a categorical variable":
        st.code("""
# Remove one level of a categorical variable
data %>% filter(category_column != "level_to_remove")
""", language="r")

    elif categorical_filter == "Keep only one level of a categorical variable":
        st.code("""
# Keep only one level of a categorical variable
data %>% filter(category_column == "level_to_keep")
""", language="r")

    elif categorical_filter == "Keep specified levels of a categorical variable":
        st.code("""
# Keep specified levels of a categorical variable
data %>% filter(category_column %in% c("level1", "level2"))
""", language="r")

    elif categorical_filter == "Remove specified levels of a categorical variable":
        st.code("""
# Remove specified levels of a categorical variable
data %>% filter(!category_column %in% c("level1", "level2"))
""", language="r")

    # Quantitative Filters
    st.write("#### Quantitative Filters")
    quantitative_filter = st.radio(
        "Choose a quantitative filter operation:",
        [
            "Keep values greater than a specified value",
            "Keep values less than a specified value",
            "Keep values within a specified range"
        ]
    )

    if quantitative_filter == "Keep values greater than a specified value":
        st.code("""
# Keep values greater than a specified value
data %>% filter(numeric_column >= specified_value)
""", language="r")

    elif quantitative_filter == "Keep values less than a specified value":
        st.code("""
# Keep values less than a specified value
data %>% filter(numeric_column <= specified_value)
""", language="r")

    elif quantitative_filter == "Keep values within a specified range":
        st.code("""
# Keep values within a specified range
data %>% filter(numeric_column >= lower_bound,
                numeric_column <= upper_bound)
""", language="r")

