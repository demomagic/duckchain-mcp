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


# Configuration is no longer needed for Smithery deployment


class DuckChainAPI:
    """BlockScout API client for DuckChain."""
    
    def __init__(self):
        self.base_url = f"https://scan.duckchain.io/api/v2"
        self.timeout = 30
        self.client = httpx.AsyncClient(timeout=self.timeout)
    
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
    
    async def get_block(self, block_number_or_hash: str) -> Dict[str, Any]:
        """Get specific block by number or hash."""
        return await self._make_request(f"/blocks/{block_number_or_hash}")
    
    async def get_block_transactions(self, block_number_or_hash: str) -> Dict[str, Any]:
        """Get transactions for a specific block."""
        return await self._make_request(f"/blocks/{block_number_or_hash}/transactions")
    
    async def get_block_withdrawals(self, block_number_or_hash: str) -> Dict[str, Any]:
        """Get withdrawals for a specific block."""
        return await self._make_request(f"/blocks/{block_number_or_hash}/withdrawals")
    
    async def get_token_transfers(self) -> Dict[str, Any]:
        """Get token transfers."""
        return await self._make_request("/token-transfers")
    
    async def get_internal_transactions(self) -> Dict[str, Any]:
        """Get internal transactions."""
        return await self._make_request("/internal-transactions")
    
    # Address endpoints
    async def get_addresses(self) -> Dict[str, Any]:
        """Get addresses list."""
        return await self._make_request("/addresses")
    
    async def get_address(self, address_hash: str) -> Dict[str, Any]:
        """Get address details by hash."""
        return await self._make_request(f"/addresses/{address_hash}")
    
    async def get_address_counters(self, address_hash: str) -> Dict[str, Any]:
        """Get address counters."""
        return await self._make_request(f"/addresses/{address_hash}/counters")
    
    async def get_address_transactions(self, address_hash: str) -> Dict[str, Any]:
        """Get transactions for a specific address."""
        return await self._make_request(f"/addresses/{address_hash}/transactions")
    
    async def get_address_token_transfers(self, address_hash: str) -> Dict[str, Any]:
        """Get token transfers for a specific address."""
        return await self._make_request(f"/addresses/{address_hash}/token-transfers")
    
    async def get_address_internal_transactions(self, address_hash: str) -> Dict[str, Any]:
        """Get internal transactions for a specific address."""
        return await self._make_request(f"/addresses/{address_hash}/internal-transactions")
    
    async def get_address_logs(self, address_hash: str) -> Dict[str, Any]:
        """Get logs for a specific address."""
        return await self._make_request(f"/addresses/{address_hash}/logs")
    
    async def get_address_blocks_validated(self, address_hash: str) -> Dict[str, Any]:
        """Get blocks validated by a specific address."""
        return await self._make_request(f"/addresses/{address_hash}/blocks-validated")
    
    async def get_address_token_balances(self, address_hash: str) -> Dict[str, Any]:
        """Get token balances for a specific address."""
        return await self._make_request(f"/addresses/{address_hash}/token-balances")
    
    async def get_address_tokens(self, address_hash: str) -> Dict[str, Any]:
        """Get tokens for a specific address."""
        return await self._make_request(f"/addresses/{address_hash}/tokens")
    
    async def get_address_coin_balance_history(self, address_hash: str) -> Dict[str, Any]:
        """Get coin balance history for a specific address."""
        return await self._make_request(f"/addresses/{address_hash}/coin-balance-history")
    
    async def get_address_coin_balance_history_by_day(self, address_hash: str) -> Dict[str, Any]:
        """Get coin balance history by day for a specific address."""
        return await self._make_request(f"/addresses/{address_hash}/coin-balance-history-by-day")
    
    async def get_address_withdrawals(self, address_hash: str) -> Dict[str, Any]:
        """Get withdrawals for a specific address."""
        return await self._make_request(f"/addresses/{address_hash}/withdrawals")
    
    async def get_address_nft(self, address_hash: str) -> Dict[str, Any]:
        """Get NFT for a specific address."""
        return await self._make_request(f"/addresses/{address_hash}/nft")
    
    async def get_address_nft_collections(self, address_hash: str) -> Dict[str, Any]:
        """Get NFT collections for a specific address."""
        return await self._make_request(f"/addresses/{address_hash}/nft/collections")
    
    # Token endpoints
    async def get_tokens(self) -> Dict[str, Any]:
        """Get tokens list."""
        return await self._make_request("/tokens")
    
    async def get_token(self, address_hash: str) -> Dict[str, Any]:
        """Get token details by address hash."""
        return await self._make_request(f"/tokens/{address_hash}")
    
    async def get_token_transfers_by_token(self, address_hash: str) -> Dict[str, Any]:
        """Get transfers for a specific token."""
        return await self._make_request(f"/tokens/{address_hash}/transfers")
    
    async def get_token_holders(self, address_hash: str) -> Dict[str, Any]:
        """Get holders for a specific token."""
        return await self._make_request(f"/tokens/{address_hash}/holders")
    
    async def get_token_counters(self, address_hash: str) -> Dict[str, Any]:
        """Get counters for a specific token."""
        return await self._make_request(f"/tokens/{address_hash}/counters")
    
    async def get_token_instances(self, address_hash: str) -> Dict[str, Any]:
        """Get instances for a specific token."""
        return await self._make_request(f"/tokens/{address_hash}/instances")
    
    async def get_token_instance(self, address_hash: str, instance_id: str) -> Dict[str, Any]:
        """Get specific token instance."""
        return await self._make_request(f"/tokens/{address_hash}/instances/{instance_id}")
    
    async def get_token_instance_transfers(self, address_hash: str, instance_id: str) -> Dict[str, Any]:
        """Get transfers for a specific token instance."""
        return await self._make_request(f"/tokens/{address_hash}/instances/{instance_id}/transfers")
    
    async def get_token_instance_holders(self, address_hash: str, instance_id: str) -> Dict[str, Any]:
        """Get holders for a specific token instance."""
        return await self._make_request(f"/tokens/{address_hash}/instances/{instance_id}/holders")
    
    async def get_token_instance_transfers_count(self, address_hash: str, instance_id: str) -> Dict[str, Any]:
        """Get transfers count for a specific token instance."""
        return await self._make_request(f"/tokens/{address_hash}/instances/{instance_id}/transfers-count")
    
    async def refetch_token_instance_metadata(self, address_hash: str, instance_id: str) -> Dict[str, Any]:
        """Refetch metadata for a specific token instance."""
        return await self._make_request(f"/tokens/{address_hash}/instances/{instance_id}/refetch-metadata")
    
    # Smart contract endpoints
    async def get_smart_contracts(self) -> Dict[str, Any]:
        """Get smart contracts list."""
        return await self._make_request("/smart-contracts")
    
    async def get_smart_contracts_counters(self) -> Dict[str, Any]:
        """Get smart contracts counters."""
        return await self._make_request("/smart-contracts/counters")
    
    async def get_smart_contract(self, address_hash: str) -> Dict[str, Any]:
        """Get smart contract details by address hash."""
        return await self._make_request(f"/smart-contracts/{address_hash}")
    
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
    
    async def get_transaction_internal_transactions(self, transaction_hash: str) -> Dict[str, Any]:
        """Get internal transactions for a specific transaction."""
        return await self._make_request(f"/transactions/{transaction_hash}/internal-transactions")
    
    async def get_transaction_logs(self, transaction_hash: str) -> Dict[str, Any]:
        """Get logs for a specific transaction."""
        return await self._make_request(f"/transactions/{transaction_hash}/logs")
    
    async def get_transaction_raw_trace(self, transaction_hash: str) -> Dict[str, Any]:
        """Get raw trace for a specific transaction."""
        return await self._make_request(f"/transactions/{transaction_hash}/raw-trace")
    
    async def get_transaction_state_changes(self, transaction_hash: str) -> Dict[str, Any]:
        """Get state changes for a specific transaction."""
        return await self._make_request(f"/transactions/{transaction_hash}/state-changes")
    
    async def get_transaction_summary(self, transaction_hash: str) -> Dict[str, Any]:
        """Get summary for a specific transaction."""
        return await self._make_request(f"/transactions/{transaction_hash}/summary")
    
    async def close(self):
        """Close the HTTP client."""
        await self.client.aclose()


@smithery.server()
def create_server():
    """Create and configure the DuckChain MCP server."""
    
    server = FastMCP("DuckChain")
    
    # Initialize API client
    api_client = None
    
    async def get_api_client(ctx: Context) -> DuckChainAPI:
        """Get or create API client."""
        nonlocal api_client
        if api_client is None:
            api_client = DuckChainAPI()
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
    
    @server.tool()
    async def get_transaction_internal_transactions(
        transaction_hash: str,
        ctx: Context
    ) -> str:
        """Get internal transactions for a specific transaction."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_transaction_internal_transactions(transaction_hash)
            return f"Internal transactions for transaction {transaction_hash}:\n{result}"
        except Exception as e:
            return f"Error getting transaction internal transactions: {str(e)}"
    
    @server.tool()
    async def get_transaction_logs(
        transaction_hash: str,
        ctx: Context
    ) -> str:
        """Get logs for a specific transaction."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_transaction_logs(transaction_hash)
            return f"Logs for transaction {transaction_hash}:\n{result}"
        except Exception as e:
            return f"Error getting transaction logs: {str(e)}"
    
    @server.tool()
    async def get_transaction_raw_trace(
        transaction_hash: str,
        ctx: Context
    ) -> str:
        """Get raw trace for a specific transaction."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_transaction_raw_trace(transaction_hash)
            return f"Raw trace for transaction {transaction_hash}:\n{result}"
        except Exception as e:
            return f"Error getting transaction raw trace: {str(e)}"
    
    @server.tool()
    async def get_transaction_state_changes(
        transaction_hash: str,
        ctx: Context
    ) -> str:
        """Get state changes for a specific transaction."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_transaction_state_changes(transaction_hash)
            return f"State changes for transaction {transaction_hash}:\n{result}"
        except Exception as e:
            return f"Error getting transaction state changes: {str(e)}"
    
    @server.tool()
    async def get_transaction_summary(
        transaction_hash: str,
        ctx: Context
    ) -> str:
        """Get summary for a specific transaction."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_transaction_summary(transaction_hash)
            return f"Summary for transaction {transaction_hash}:\n{result}"
        except Exception as e:
            return f"Error getting transaction summary: {str(e)}"
    
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
    
    @server.tool()
    async def get_block_details(
        block_number_or_hash: str,
        ctx: Context
    ) -> str:
        """Get specific block details by number or hash."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_block(block_number_or_hash)
            return f"Block details for {block_number_or_hash}:\n{result}"
        except Exception as e:
            return f"Error getting block details: {str(e)}"
    
    @server.tool()
    async def get_block_transactions(
        block_number_or_hash: str,
        ctx: Context
    ) -> str:
        """Get transactions for a specific block."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_block_transactions(block_number_or_hash)
            return f"Transactions for block {block_number_or_hash}:\n{result}"
        except Exception as e:
            return f"Error getting block transactions: {str(e)}"
    
    @server.tool()
    async def get_block_withdrawals(
        block_number_or_hash: str,
        ctx: Context
    ) -> str:
        """Get withdrawals for a specific block."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_block_withdrawals(block_number_or_hash)
            return f"Withdrawals for block {block_number_or_hash}:\n{result}"
        except Exception as e:
            return f"Error getting block withdrawals: {str(e)}"
    
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
    
    # Address tools
    @server.tool()
    async def get_addresses_list(ctx: Context) -> str:
        """Get addresses list."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_addresses()
            return f"Addresses list:\n{result}"
        except Exception as e:
            return f"Error getting addresses list: {str(e)}"
    
    @server.tool()
    async def get_address_details(
        address_hash: str,
        ctx: Context
    ) -> str:
        """Get address details by hash."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_address(address_hash)
            return f"Address details for {address_hash}:\n{result}"
        except Exception as e:
            return f"Error getting address details: {str(e)}"
    
    @server.tool()
    async def get_address_counters(
        address_hash: str,
        ctx: Context
    ) -> str:
        """Get address counters."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_address_counters(address_hash)
            return f"Address counters for {address_hash}:\n{result}"
        except Exception as e:
            return f"Error getting address counters: {str(e)}"
    
    @server.tool()
    async def get_address_transactions(
        address_hash: str,
        ctx: Context
    ) -> str:
        """Get transactions for a specific address."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_address_transactions(address_hash)
            return f"Transactions for address {address_hash}:\n{result}"
        except Exception as e:
            return f"Error getting address transactions: {str(e)}"
    
    @server.tool()
    async def get_address_token_transfers(
        address_hash: str,
        ctx: Context
    ) -> str:
        """Get token transfers for a specific address."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_address_token_transfers(address_hash)
            return f"Token transfers for address {address_hash}:\n{result}"
        except Exception as e:
            return f"Error getting address token transfers: {str(e)}"
    
    @server.tool()
    async def get_address_internal_transactions(
        address_hash: str,
        ctx: Context
    ) -> str:
        """Get internal transactions for a specific address."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_address_internal_transactions(address_hash)
            return f"Internal transactions for address {address_hash}:\n{result}"
        except Exception as e:
            return f"Error getting address internal transactions: {str(e)}"
    
    @server.tool()
    async def get_address_logs(
        address_hash: str,
        ctx: Context
    ) -> str:
        """Get logs for a specific address."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_address_logs(address_hash)
            return f"Logs for address {address_hash}:\n{result}"
        except Exception as e:
            return f"Error getting address logs: {str(e)}"
    
    @server.tool()
    async def get_address_blocks_validated(
        address_hash: str,
        ctx: Context
    ) -> str:
        """Get blocks validated by a specific address."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_address_blocks_validated(address_hash)
            return f"Blocks validated by address {address_hash}:\n{result}"
        except Exception as e:
            return f"Error getting address blocks validated: {str(e)}"
    
    @server.tool()
    async def get_address_token_balances(
        address_hash: str,
        ctx: Context
    ) -> str:
        """Get token balances for a specific address."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_address_token_balances(address_hash)
            return f"Token balances for address {address_hash}:\n{result}"
        except Exception as e:
            return f"Error getting address token balances: {str(e)}"
    
    @server.tool()
    async def get_address_tokens(
        address_hash: str,
        ctx: Context
    ) -> str:
        """Get tokens for a specific address."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_address_tokens(address_hash)
            return f"Tokens for address {address_hash}:\n{result}"
        except Exception as e:
            return f"Error getting address tokens: {str(e)}"
    
    @server.tool()
    async def get_address_coin_balance_history(
        address_hash: str,
        ctx: Context
    ) -> str:
        """Get coin balance history for a specific address."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_address_coin_balance_history(address_hash)
            return f"Coin balance history for address {address_hash}:\n{result}"
        except Exception as e:
            return f"Error getting address coin balance history: {str(e)}"
    
    @server.tool()
    async def get_address_coin_balance_history_by_day(
        address_hash: str,
        ctx: Context
    ) -> str:
        """Get coin balance history by day for a specific address."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_address_coin_balance_history_by_day(address_hash)
            return f"Coin balance history by day for address {address_hash}:\n{result}"
        except Exception as e:
            return f"Error getting address coin balance history by day: {str(e)}"
    
    @server.tool()
    async def get_address_withdrawals(
        address_hash: str,
        ctx: Context
    ) -> str:
        """Get withdrawals for a specific address."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_address_withdrawals(address_hash)
            return f"Withdrawals for address {address_hash}:\n{result}"
        except Exception as e:
            return f"Error getting address withdrawals: {str(e)}"
    
    @server.tool()
    async def get_address_nft(
        address_hash: str,
        ctx: Context
    ) -> str:
        """Get NFT for a specific address."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_address_nft(address_hash)
            return f"NFT for address {address_hash}:\n{result}"
        except Exception as e:
            return f"Error getting address NFT: {str(e)}"
    
    @server.tool()
    async def get_address_nft_collections(
        address_hash: str,
        ctx: Context
    ) -> str:
        """Get NFT collections for a specific address."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_address_nft_collections(address_hash)
            return f"NFT collections for address {address_hash}:\n{result}"
        except Exception as e:
            return f"Error getting address NFT collections: {str(e)}"
    
    # Token tools
    @server.tool()
    async def get_tokens_list(ctx: Context) -> str:
        """Get tokens list."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_tokens()
            return f"Tokens list:\n{result}"
        except Exception as e:
            return f"Error getting tokens list: {str(e)}"
    
    @server.tool()
    async def get_token_details(
        address_hash: str,
        ctx: Context
    ) -> str:
        """Get token details by address hash."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_token(address_hash)
            return f"Token details for {address_hash}:\n{result}"
        except Exception as e:
            return f"Error getting token details: {str(e)}"
    
    @server.tool()
    async def get_token_transfers_by_token(
        address_hash: str,
        ctx: Context
    ) -> str:
        """Get transfers for a specific token."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_token_transfers_by_token(address_hash)
            return f"Transfers for token {address_hash}:\n{result}"
        except Exception as e:
            return f"Error getting token transfers: {str(e)}"
    
    @server.tool()
    async def get_token_holders(
        address_hash: str,
        ctx: Context
    ) -> str:
        """Get holders for a specific token."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_token_holders(address_hash)
            return f"Holders for token {address_hash}:\n{result}"
        except Exception as e:
            return f"Error getting token holders: {str(e)}"
    
    @server.tool()
    async def get_token_counters(
        address_hash: str,
        ctx: Context
    ) -> str:
        """Get counters for a specific token."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_token_counters(address_hash)
            return f"Counters for token {address_hash}:\n{result}"
        except Exception as e:
            return f"Error getting token counters: {str(e)}"
    
    @server.tool()
    async def get_token_instances(
        address_hash: str,
        ctx: Context
    ) -> str:
        """Get instances for a specific token."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_token_instances(address_hash)
            return f"Instances for token {address_hash}:\n{result}"
        except Exception as e:
            return f"Error getting token instances: {str(e)}"
    
    @server.tool()
    async def get_token_instance_details(
        address_hash: str,
        instance_id: str,
        ctx: Context
    ) -> str:
        """Get specific token instance details."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_token_instance(address_hash, instance_id)
            return f"Token instance details for {address_hash}/{instance_id}:\n{result}"
        except Exception as e:
            return f"Error getting token instance details: {str(e)}"
    
    @server.tool()
    async def get_token_instance_transfers(
        address_hash: str,
        instance_id: str,
        ctx: Context
    ) -> str:
        """Get transfers for a specific token instance."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_token_instance_transfers(address_hash, instance_id)
            return f"Transfers for token instance {address_hash}/{instance_id}:\n{result}"
        except Exception as e:
            return f"Error getting token instance transfers: {str(e)}"
    
    @server.tool()
    async def get_token_instance_holders(
        address_hash: str,
        instance_id: str,
        ctx: Context
    ) -> str:
        """Get holders for a specific token instance."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_token_instance_holders(address_hash, instance_id)
            return f"Holders for token instance {address_hash}/{instance_id}:\n{result}"
        except Exception as e:
            return f"Error getting token instance holders: {str(e)}"
    
    @server.tool()
    async def get_token_instance_transfers_count(
        address_hash: str,
        instance_id: str,
        ctx: Context
    ) -> str:
        """Get transfers count for a specific token instance."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_token_instance_transfers_count(address_hash, instance_id)
            return f"Transfers count for token instance {address_hash}/{instance_id}:\n{result}"
        except Exception as e:
            return f"Error getting token instance transfers count: {str(e)}"
    
    @server.tool()
    async def refetch_token_instance_metadata_tool(
        address_hash: str,
        instance_id: str,
        ctx: Context
    ) -> str:
        """Refetch metadata for a specific token instance."""
        try:
            api = await get_api_client(ctx)
            result = await api.refetch_token_instance_metadata(address_hash, instance_id)
            return f"Metadata refetch result for token instance {address_hash}/{instance_id}:\n{result}"
        except Exception as e:
            return f"Error refetching token instance metadata: {str(e)}"
    
    # Smart contract tools
    @server.tool()
    async def get_smart_contracts_list(ctx: Context) -> str:
        """Get smart contracts list."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_smart_contracts()
            return f"Smart contracts list:\n{result}"
        except Exception as e:
            return f"Error getting smart contracts list: {str(e)}"
    
    @server.tool()
    async def get_smart_contracts_counters(ctx: Context) -> str:
        """Get smart contracts counters."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_smart_contracts_counters()
            return f"Smart contracts counters:\n{result}"
        except Exception as e:
            return f"Error getting smart contracts counters: {str(e)}"
    
    @server.tool()
    async def get_smart_contract_details(
        address_hash: str,
        ctx: Context
    ) -> str:
        """Get smart contract details by address hash."""
        try:
            api = await get_api_client(ctx)
            result = await api.get_smart_contract(address_hash)
            return f"Smart contract details for {address_hash}:\n{result}"
        except Exception as e:
            return f"Error getting smart contract details: {str(e)}"
    
    # # Resources
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
        - get_transaction_internal_transactions: Get internal transactions for a transaction
        - get_transaction_logs: Get logs for a transaction
        - get_transaction_raw_trace: Get raw trace for a transaction
        - get_transaction_state_changes: Get state changes for a transaction
        - get_transaction_summary: Get summary for a transaction
        
        Blocks:
        - get_blocks: Get blocks with optional type filtering
        - get_block_details: Get specific block details by number or hash
        - get_block_transactions: Get transactions for a specific block
        - get_block_withdrawals: Get withdrawals for a specific block
        
        Address Operations:
        - get_addresses_list: Get addresses list
        - get_address_details: Get address details by hash
        - get_address_counters: Get address counters
        - get_address_transactions: Get transactions for a specific address
        - get_address_token_transfers: Get token transfers for a specific address
        - get_address_internal_transactions: Get internal transactions for a specific address
        - get_address_logs: Get logs for a specific address
        - get_address_blocks_validated: Get blocks validated by a specific address
        - get_address_token_balances: Get token balances for a specific address
        - get_address_tokens: Get tokens for a specific address
        - get_address_coin_balance_history: Get coin balance history for a specific address
        - get_address_coin_balance_history_by_day: Get coin balance history by day for a specific address
        - get_address_withdrawals: Get withdrawals for a specific address
        - get_address_nft: Get NFT for a specific address
        - get_address_nft_collections: Get NFT collections for a specific address
        
        Token Operations:
        - get_token_transfers: Get all token transfers
        - get_tokens_list: Get tokens list
        - get_token_details: Get token details by address hash
        - get_token_transfers_by_token: Get transfers for a specific token
        - get_token_holders: Get holders for a specific token
        - get_token_counters: Get counters for a specific token
        - get_token_instances: Get instances for a specific token
        - get_token_instance_details: Get specific token instance details
        - get_token_instance_transfers: Get transfers for a specific token instance
        - get_token_instance_holders: Get holders for a specific token instance
        - get_token_instance_transfers_count: Get transfers count for a specific token instance
        - refetch_token_instance_metadata_tool: Refetch metadata for a specific token instance
        
        Smart Contract Operations:
        - get_smart_contracts_list: Get smart contracts list
        - get_smart_contracts_counters: Get smart contracts counters
        - get_smart_contract_details: Get smart contract details by address hash
        
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
         - No configuration required - uses default settings
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
