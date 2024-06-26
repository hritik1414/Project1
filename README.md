The goal of this project is to develop and optimize a trading strategy based on alpha signals using a custom backtesting engine. The process will involve the following tasks:

Static Thresholds Implementation:  
Develop a trading strategy based on static thresholds for building and liquidating a position.
Use the provided alpha values as trading signals to decide whether to buy or sell the asset.
At maximum, hold 1 unit of the stock either in the buy or sell side.
Liquidate any positions completely at the end of the trading cycle.
No transaction costs are considered in this simulation.
Record the trades by adding a column named position to the dataset, indicating the position held at each time point: 1 (long), 0 (neutral), or -1 (short).

Backtesting Engine Development:  
Create a backtesting engine to simulate trading based on the developed strategy.
Generate a Profit and Loss (P&L) statement based on the trading strategy applied to the given dataset.

Threshold Optimization:  
Optimize the build and liquidate thresholds to maximize the P&L for the given data.
Implement a methodology to find the optimal thresholds and validate their effectiveness.
