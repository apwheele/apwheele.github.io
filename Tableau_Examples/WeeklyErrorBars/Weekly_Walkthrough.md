# Making a Weekly Crime Count and Error Bar Chart in Tableau

By [Andrew Wheeler](mailto:apwheele@gmail.com)

So this is the second Tableau walkthrough I have created. It is an attempt to replicate the materials in the weekly chart section for my [crime analysis tutorials](https://apwheele.github.io/Class_CrimeAnalysis/Lab03_TemporalAnalysis.html) in Excel. 

We will be using the prior example, to start with, see [*Making a Seasonal Chart in Tableau*](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/Seasonal_Walkthrough.md) for part 1. 

At a high level, the idea is to make a chart that shows both current trends (by showing a moving average of the prior 8 weeks), as well as show error bars around that prior moving average. This then lets you see both long term trends, as well as local outliers (if above the error bars, it signifies that recent week is anomalous compared to the recent 8 week trend). 

## Part 1 Making New Fields

First, open up the prior tbx example you created in the Seasonal chart walkthrough. (If doing out of order, you will need to sync up your own data, and make a calculated field for the crime counts per unit time). We are going to create a new worksheet, but first lets right click on the Seasonal Chart sheet and select copy.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/WeeklyErrorBars/ScreenShots/01_ErrorBar.PNG?raw=true)

Then right click on the little icon to the right and select Paste.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/WeeklyErrorBars/ScreenShots/02_ErrorBar.PNG?raw=true)

Then go ahead and rename this worksheet Weekly Crimes, and in the Marks portion right click and remove the Yearly variable.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/WeeklyErrorBars/ScreenShots/03_ErrorBar.PNG?raw=true)

Next, migrate up to the Columns portion of the main worksheet. Right click on the Month pill in the Columns section. Then select Week Number and Discrete. To create error bars later on we need the data to be discrete instead of continuous.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/WeeklyErrorBars/ScreenShots/04_ErrorBar.PNG?raw=true)

Next we will be making our moving average and low/high error bar fields. In the Measure Names section on the lower left, right click in any whitespace area, and select *Create Calculated Field...*.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/WeeklyErrorBars/ScreenShots/05_ErrorBar.PNG?raw=true)

Name the field `Prior Average 8`, and for the function type in `WINDOW_AVG([Crime Count (with 0s)],-9,-1)`. Note that the field `[Crime Count (with 0s)]` is one we created from the prior Seasonal Chart tutorial. Once done, go ahead and click OK. -9 to -1 makes it a moving average of the prior 8 weeks in this example.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/WeeklyErrorBars/ScreenShots/06_ErrorBar.PNG?raw=true)

You will see the new field you just created in that same area in the Measure Names section. Go ahead and drag that new calculated field onto the location of the Y axis on the current chart. This superimposes the two lines, the observed count and the prior average, on the same chart.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/WeeklyErrorBars/ScreenShots/07_ErrorBar.PNG?raw=true)

Next we are making the upper/lower error bars via two additional fields. These are calculated via square root of the Poisson distribution, which is a variance stabilizing transformation, see my [article on the topic for reference](https://journals.sagepub.com/doi/10.1177/1461355716642781). For the lower CI, the formula is `(3/2 + SQRT([Prior Average 8]))^2`.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/WeeklyErrorBars/ScreenShots/08_ErrorBar.PNG?raw=true)

And for the lower CI, the formula is `MAX((-3/2 + SQRT([Prior Average 8]))^2,0)`.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/WeeklyErrorBars/ScreenShots/09_ErrorBar.PNG?raw=true)

## Part 2 Making Error Bars

At this point you should see the four lines superimposed. To make our error bars, we are going to remove the crime counts measure though (and add it back in later). This is because Tableau limits the error bar calculates to particular summary statistics, like the min/max of all measures. So go ahead and right click on the Crime Count pill, and select Remove.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/WeeklyErrorBars/ScreenShots/10_ErrorBar.PNG?raw=true)

In the Y axis area of the chart, right click and select *Add Reference Line*:

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/WeeklyErrorBars/ScreenShots/11_ErrorBar.PNG?raw=true)

In the pop up, select the Band option at the top, then make sure the Per Cell option is selected. I believe the from/to fields are by default here minimum and maximum (which is what we want), but we can turn off the labels by selecting None for the label. Then you should see the grey error band in the background, in addition to the prior average/low/high bars.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/WeeklyErrorBars/ScreenShots/12_ErrorBar.PNG?raw=true)

Next, in the Marks area on the left, change the lines to Gantt bars, this is because the lines don't match up nicely with the error bars. (I would prefer the center moving average to be a line instead of the steps, but I was not able to figure out how in this set up.)

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/WeeklyErrorBars/ScreenShots/13_ErrorBar.PNG?raw=true)

Next, on the right hand side I double clicked on the color swatches. I then change the moving average to black, and the lower/upper lines to the same error bar color, here it is `#d7d7d7`. This is so it is just a grey blob as the error area, not outlined by different colors.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/WeeklyErrorBars/ScreenShots/14_ErrorBar.PNG?raw=true)

## Part 3 Dual Axis and Some Extras

Now for the third part, we need to add back in our observed line. Remember the whole point is to see if the current week is above the moving average and its error bar. This is a signal that the process is an outlier. To do this drag the `Crime Count with 0s` variable onto the Rows dimension. This creates a second panel below the error bars with the crime counts.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/WeeklyErrorBars/ScreenShots/15_ErrorBar.PNG?raw=true)

In the marks area on the left, change the type to line. Also then right click anywhere in the Y axis area of the Crime counts panel, and then select Dual Axis.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/WeeklyErrorBars/ScreenShots/16_ErrorBar.PNG?raw=true)

Now there will only be one panel with all of the elements superimposed. But the two axes will not be lined up. If you right click on the Y axes on the right, select Synchronize Axis to make sure the lines and error bars are superimposed correctly.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/WeeklyErrorBars/ScreenShots/17_ErrorBar.PNG?raw=true)

And now you have the main components of your weekly error bar chart. But to clean up a few final things. First, I changed my line color of the observed series to orange (to make it stand out slightly more). 

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/WeeklyErrorBars/ScreenShots/18_ErrorBar.PNG?raw=true)

Then I make sure to turn off labels (these were turned on for the final observation for the seasonal chart we copied at first). 

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/WeeklyErrorBars/ScreenShots/19_ErrorBar.PNG?raw=true)

And there you have it, you can use the preview button to see how your chart looks. Here is a selection of Burglaries (make sure to scroll the X axis left/right to see the changes over time). So you can see from this one week was anomalous, going from 4 to 20. But going from 4 to 10 is not anomalous according to the Poisson distribution.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/WeeklyErrorBars/ScreenShots/20_ErrorBar.PNG?raw=true)






