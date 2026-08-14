import vectorbt as vbt

data = vbt.YFData.download(
    "NVDA",
    period="1mo"
)

close = data.get("Close")

print(close.tail())