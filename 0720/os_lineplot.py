import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib qt
plt.figure(figsize=(12.8, 4.8))
# %% load data
data1 = pd.DataFrame(
    [
        ["2018", 0.0126, 'Android'],
        ["2018", 0.0491, 'IOS'],
        ["2019", 0.0241, 'Android'],
        ["2019", 0.0345, 'IOS'],
        ["2020", 0.0123, 'Android'],
        ["2020", 0.0234, 'IOS'],
    ], columns=['Year', 'Rate', 'OS']
)

data2 = pd.DataFrame(
    [
        ["2018", 0.2824, 'Android'],
        ["2018", 0.3586, 'IOS'],
        ["2019", 0.3732, 'Android'],
        ["2019", 0.3456, 'IOS'],
        ["2020", 0.2143, 'Android'],
        ["2020", 0.3214, 'IOS'],
    ], columns=['Year', 'Rate', 'OS']
)

# %% plot
ax1 = plt.subplot(121)
g1 = sns.lineplot(x='Year', y='Rate', hue='OS', data=data1, style="OS", markers=True, dashes=False)
plt.ylim(0)
plt.legend(["Android", "IOS"], loc="upper right", fontsize=8)
ax2 = plt.subplot(122)
g2 = sns.lineplot(x='Year', y='Rate', hue='OS', data=data2, style="OS", markers=True, dashes=False)
plt.legend(["Android", "IOS"], loc="upper right", fontsize=8)
plt.ylim(0)
plt.show()
