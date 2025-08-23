# LandInsights Data Dictionary

## Inventory Metrics

| Data Label | Description |
|------------|-------------|
| **Active** | Quantity of land for sale |
| **Pending** | Quantity of land under contract |
| **Sold: 1mo** | Quantity of land sold in last 1 month |
| **Sold: 3mo** | Quantity of land sold in last 3 months |
| **Sold: 6mo** | Quantity of land sold in last 6 months |
| **Sold: 1yr** | Quantity of land sold in last 12 months |

## Sell-Through Rate (STR)

| Data Label | Description |
|------------|-------------|
| **Pending STR** | Pending / Active |
| **1mo STR** | Sold: 1mo / Active |
| **3mo STR** | Sold: 3mo / Active |
| **6mo STR** | Sold: 6mo / Active |
| **1yr STR** | Sold: 12mo / Active |

## Days on Market (DOM)

| Data Label | Description |
|------------|-------------|
| **Avg DOM 1mo** | Average Number of days for a listing to sell in last 1 month |
| **Avg DOM 3mo** | Average Number of days for a listing to sell in last 3 months |
| **Avg DOM 6mo** | Average Number of days for a listing to sell in last 6 months |
| **Avg DOM 1yr** | Average Number of days for a listing to sell in last 12 months |

## Median Prices

| Data Label | Description |
|------------|-------------|
| **Median Active Price** | Median price of land currently for sale |
| **Median Pending Price** | Median price of land currently under contract |
| **Median Price 1mo** | Median sales price of land sold in the last 1 month |
| **Median Price 3mo** | Median sales price of land sold in the last 3 months |
| **Median Price 6mo** | Median sales price of land sold in the last 6 months |
| **Median Price 1yr** | Median sales price of land sold in the last 12 months |

## Median Acreage

| Data Label | Description |
|------------|-------------|
| **Median Active Acreage** | Median acreage of land currently for sale |
| **Median Pending Acreage** | Median acreage of land currently under contract |
| **Median Sold Acreage** | Median acreage of land sold in the last 12 months |

## Median Price Per Acre (PPA)

| Data Label | Description |
|------------|-------------|
| **Median Active PPA** | Median price per acre of land currently for sale |
| **Median Pending PPA** | Median price per acre of land currently under contract |
| **Median Sold PPA** | Median price per acre of land sold in the last 12 months |

## Price Per Acre Range - Active Listings

| Data Label | Description |
|------------|-------------|
| **Active PPA Min** | Lowest price per acre listing of land currently listed for sale |
| **Active PPA Max** | Highest price per acre listing of land currently listed for sale |
| **Pending PPA Min** | Lowest price per acre listing of land currently under contract |
| **Pending PPA Max** | Highest price per acre listing of land currently under contract |

## Price Per Acre Range - Sold Properties

| Data Label | Description |
|------------|-------------|
| **PPA Range 1mo Min** | Lowest price per acre listing sold in the last 1 month |
| **PPA Range 1mo Max** | Highest price per acre listing sold in the last 1 month |
| **PPA Range 3mo Min** | Lowest price per acre listing sold in the last 3 months |
| **PPA Range 3mo Max** | Highest price per acre listing sold in the last 3 months |
| **PPA Range 6mo Min** | Lowest price per acre listing sold in the last 6 months |
| **PPA Range 6mo Max** | Highest price per acre listing sold in the last 6 months |
| **PPA Range 1yr Min** | Lowest price per acre listing sold in the last 12 months |
| **PPA Range 1yr Max** | Highest price per acre listing sold in the last 12 months |

## Gini Index

| Data Label | Description |
|------------|-------------|
| **Gini Index** | The Gini index measures the extent to which the distribution of sales PPA deviates from a perfectly equal distribution. A Gini index of 0 represents perfect equality, while an index of 100 implies perfect inequality. Simply put, Gini captures how well the PPA of the dataset "hugs" the mean value in a distribution. When analyzing gini in a market, the lower the gini, the more homogeneous the pricing is in that market. Gini is only effective when looking at smaller acreage ranges like 1-2 acres or 10-20 acres since it is using only the sales prices in that range. |
| **Gini 1mo** | Gini index of sold PPA in the last 1 month |
| **Gini 3mo** | Gini index of sold PPA in the last 3 months |
| **Gini 6mo** | Gini index of sold PPA in the last 6 months |
| **Gini 1yr** | Gini index of sold PPA in the last 12 months |