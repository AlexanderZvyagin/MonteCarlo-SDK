from __future__ import annotations
import mcsdk

import matplotlib.pyplot as plt

def linspace(min:float,max:float,n:int):
    if not (n>=1 and min!=max):
        raise Exception(f'Bad histogram axis: nbins={n} range=[{min},{max}]')
    step = (max-min)/n
    return [min] + [min+step*i for i in range(1,n)] + [max]

def find(results:mcsdk.EvaluationResults,point:int,stateX:int,stateY:int|None=None,histogram_index=0):
    fig, ax = plt.subplots(tight_layout=True)
    ax.set_title(f'Extraction point {point} out of [0,{len(results.time_points)}), time={results.time_points[point]}')
    histograms_filtered = [h for h in results.histograms if h.evaluation_point==point and h.ax.state==stateX]
    if stateY is None:
        histograms_filtered = [h for h in histograms_filtered if not h.ay]
        if len(histograms_filtered)<=histogram_index:
            raise Exception('Cannot find the requested 1D histogram.')
        h = histograms_filtered[histogram_index]
        
        edges = linspace(h.ax.min,h.ax.max,h.ax.nbins)
        n, bins, patches = ax.hist(edges[:-1], edges, weights=h.bins, density=True)
    else:
        # 2D histogram
        histograms_filtered = [h for h in histograms_filtered if h.ay and h.ay.state==stateY]
        if len(histograms_filtered)<=histogram_index:
            raise Exception('Cannot find the requested 2D histogram.')
        h = histograms_filtered[histogram_index]

        x_edges = linspace(h.ax.min,h.ax.max,h.ax.nbins)
        y_edges = linspace(h.ay.min,h.ay.max,h.ay.nbins)

        vx = []
        vy = []
        for y in y_edges[:-1]:
            for x in x_edges[:-1]:
                vx.append(x)
                vy.append(y)

        ax.hist2d(vx,vy,bins=[x_edges,y_edges],weights=h.bins)
        bins = None
        ax.set_ylabel(results.model.titles[stateY])

    plt.xlabel(results.model.titles[stateX])
    return fig,ax,bins

def plot(results:mcsdk.EvaluationResults,point:int,stateX:int,stateY:int|None=None,histogram_index=0):
    find(results,point,stateX,stateY,histogram_index)
    plt.show()

import pandas as pd
def show_histograms2(results):
    def add_axis(d,name,a):
        return {f'{name} title':a.title,f'{name} bins':a.nbins,f'{name} min':a.min,f'{name} max':a.max}
    
    def add_histogram(h):
        d = {'Title':h.Title,'TimeStep':h.TimeStep,'EPoint':h.EvaluationPoint}
        for a,xyz in [(h.AxisX,'X'),(h.AxisY,'Y'),(h.AxisZ,'Z')]:
            if a:
                d = d | add_axis(d,xyz,a)
        return d
    
    return pd.DataFrame([add_histogram(h) for h in results.histograms2])

def plot2(h):
    fig, ax = plt.subplots(tight_layout=True)
    ax.set_title(h.Title)

    if not h.AxisY:
        edges = linspace(h.AxisX.min,h.AxisX.max,h.AxisX.nbins)
        n, bins, patches = ax.hist(edges[:-1], edges, weights=h.Bins, density=True)
    else:
        # 2D histogram
        x_edges = linspace(h.AxisX.min,h.AxisX.max,h.AxisX.nbins)
        y_edges = linspace(h.AxisY.min,h.AxisY.max,h.AxisY.nbins)

        vx = []
        vy = []
        for y in y_edges[:-1]:
            for x in x_edges[:-1]:
                vx.append(x)
                vy.append(y)

        ax.hist2d(vx,vy,bins=[x_edges,y_edges],weights=h.Bins,cmap = plt.colormaps["winter"])
        bins = None
        ax.set_ylabel(h.AxisY.title)

    ax.set_xlabel(h.AxisX.title)
    plt.show()
    # return fig,ax,bins
