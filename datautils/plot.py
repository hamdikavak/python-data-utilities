# Hamdi Kavak
# 
# MIT License
# Plotting wrapper functions.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from pandas import Series, DataFrame
from matplotlib.dates import DateFormatter

# global visual settings for my nice plots
g_gridcolor = '#cccccc'
g_legend_fontsize=8
g_legend_edgecolor='#666666'
g_line_width = 0.5

def resetPlotAx(ax):

	ax.set_axisbelow(True)
	ax.yaxis.grid(color=g_gridcolor, linestyle='dashed',linewidth=0.5)
	ax.spines['top'].set_visible(False)
	ax.spines['right'].set_visible(False)
	ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
	
	return ax

def makeBarPlot(df, barprop, filename=None, 
                xlabel=None, ylabel=None, 
                xlim=None, ylim=[0,100], 
                figuresize=(6, 3), barwidth=0.1):
    
    # create plot
    fig, ax = plt.subplots(figsize=figuresize)
    index = np.arange(len(df.index))
    
    ax = resetPlotAx(ax)
    
    if xlim != None:
        ax.set_xlim(xlim)
    
    if ylim != None:    
        ax.set_ylim(ylim)

    loop_index = 0
    
    for df_col in df:
    	plt.bar(index + barwidth * loop_index, df[df_col], barwidth, 
    	        edgecolor='#000000', color=barprop[df_col]['color'], 
    	        label=barprop[df_col]['label'], 
    	        linewidth=g_line_width)
    	loop_index = loop_index + 1
        
    if xlabel != None:
        plt.xlabel(xlabel,fontsize=12)
        
    if ylabel != None:
        plt.ylabel(ylabel,fontsize=12)
            
    plt.xticks(index + barwidth, df.index)
    plt.tick_params(axis='both', which='major', labelsize=8)
    	
    
    leg = plt.legend(fontsize=g_legend_fontsize)
    leg.get_frame().set_edgecolor(g_legend_edgecolor)
	
    plt.tight_layout()
    
    if filename != None:
        plt.savefig(filename, format='eps', dpi=1200)
    else:
    	plt.show()
    
    return;
    
def makeLinePlot(df, lineprop, filename=None, xaxisdatetime=False,
                xlabel=None, ylabel=None, 
                xlim=None, ylim=[0,100], 
                figuresize=(10, 3)):
    
    # create plot
    fig, ax = plt.subplots(figsize=figuresize)
    index = np.arange(len(df.index))
    
    if xlim != None:
        ax.set_xlim(xlim)
    
    if ylim != None:    
        ax.set_ylim(ylim)
        
    ax.set_ylim(ylim)
    ax = resetPlotAx(ax)
    
    loop_index = 0
    
    if xaxisdatetime == True:
        for df_col in df:
    	    plt.plot(df.index, df[df_col], color=lineprop[df_col]['color'], 
    	             label=lineprop[df_col]['label'])
    	    loop_index = loop_index + 1
    else:  
        for df_col in df:
    	    plt.plot(index, df[df_col], color=lineprop[df_col]['color'], 
    	             label=lineprop[df_col]['label'])
    	    loop_index = loop_index + 1
        
    if xlabel != None:
        plt.xlabel(xlabel,fontsize=12)
        
    if ylabel != None:
        plt.ylabel(ylabel,fontsize=12)
       
    if xaxisdatetime == True:
        ax.xaxis_date()

        fig.autofmt_xdate() 
        ax.xaxis.set_major_locator(ticker.MultipleLocator(24))
        monthsFmt = DateFormatter("%b %d, %y")
        ax.xaxis.set_major_formatter(monthsFmt)
    else:  
        plt.xticks(index, df.index)
    
    plt.tick_params(axis='both', which='major', labelsize=8)
    
    
    leg = plt.legend(fontsize=g_legend_fontsize)
    leg.get_frame().set_edgecolor(g_legend_edgecolor)
    plt.tight_layout()
    
    if filename != None:
		plt.savefig(filename, format='eps', dpi=1200)
    else:
		plt.show()
    
    return;