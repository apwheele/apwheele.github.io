# Making a Seasonal Chart in Tableau

By [Andrew Wheeler](mailto:apwheele@gmail.com)

This is an example of making a seasonal chart in Tableau. I have prior examples in [Excel](https://apwheele.github.io/Class_CrimeAnalysis/Lab03_TemporalAnalysis.html). And that provides the source for the data I will be using as well (Calls for Service in Burlington, Vermont). I am using the free version, [Tableau Public](https://public.tableau.com/en-us/s/).

# Part 1: Making a basic seasonal chart

So first, open up your Tableau App. Then on the Connect screen select Microsoft Excel. The data we will be using can be downloaded from [here](https://github.com/apwheele/apwheele.github.io/tree/master/Tableau_Examples/SeaonalChart) to your local computer, `OriginalData.xlsx`. 

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/01_TBSeas.PNG?raw=true)

Then it is just a normal dialogue to navigate to the file and select it. Note in a real application, this would be a good use case to connect to a database, so the chart gets auto-updated to the most recent data.

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

So first we will edit the colors for each of the lines. So in the Legend portion in the bottom right of the chart, select the *left click* to select the dropdown, and then pick Edit Colors.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/11_TBSeas.PNG?raw=true)

On Windows, you can hold the `Ctrl` button and left click to select multiple years. Selects the years 12-16, and then select the greyish color.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/12_TBSeas.PNG?raw=true)

If you *double click* on the yellow 2017 swatch, it will bring up a more detailed color picker. Here I just select Red for 2017 (the last year in the data, in real life up-to-date calls for service you would use the current year for your data).

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/13_TBSeas.PNG?raw=true)

Now the lines will be colored so the older years are grey and the current year stands out. But, the 2017 line is drawn in the back. To make it so the Red 2017 line is in the front, we will sort our legend by left clicking on the Legend portion again:

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/14_TBSeas.PNG?raw=true)

Then choose Descending order (default as Ascending) and the most recent year will be at the top.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/15_TBSeas.PNG?raw=true)

Next I like to add a point to the final observation in the data. So in the Marks section on the left hand side of the chart, click Label, then check on Show Mark Labels, select Most Recent, and for the scope select Pane.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/16_TBSeas.PNG?raw=true)

Now if we go back to the big chart, click off the All call-type on the left, and only select Aggravated Assaults. When you do this, you can see we have missing data/discontinuous lines. The next part shows how to fix this.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/17_TBSeas.PNG?raw=true)

For the green `CNT(Call Type)` button, right click and select Edit in Shelf.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/18_TBSeas.PNG?raw=true)

Now for the formula type in `IFNULL(LOOKUP(COUNT([Call Type]),0),0)`. Then hit enter.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/19_TBSeas.PNG?raw=true)

And now you should see some zero observations in the line chart. 

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/20_TBSeas.PNG?raw=true)

Now we are going to save this calculated field, in case we want to use it in other charts. Now drag the green field from the Rows pane over to the Measures pane on the left hand side. This will then let you edit the Measure name. Here I name it `Crime Count (with 0s)`. 

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/21_TBSeas.PNG?raw=true)

Now the final parts we are just going to clean up some of the axis labels and header info. First, for the Y axis, right click and select Edit Axis.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/22_TBSeas.PNG?raw=true)

Then in the Title portion at the bottom, just leave this blank. We will give the chart a title that is informative enough to understand what the Y axis shows. 

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/23_TBSeas.PNG?raw=true)

Next, at the top of the chart, we have `Call Type` in smaller letters. Right click that, and select Hide Field.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/24_TBSeas.PNG?raw=true)

Then finally, we will edit the chart title (in bigger font, above and to the left where the Call Type text was). Right click and select Edit Title.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/25_TBSeas.PNG?raw=true)

Delete the text that default pulls from the sheet name. Go ahead and type in `Crime counts by month per year ()`, and place the cursor inside of the parenthesis. Then select Insert on the top tool bar, and select `Call Type`. 

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/26_TBSeas.PNG?raw=true)

When you update the call type filter, it will propogate to the chart title now, including multiple selections.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/27_TBSeas.PNG?raw=true)

Here is a screenshot showing what the title looks like when selecting both of the assault (aggravated and simple) categories.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/28_TBSeas.PNG?raw=true)

As a final touch, I double click on the sheet name in the lower left, and rename it to `Seasonal Chart`. Then I go to save the workbook, the floppy disc icon on the toolbar towards the top left of the app.

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/29_TBSeas.PNG?raw=true)

Here I just name it `Example Crime Analysis Charts`. 

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/30_TBSeas.PNG?raw=true)

And you can see the interactive version online [here](https://public.tableau.com/views/ExampleCrimeAnalysisCharts/SeasonalChart?:language=en&:display_count=y&publish=yes&:origin=viz_share_link), but here is a screenshot of the app. You can go ahead and click different crime combinations, as well as highlight particular years by selecting them in the legend on the right. 

![](https://github.com/apwheele/apwheele.github.io/blob/master/Tableau_Examples/SeaonalChart/ScreenShots/31_TBSeas.PNG?raw=true)

# Some Notes for Real Life Applications

So that was alot of work! A total of 30 screenshots. But, one of the nice things about Tableau is that you can point the workbook to a live data source, such as an Access database table or view, and then it will just auto-update.

But, if you do that a few caveats. First, you will likely want to filter out the data so it does not show partial months. It will make it seem like crime is going down in the latest month.

Since this is old data, it is a bit hard to show. But you can either use filters in Tableau, or do it in the database via a view, and point Tableau to a view.

A nice part though of doing all the calculations in Tableau is you can add on more filters. So say you wanted both Call Types and Geographic regions, that is as simple as placing a second Filter for area in the Tableau chart. 
