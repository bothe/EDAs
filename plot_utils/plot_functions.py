import matplotlib.pyplot as plt
import numpy as np

tags_to_plot = ['xx', 'sd', 'sv', '^q', 'aa', 'ad', 'b', 'ba', 'bh',
                'qh', 'qw', 'qy', 'qy^d', 'nn', 'ny', 'fa', 'fc', 'ft']


def plot_eda_usage(labels, label_values, title, colors_emo,
                   sentiments, sentiments_values, colors_sent,
                   test_show_plot=False, data_name='meld', plot_pie=True):
    print(len(labels), labels)
    data = label_values[0:len(labels) - 1] + [label_values[-1]]
    print(len(data), data)

    # Create a pieplot
    if plot_pie:
        n_emo = plt.pie(data, colors=colors_emo, counterclock=False, startangle=180, radius=1.2)
        for i in range(len(n_emo[0])):
            n_emo[0][i].set_alpha(0.8)

        if data_name == 'meld':
            data_sent = sentiments_values[0:3] + [sentiments_values[-1]]
            plt.pie(data_sent, colors=colors_sent, counterclock=False, startangle=180, radius=0.8)
        # add a circle at the center
        my_circle = plt.Circle((0, 0), 0.5, color='white')
        p = plt.gcf()
        p.gca().add_artist(my_circle)
        # plt.title(title, y=1)
        plt.text(0, -0.15, title, fontdict={'size': 15.0, 'horizontalalignment': 'center'})
    else:
        for i in range(len(labels)):
            plt.bar(labels[i] + labels[i + 1], data[i])  # , colors=colors_emo)

    if test_show_plot:
        plt.show()
        return
    plt.savefig('figures/' + data_name + '/fig_' + title.split('\n')[0], bbox_inches='tight', transparent=True)
    plt.close()


def plot_normal_bars(labels, label_values, title, test_show_plot=False):
    plt.rcParams.update({'font.size': 16})
    plt.bar(labels, label_values)
    plt.title(title.split('\n')[0] + ' - ' + title.split('\n')[1])
    plt.xticks(rotation=15)
    # plt.yaxis.set_major_locator(MaxNLocator(integer=True))
    # plt.ylim(.5, 5.5)
    # plt.xlim(.5, 5.5)
    # plt.xlabel('Emotions')
    # plt.ylabel('Number of Utterances')
    if test_show_plot:
        plt.show()
        return
    plt.savefig('figures/meld/fig_' + title.split('\n')[0])
    plt.close()


def plot_bars_plot(stack_emotions_values, emotions, colors_emo, tags,
                   test_show_plot=False, data='meld', type_of='emotion',
                   save_eps=False, save_svg=False, plot_selected_das=True, plot_sankeys=False):
    from plot_utils.stacked_bars import StackedBarGrapher
    gap, width = 8.0, 10.0
    if 'fo_o_fw_"_by_bc' in tags:
        tags[tags.index('fo_o_fw_"_by_bc')] = 'fo'
    if not plot_selected_das:
        stack_emo_names = {}
        das_stacked = np.array(stack_emotions_values).transpose()
        for i in range(len(emotions)):
            stack_emo_names[emotions[i]] = das_stacked[i]
        totals = das_stacked.sum(axis=0)
        stack_emo_bars = []
        for key in stack_emo_names.keys():
            stack_emo_bars.append([round(i / j * 100, 3) for i, j in zip(stack_emo_names[key], totals)])
        bars = np.array(stack_emo_bars).transpose()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        SBG = StackedBarGrapher()
        SBG.stackedBarPlot(ax, bars, colors_emo, xLabels=tags,
                           gap=gap, widths=[width] * len(tags))
    else:
        stack_emo_lists = []
        das_stacked = np.array(stack_emotions_values).transpose()
        for i in range(len(emotions)):
            stack_emo_lists.append(das_stacked[i])
        totals = das_stacked.sum(axis=0)
        bars = ((stack_emo_lists / totals) * 100).transpose()
        selected_bars_normalized, selected_bars = [], []
        for tag in tags_to_plot:
            selected_bars_normalized.append(bars[tags.index(tag)])
            selected_bars.append(das_stacked.transpose()[tags.index(tag)])

        if plot_sankeys:
            # This will open in browser
            plotting_sankeys(colors_emo, emotions, selected_bars, selected_bars_normalized, data, type_of)

        fig = plt.figure()
        ax = fig.add_subplot(111)
        SBG = StackedBarGrapher()
        SBG.stackedBarPlot(ax, selected_bars_normalized, colors_emo, xLabels=tags_to_plot,
                           gap=gap, widths=[width] * len(tags_to_plot))

    if test_show_plot:
        plt.show()
        return
    dpi = 500
    if save_eps:
        file_name = 'figures/' + data + '_bars_' + type_of + '.eps'
        plt.savefig(file_name, format='eps', bbox_inches='tight', transparent=True, dpi=dpi)
    elif save_svg:
        file_name = 'figures/' + data + '_bars_' + type_of + '.svg'
        plt.savefig(file_name, format='svg', bbox_inches='tight', transparent=True, dpi=dpi)
    else:
        file_name = 'figures/' + data + '_bars_' + type_of + '.png'
        plt.savefig(file_name, bbox_inches='tight', transparent=True, dpi=dpi)
    print('Figure saved as: {}'.format(file_name))
    plt.close()


def plotting_sankeys(colors_emo, emotions, selected_bars, selected_bars_normalized, data, type_of):
    label, color, source, target, value, value_norms, color_links = [], [], [], [], [], [], []
    label = emotions + tags_to_plot
    color = colors_emo[0:len(emotions)] + [colors_emo[-1]] * len(tags_to_plot)
    for i in range(len(tags_to_plot)):
        for j in range(len(emotions)):
            source.append(j)
            target.append(i + len(emotions))
            value.append(selected_bars[i][j])
            value_norms.append(selected_bars_normalized[i][j])
            color_links.append(colors_emo[j])
    plotter_sankey(label, color, source, target, value, color_links, data +
                   " - " + type_of + " - with real number of utterances")
    plotter_sankey(label, color, source, target, value_norms, color_links, data +
                   " - " + type_of + " - with normalized number of utterances")


def plotter_sankey(label, color, source, target, value, color_links, title, create_html=False, host_online=False):
    import plotly.graph_objects as go
    fig = go.Figure(data=[go.Sankey(
        node=dict(pad=3, thickness=15, line=dict(color="green", width=0.), label=label, color=color),
        link=dict(source=source, target=target, value=value, color=color_links))])
    fig.update_layout(title_text=title, font_size=14)
    fig.show()
    if create_html:
        import plotly.io as pio
        pio.write_html(fig, file='figures/' + title + '.html', auto_open=True)
    if host_online:
        import chart_studio.plotly as py
        py.iplot(fig, filename=title)
