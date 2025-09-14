"""
DuckChain MCP Server

A comprehensive MCP server that provides access to blockchain data
via the BlockScout API v2 specification.
"""

import httpx
from typing import Optional, Dict, Any, List
from mcp.server.fastmcp import Context, FastMCP
from pydantic import BaseModel, Field
from smithery.decorators import smithery


class ConfigSchema(BaseModel):
    """Configuration schema for DuckChain MCP server."""
    # server_url: str = Field(
    #     default="scan.duckchain.io",
    #     description="BlockScout server URL (e.g., 'scan.duckchain.io')"
    # )
    timeout: int = Field(
        default=30,
        description="Request timeout in seconds"
    )


class DuckChainAPI:
    """BlockScout API client for DuckChain."""
    
    def __init__(self, timeout: int = 30):
        self.base_url = f"https://scan.duckchain.io/api/v2"
        self.timeout = timeout
        self.client = httpx.AsyncClient(timeout=timeout)
    
    async def _make_request(self, endpoint: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """Make a request to the BlockScout API."""
        url = f"{self.base_url}{endpoint}"
        
        response = await self.client.get(url, params=params or {})
        response.raise_for_status()
        return response.json()
    
    async def search(self, q: str) -> Dict[str, Any]:
        """Search for addresses, tokens, blocks, or transactions."""
        return await self._make_request("/search", {"q": q})
    
    async def search_redirect(self, q: str) -> Dict[str, Any]:
        """Check if search query should redirect to a specific page."""
        return await self._make_request("/search/check-redirect", {"q": q})
    
    async def get_transactions(
        self,
        filter_type: Optional[str] = None,
        type: Optional[str] = None,
        method: Optional[str] = None
    ) -> Dict[str, Any]:
        """Get transactions with optional filtering."""
        params = {}
        if filter_type:
            params["filter"] = filter_type
        if type:
            params["type"] = type
        if method:
            params["method"] = method
        return await self._make_request("/transactions", params)
    
    async def get_blocks(self, type: Optional[str] = None) -> Dict[str, Any]:
        """Get blocks with optional type filtering."""
        params = {}
        if type:
            params["type"] = type
        return await self._make_request("/blocks", params)
    
    async def get_token_transfers(self) -> Dict[str, Any]:
        """Get token transfers."""
        return await self._make_request("/token-transfers")
    
    async def get_internal_transactions(self) -> Dict[str, Any]:
        """Get internal transactions."""
        return await self._make_request("/internal-transactions")
    
    async def get_main_page_transactions(self) -> List[Dict[str, Any]]:
        """Get main page transactions."""
        return await self._make_request("/main-page/transactions")
    
    async def get_main_page_blocks(self) -> List[Dict[str, Any]]:
        """Get main page blocks."""
        return await self._make_request("/main-page/blocks")
    
    async def get_indexing_status(self) -> Dict[str, Any]:
        """Get indexing status."""
        return await self._make_request("/main-page/indexing-status")
    
    async def get_stats(self) -> Dict[str, Any]:
        """Get statistics counters."""
        return await self._make_request("/stats")
    
    async def get_transactions_chart(self) -> Dict[str, Any]:
        """Get transactions chart data."""
        return await self._make_request("/stats/charts/transactions")
    
    async def get_market_chart(self) -> Dict[str, Any]:
        """Get market chart data."""
        return await self._make_request("/stats/charts/market")
    
    async def get_transaction(self, transaction_hash: str) -> Dict[str, Any]:
        """Get transaction details by hash."""
        return await self._make_request(f"/transactions/{transaction_hash}")
    
    async def get_transaction_token_transfers(
        self,
        transaction_hash: str,
        type: Optional[str] = None
    ) -> Dict[str, Any]:
        """Get token transfers for a specific transaction."""
        params = {}
        if type:
            params["type"] = type
        return await self._make_request(f"/transactions/{transaction_hash}/token-transfers", params)
    
    async def close(self):
        """Close the HTTP client."""
        await self.client.aclose()


@smithery.server(config_schema=ConfigSchema)
def create_server():
    """Create and configure the DuckChain MCP server."""
    
    server = FastMCP("DuckChain")
    
    # Initialize API client
    api_client = None
    
    async def get_api_client(ctx: Context) -> DuckChainAPI:
        """Get or create API client with session config."""
        nonlocal api_client
        if api_client is None:
            config = ctx.session_config
            api_client = DuckChainAPI(
                timeout=config.timeout
            )
        return api_client
    
    # Search tools
    @server.tool()
    async def search_blockchain(
        query: str,
        ctx: Context
    ) -> str:
        """Search for addresses, tokens, blocks, or transactions on the blockchain."""
        try:
            api = await get_api_client(ctx)
            result = await api.search(query)
            return f"Search results for '{query}':\n{result}"
        except Exception as e:
            return f"Error searching blockchain: {str(e)}"
    
    @server.tool()
    async def check_search_redirect(
        query: str,
        ctx: Context
    ) -> str:
        """Check if a search query should redirect to a specific page."""
        try:
            api = await get_api_client(ctx)
            result = await api.search_redirect(query)
            return f"Search redirect check for '{query}':\n{result}"
        except Exception as e:
            return f"Error checking search redirect: {str(e)}"
    
    # Transaction tools
    @server.tool()
    async def get_transactions(
        filter_type: Optional[str] = None,
        transaction_type: Optional[str] = None,
        method: Optional[str] = None,
        ctx: Context = None
    ) -> str:
        """Get transactions with optional filtering by status, type, or method."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_transactions(filter_type, transaction_type, method)
            return f"Transactions:\n{result}"
        except Exception as e:
            return f"Error getting transactions: {str(e)}"
    
    @server.tool()
    async def get_transaction_details(
        transaction_hash: str,
        ctx: Context
    ) -> str:
        """Get detailed information about a specific transaction by its hash."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_transaction(transaction_hash)
            return f"Transaction details for {transaction_hash}:\n{result}"
        except Exception as e:
            return f"Error getting transaction details: {str(e)}"
    
    @server.tool()
    async def get_transaction_token_transfers(
        transaction_hash: str,
        token_type: Optional[str] = None,
        ctx: Context = None
    ) -> str:
        """Get token transfers for a specific transaction."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_transaction_token_transfers(transaction_hash, token_type)
            return f"Token transfers for transaction {transaction_hash}:\n{result}"
        except Exception as e:
            return f"Error getting transaction token transfers: {str(e)}"
    
    # Block tools
    @server.tool()
    async def get_blocks(
        block_type: Optional[str] = None,
        ctx: Context = None
    ) -> str:
        """Get blocks with optional type filtering (block, uncle, reorg)."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_blocks(block_type)
            return f"Blocks:\n{result}"
        except Exception as e:
            return f"Error getting blocks: {str(e)}"
    
    # Token transfer tools
    @server.tool()
    async def get_token_transfers(ctx: Context) -> str:
        """Get all token transfers."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_token_transfers()
            return f"Token transfers:\n{result}"
        except Exception as e:
            return f"Error getting token transfers: {str(e)}"
    
    # Internal transaction tools
    @server.tool()
    async def get_internal_transactions(ctx: Context) -> str:
        """Get internal transactions."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_internal_transactions()
            return f"Internal transactions:\n{result}"
        except Exception as e:
            return f"Error getting internal transactions: {str(e)}"
    
    # Main page data tools
    @server.tool()
    async def get_main_page_transactions(ctx: Context) -> str:
        """Get transactions for the main page display."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_main_page_transactions()
            return f"Main page transactions:\n{result}"
        except Exception as e:
            return f"Error getting main page transactions: {str(e)}"
    
    @server.tool()
    async def get_main_page_blocks(ctx: Context) -> str:
        """Get blocks for the main page display."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_main_page_blocks()
            return f"Main page blocks:\n{result}"
        except Exception as e:
            return f"Error getting main page blocks: {str(e)}"
    
    @server.tool()
    async def get_indexing_status(ctx: Context) -> str:
        """Get the current indexing status of the blockchain."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_indexing_status()
            return f"Indexing status:\n{result}"
        except Exception as e:
            return f"Error getting indexing status: {str(e)}"
    
    # Statistics tools
    @server.tool()
    async def get_blockchain_stats(ctx: Context) -> str:
        """Get blockchain statistics and counters."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_stats()
            return f"Blockchain statistics:\n{result}"
        except Exception as e:
            return f"Error getting blockchain stats: {str(e)}"
    
    @server.tool()
    async def get_transactions_chart(ctx: Context) -> str:
        """Get transaction chart data for visualization."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_transactions_chart()
            return f"Transactions chart data:\n{result}"
        except Exception as e:
            return f"Error getting transactions chart: {str(e)}"
    
    @server.tool()
    async def get_market_chart(ctx: Context) -> str:
        """Get market chart data for price and volume visualization."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_market_chart()
            return f"Market chart data:\n{result}"
        except Exception as e:
            return f"Error getting market chart: {str(e)}"
    
    # Resources
    @server.resource("duckchain://api-docs")
    def api_documentation() -> str:
        """BlockScout API v2 documentation and available endpoints."""
        return """
        DuckChain MCP Server - BlockScout API v2 Integration
        
        Available Tools:
        
        Search:
        - search_blockchain: Search for addresses, tokens, blocks, or transactions
        - check_search_redirect: Check if search should redirect to specific page
        
        Transactions:
        - get_transactions: Get transactions with filtering options
        - get_transaction_details: Get detailed transaction information
        - get_transaction_token_transfers: Get token transfers for a transaction
        
        Blocks:
        - get_blocks: Get blocks with optional type filtering
        
        Token Operations:
        - get_token_transfers: Get all token transfers
        
        Internal Operations:
        - get_internal_transactions: Get internal transactions
        
        Main Page Data:
        - get_main_page_transactions: Get transactions for main page
        - get_main_page_blocks: Get blocks for main page
        - get_indexing_status: Get blockchain indexing status
        
        Statistics:
        - get_blockchain_stats: Get blockchain statistics
        - get_transactions_chart: Get transaction chart data
        - get_market_chart: Get market chart data
        
        Configuration:
        - timeout: Request timeout in seconds (default: 30)
        """
    
    @server.resource("duckchain://supported-chains")
    def supported_chains() -> str:
        """List of supported blockchain networks."""
        return """
        Supported BlockScout Networks:
        
        - Ethereum Mainnet (blockscout.com/eth/mainnet)
        - Ethereum Goerli (blockscout.com/eth/goerli)
        - Polygon (blockscout.com/matic/mainnet)
        - BSC (blockscout.com/bsc/mainnet)
        - Arbitrum (blockscout.com/arbitrum/mainnet)
        - Optimism (blockscout.com/optimism/mainnet)
        - Avalanche (blockscout.com/avax/mainnet)
        - Fantom (blockscout.com/ftm/mainnet)
        - Gnosis Chain (blockscout.com/gnosis/mainnet)
        - POA Core (blockscout.com/poa/core) - Default
        
        """
    
    # Prompts
    @server.prompt()
    def analyze_transaction(transaction_hash: str) -> list:
        """Generate a prompt to analyze a blockchain transaction."""
        return [
            {
                "role": "user",
                "content": f"Analyze this blockchain transaction: {transaction_hash}. Provide details about the transaction, its purpose, gas usage, and any token transfers involved."
            }
        ]
    
    @server.prompt()
    def explore_address(address: str) -> list:
        """Generate a prompt to explore a blockchain address."""
        return [
            {
                "role": "user",
                "content": f"Explore this blockchain address: {address}. Find information about its transactions, token holdings, and activity patterns."
            }
        ]
    
    @server.prompt()
    def research_token(token_symbol: str) -> list:
        """Generate a prompt to research a token."""
        return [
            {
                "role": "user",
                "content": f"Research the token {token_symbol}. Find its contract address, market data, holders, and recent activity."
            }
        ]
    
    return server
