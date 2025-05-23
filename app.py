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
                        # Base R Histogram
                        library(mosaic)
                        histogram(data$response_variable, 
                                  xlab = "Temperature",
                                  ylab = "Number of Days",
                                  main = "La Guardia Airport Daily Mean Temperature")
                        
                        # ggplot2 Histogram
                        library(ggplot2)
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
                st.code("""
                        library(mosaic)
                        favstats(data$value ~ data$group)
                        """, language="r")
                st.write("Graph: Side-by-side Boxplot")
                st.code("""
                        # Base R Boxplot: Categorical Explanatory Variable
                        boxplot(data$response ~ data$explanatory,
                                xlab = "Group",
                                ylab = "Value",
                                main = "Boxplot of Value by Group")
                                
                        # ggplot2 Boxplot
                        library(tidyverse)
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
                        # Base R Scatterplot: Quantitative Explanatory Variable
                        plot(data$response ~ data$explanatory,
                             xlab = "Explanatory Variable",
                             ylab = "Response Variable",
                             main = "Scatterplot of Response vs. Explanatory")
                        
                        # ggplot2 Scatterplot
                        library(tidyverse)
                        ggplot(data, aes(x = x, y = y)) + 
                            geom_point() + 
                            geom_smooth(method = 'lm')""", language="r")
                st.image("https://github.com/byuistats/Math221D_Cannon/raw/master/Images/Regression_Line_Example.png", caption="Scatterplot Example", width=200)
                st.write("Correlation Coefficient (r)")
                st.code("""
                        cor(data$response ~ data$explanatory)
                        """, language="r")

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
                st.code("""
                        # Frequency Table
                        table(data$Most_Used_Social_Media)
                        """, language="r")
                st.write("Proportion (p)")
                st.code("""
                        # Proportion (p)
                        prop.table(table(data$Most_Used_Social_Media))
                        """, language="r")
                st.write("Graphs: Bar chart")
                st.code("""
                        # Base R Barplot
                        prop_table_major <- sort(prop.table(table(creativity$Major_Category)), decreasing = TRUE)

                        barplot(prop_table_major, las=2)
                        
                        # ggplot2 Barplot
                        library(tidyverse)
                        
                        ggplot(data, aes(x = Most_Used_Social_Media)) +
                            geom_bar() +
                            theme_bw() +
                            labs(
                                y = "",
                                x = "Count",
                                title = "Most Used Social Media"
                            )""", language="r")
                st.image('https://github.com/byuistats/221D_CourseMap_App/raw/main/images/Social_Media_Graph1.png', caption="Bar Chart Example", width=400)
                st.code("""
                        ggplot(data, aes(y = fct_infreq(Most_Used_Social_Media))) +
                            geom_bar() +
                            theme_bw() +
                            labs(
                                y = "",
                                x = "Count",
                                title = "Most Used Social Media"
                            )""", language="r")
                st.image('https://github.com/byuistats/221D_CourseMap_App/raw/main/images/Social_Media_Graph2.png', caption="Bar Chart Example", width=400)
                st.code("""
                        ggplot(data, aes(y = fct_rev(fct_infreq(Most_Used_Social_Media)))) +
                            geom_bar() +
                            theme_bw() +
                            labs(
                                y = "",
                                x = "Count",
                                title = "Most Used Social Media"
                            )""", language="r")
                st.image('https://github.com/byuistats/221D_CourseMap_App/raw/main/images/Social_Media_Graph3.png', caption="Bar Chart Example", width=400)


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
                st.code("""
                        # Frequency Table
                        table(data$Most_Used_Social_Media, data$Biosex)
                        """, language="r")
                st.write("Proportions (p1, p2)")
                st.code("""
                        # x1 = number of successes in group 1
                        # x2 = number of successes in group 2
                        # n1 = sample size in group 1
                        # n2 = sample size in group 2
                        phat1 <- x1/n1
                        phat2 <- x2/n2
                        """, language="r")
                st.write("Graphs: Clustered bar chart")
                st.code("""
                        # base R
                        barplot(table(data$Most_Used_Social_Media, data$Biosex),   
                                beside = TRUE,
                                xlab = "Most Used Social Media",
                                ylab = "Count",
                                main = "Social Media Use by Biosex")
                                
                        # ggplot2
                        library(tidyverse)
                        
                        ggplot(two_cat_dat, aes(y = Most_Used_Social_Media, fill=Biosex)) +
                            geom_bar(position=\"dodge\") +
                            theme_bw() +
                            labs(
                                x = "Most Used Social Media",
                                y = "Count",
                            title = "Social Media Use by Biosex"
  )""", language="r")
                st.image('https://github.com/byuistats/221D_CourseMap_App/raw/main/images/Two_Sample_Categorical_Chart.png', caption="Clustered Bar Chart Example", width=400)
                st.code("""
                        ggplot(two_cat_dat, aes(fill = Most_Used_Social_Media, x=Biosex)) +
                            geom_bar(position=\"dodge\") +
                            theme_bw() +
                            labs(
                                x = "Most Used Social Media",
                                y = "Count",
                            title = "Social Media Use by Biosex"
  )""", language="r")
                st.image('https://github.com/byuistats/221D_CourseMap_App/raw/main/images/Two_Sample_Categorical_Chart2.png', caption="Clustered Bar Chart Example", width=400)


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
                st.write("Frequency Table:")
                st.code("""
                        table(data$row_variable, data$column_variable)
                        """, language="r")
                st.write("Row Percents:")
                st.code("""
                        prop.table(table(data$row_variable, data$column_variable), margin = 1)
                        """, language="r")
                st.write("Column Percents:")
                st.code("""
                        prop.table(table(data$row_variable, data$column_variable), margin = 2)
                        """, language="r")
                st.write("Overall Percents:")
                st.code("""
                        prop.table(table(data$row_variable, data$column_variable))
                        """, language="r")
                st.write("Graphs: Clustered bar chart")
                st.code("""
                        
                        # base R
                        barplot(table(data$row_variable, data$column_variable),
                                beside = TRUE,
                                xlab = "Row Variable",
                                ylab = "Count",
                                main = "Clustered Bar Chart")
                                
                        # ggplot2
                        library(tidyverse)
                        
                        ggplot(data, aes(x = row_variable, fill = column_variable)) + 
                            geom_bar(position = \"dodge\")""", language="r")
                st.image('https://github.com/byuistats/221D_CourseMap_App/raw/main/images/dodged_bar_example.png', caption="Clustered Bar Chart Example", width=400)
            with st.expander("Inferential Statistics"):
                st.write("Chi-square test")
                st.image('https://github.com/byuistats/221D_CourseMap_App/raw/main/images/chi2_test_statistic.png', caption="Chi-Square Test Statistic", width=400)
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

