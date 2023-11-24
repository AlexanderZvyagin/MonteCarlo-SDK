import mcsdk

import matplotlib.pyplot as plt

def linspace(min:float,max:float,n:int):
    if not (n>=1 and min!=max):
        raise Exception(f'Bad histogram axis: nbins={n} range=[{min},{max}]')
    step = (max-min)/n
    return [min] + [min+step*i for i in range(1,n)] + [max]

def plot(results:mcsdk.EvaluationResults,point:int,stateX:int,stateY:int|None=None,histogram_index=0):
    fig, ax = plt.subplots(tight_layout=True)
    ax.set_title(f'Extraction point {point} out of [0,{len(results.time_points)}), time={results.time_points[point]}')
    histograms_filtered = [h for h in results.histograms if h.evaluation_point==point and h.ax.state==stateX]
    if stateY is None:
        histograms_filtered = [h for h in histograms_filtered if not h.ay]
        if len(histograms_filtered)<=histogram_index:
            raise Exception('Cannot find the requested 1D histogram.')
        h = histograms_filtered[histogram_index]
        
        edges = linspace(h.ax.min,h.ax.max,h.ax.nbins)
        ax.hist(edges[:-1], edges, weights=h.bins)
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

        plt.hist2d(vx,vy,bins=[x_edges,y_edges],weights=h.bins)
        ax.set_ylabel(results.model.titles[stateY])

    plt.xlabel(results.model.titles[stateX])
    plt.show()