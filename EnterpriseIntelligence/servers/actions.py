from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ActionServer")

@mcp.tool()
def calculate_bonus(salary: float, performance_score: float) -> float:
    """
    Calculates employee bonus based on salary and performance score (0-5).
    Returns the bonus amount.
    """
    if performance_score > 4.5:
        return salary * 0.20
    elif performance_score > 3.0:
        return salary * 0.10
    else:
        return 0.0

@mcp.tool()
def get_stock_price(ticker: str) -> str:
    """Fake stock price fetcher for demo purposes."""
    return f"The current price of {ticker} is $150.00"

if __name__ == "__main__":
    mcp.run(transport="stdio")