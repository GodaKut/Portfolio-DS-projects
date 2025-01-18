# South Korea 2020 COVID-19 crisis analysis

The goal of the notebook is to perform EDA on the Kaggle datasets of COVID-19 data from 2020-01 to 2020-07, draw critical insights ans present how the pandemic fighting plan could have been improved. 

### Objectives
* Practice identifying opportunities for data analysis.
* Practice performing EDA.
* Practice working with data from Kaggle.
* Practice visualizing data with Matplotlib & Seaborn.
* Practice reading data, performing queries, and filtering data using Pandas.

## Conclusions

The First wave lasted for 2 whole months however the peak of daily infections (813) was reached in the first 10 days meaning that there should be no hesitation when implementing strict policies. In the next 14 days daily confirmed cases have decreased drastically and nearly even out with the numbers of people recovered from COVID-19. It took nearly a month for the recovery number and number of deceased people to peak. </br>
When looking at the number of tests per person confirmed with COVID-19 it is evident that the number of tests conducted has not managed to keep up with the number of confirmed cases. After the daily confirmed cases have reached its peak the conducted test ratio has been increasing steadily once again. There is an opportunity to improve when talking about the number of tests conducted during the times when confirmed cases are sharply increasing.</br>
The 4 provinces Daegu, Gyeongsangbuk-doo, Seoul, and Gyeonggi-do showed the highest numbers of infected people, Daegu being in the strong lead. It should be investigated further why Seoul despite having the same number people of confirmed with COVID-19 as Gyeonggi-do managed to have a lower mortality rate. The Shincheonji Church infection case has brought a huge amount of infected people to Daegu province. Such gatherings should be closely monitored or restricted in the future. Cities having high academy ratios like Daegu should take extra measures to prevent people in their 20s from being infected and spreading the virus to the elderly. </br> 
It remains unclear why the male mortality rate is higher than females despite more females being confirmed with COVID-19. This is especially evident for people in their 60s and 70s. An investigation should be done if there is any gender discrimination when it comes to patient treatment or if there are additional factors causing this.</br>
As expected number of deceased people is higher for people in their 50s and older. Having this in mind the fact that people in their 50s were the second most infected age group is troubling and should be brought to light for the public.</br>
When it comes to the leading infections contact with the patient, cases overseas inflow and Shincheonji Church case stand out. For the age groups that are most vulnerable to being deceased (in the 50s and older) contact with patients seems to be the leading cause of infection. People in their 90s tend to have the highest average number of contacts. </br>
Taking all that into consideration, implementing a strong Social Distancing Campaign on the day the Infectious Disease Alert Level was elevated to 4 (Red) could have aided in decreasing the number of people confirmed with COVID-19. Since overseas inflow brought more infections than contact with the patient, all Special Immigration Procedures should be implemented early on as well.  Mandatory 14-day Self-Quarantine seems to have aided in preventing the confirmed numbers from peaking again though its implementation was quite late.

## Getting Started

### Dependencies


* python
* pandas
* numpy
* matplotlib 
* seaborn 
* scipy 

For more information see REQUIREMENTS.txt

### Datasets

Kaggel:
https://www.kaggle.com/datasets/kimjihoo/coronavirusdataset/?select=TimeProvince.csv



## Authors

Goda Kutkeviciute 

## Version History

* 0.2
    * Fixed spelling issues
    * Tuckey method for finding outliers was moved to a separate file
    * Created a function to put annotations to shrink the size of cells
    * Added barplot for the treated and isolated patients per age group by gender
    * Added barplot for the number of contacts per age group
    * Changed the correlations to be calculated on confirmed increases instead of accumulative number of confirmed infections
    * Added a heatmap of correlations
    * Rewritten concussions to be more readable
* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.txt file for details

