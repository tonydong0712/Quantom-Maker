# Quantom Maker — System Architecture

## V1 Architecture Overview

```mermaid
graph TB

    subgraph DATA["Data Layer"]
        A[US Stock Universe]
        A --> B[Market Data Fetcher]
        B --> C[OHLCV / Index / ETF Data]

        C --> D[Feature Calculation]
        D --> D1[MA 5 / 20 / 50 / 200]
        D --> D2[ATR / Volatility]
        D --> D3[Volume / RVOL / Z-Score]
    end

    subgraph ANALYSIS["Analysis Engine"]
        D --> E[Market Analysis]
        D --> F[Theme / Sector Analysis]
        D --> G[Stock Analysis]

        E --> E1[Market Regime]
        E --> E2[Market Breadth]
        E --> E3[Market Liquidity]

        F --> F1[Theme Relative Strength]
        F --> F2[Theme Breadth]
        F --> F3[Capital Flow]
        F --> F4[Leadership]

        G --> G1[Relative Strength]
        G --> G2[Macro Phase]
        G --> G3[Structure Case 1-6]
        G --> G4[Volume / Volatility]

        E1 --> H[Decision Engine]
        E2 --> H
        E3 --> H

        F1 --> H
        F2 --> H
        F3 --> H
        F4 --> H

        G1 --> H
        G2 --> H
        G3 --> H
        G4 --> H
    end

    subgraph RISK["Risk Management"]
        H --> I[Risk Analysis]

        I --> I1[Expected Reward]
        I --> I2[Stop Loss]
        I --> I3[Risk / Reward]
        I --> I4[Portfolio Exposure]
    end

    subgraph POSITION["Position Management"]
        I --> J[Position Engine]

        J --> J1[Position Size]
        J --> J2[Add]
        J --> J3[Hold]
        J --> J4[Reduce]
        J --> J5[Exit]
    end

    subgraph OUTPUT["Output & Validation"]
        J --> K[Signal / Watchlist]
        J --> L[Portfolio Report]

        K --> M[VectorBT Backtest]
        M --> N[Performance Analysis]
        N --> O[Parameter Optimization]
    end
```

## Design Principle

Quantom Maker separates analysis into three major branches:

- **Market Analysis** — determines the overall market environment.
- **Theme / Sector Analysis** — identifies capital concentration and leading themes.
- **Stock Analysis** — evaluates individual stock strength and price structure.

These branches are analyzed independently and merged by the **Decision Engine**.

The system then separates:

**Analysis → Risk → Position Management → Validation**

to keep signal generation independent from portfolio and risk decisions.