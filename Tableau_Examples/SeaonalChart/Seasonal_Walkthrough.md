# Making a Seasonal Chart in Tableau

By [Andrew Wheeler](mailto:apwheele@gmail.com)

This is an example of making a seasonal chart in Tableau. I have prior examples in [Excel](https://apwheele.github.io/Class_CrimeAnalysis/Lab03_TemporalAnalysis.html). And that provides the source for the data I will be using as well (Calls for Service in Burlington, Vermont). I am using the free version, [Tableau Public](https://public.tableau.com/en-us/s/).

# Part 1: Making a basic seasonal chart

So first, open up your Tableau App. Then on the Connect screen select Microsoft Excel. The data we will be using can be downloaded from [here](https://github.com/apwheele/apwheele.github.io/tree/master/Tableau_Examples/SeaonalChart) to your local computer, `OriginalData.xlsx`.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/01_TBSeas.PNG?raw=true)

Then it is just a normal dialogue to navigate to the file and select it.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/02_TBSeas.PNG?raw=true)

This file only has one Sheet, `OriginalData`, and that is imported in Tableau. And you can see the table with the column names. If you zoom in you can see that Call Time was not formatted correctly for example, but we do not need to worry about that for now.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/03_TBSeas.PNG?raw=true)

In the bottom tabs select a New Sheet, and then you will see this page below. Drag the `CallDate` field from the left hand side to the Columns area of the chart to begin making our graph. By default Tableau aggregates to the yearly level.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/04_TBSeas.PNG?raw=true)

We can change the temporal aggregation though. Here *right click* on the `YEAR(Call Date)` field, and select Month in the menu.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/05_TBSeas.PNG?raw=true)

Next, drag the Call Type field into the rows. Then *right click* on the Blue Call Type button, and select Measure -> Count.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/06_TBSeas.PNG?raw=true)

At first this will aggregate the monthly counts across each year, but we want to split the lines for each year. So to do that, we again drag the Call Date field from the left, but this time drag it to the Marks area on the left hand side of the graph. This will make the chart have unique lines for each year. 

Then select the little icon to the left of `YEAR(Call Date)` in the marks section, and then select Color. After that, each year will have a unique color.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/07_TBSeas.PNG?raw=true)

Now we are going to make a filter that allows us to generate a Seasonal chart for various aggregations of different call types. So drag the `Call Type` field into the Filter area. Once you do that, you get the below pop-up. Go ahead and select the All button, and click OK.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/08_TBSeas.PNG?raw=true)

Nothing will happen in the chart yet. You need to right click on the Call Type button in the filter area, and then select *Show Filter*.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/09_TBSeas.PNG?raw=true)

Now we have our basic Seasonal chart, with the default set to looking at all calls for service aggregated together. We can see the seasonal effect, with a peak in September, and no uber obvious increases/decreases over the years. 

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/10_TBSeas.PNG?raw=true)

# Part 2: Formatting and Zero Values 

So this is not a bad start, but there are a few aesthetics I like to make the chart look alittle nicer (although some are somewhat arbitrary). Another issue is that if you select certain rare Call Types, you can get a discontinous chart, because it results in some missing data in the Count aggregation (but should just be recoded as 0 values). 

So first we will 

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/11_TBSeas.PNG?raw=true)

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/12_TBSeas.PNG?raw=true)

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/13_TBSeas.PNG?raw=true)

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/14_TBSeas.PNG?raw=true)

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/15_TBSeas.PNG?raw=true)

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/16_TBSeas.PNG?raw=true)

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/17_TBSeas.PNG?raw=true)

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/18_TBSeas.PNG?raw=true)

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/19_TBSeas.PNG?raw=true)

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/20_TBSeas.PNG?raw=true)

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/21_TBSeas.PNG?raw=true)

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/22_TBSeas.PNG?raw=true)

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/23_TBSeas.PNG?raw=true)

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/24_TBSeas.PNG?raw=true)

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/25_TBSeas.PNG?raw=true)

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/26_TBSeas.PNG?raw=true)

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/27_TBSeas.PNG?raw=true)

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/28_TBSeas.PNG?raw=true)

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/29_TBSeas.PNG?raw=true)

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/30_TBSeas.PNG?raw=true)

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/31_TBSeas.PNG?raw=true)

