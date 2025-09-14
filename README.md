# DuckChain MCP Server

A comprehensive Model Context Protocol (MCP) server that provides complete access to blockchain data via the BlockScout API v2 specification. DuckChain enables AI assistants to perform deep blockchain analysis, including transaction tracing, address exploration, token management, smart contract analysis, and comprehensive market research with 56+ specialized tools.

## Features

### 🔍 Search & Discovery
- **Blockchain Search**: Search for addresses, tokens, blocks, or transactions
- **Search Redirects**: Check if queries should redirect to specific pages

### 📊 Transaction Analysis
- **Transaction Details**: Get comprehensive transaction information by hash
- **Transaction Filtering**: Filter transactions by status, type, or method
- **Token Transfers**: Retrieve token transfer details for specific transactions
- **Internal Transactions**: Access internal transaction data for specific transactions
- **Transaction Logs**: Get detailed logs for transaction analysis
- **Raw Trace**: Access raw transaction trace data
- **State Changes**: Monitor state changes caused by transactions
- **Transaction Summary**: Get concise transaction summaries

### 🧱 Block Operations
- **Block Data**: Access block information with optional type filtering
- **Block Details**: Get specific block details by number or hash
- **Block Transactions**: Retrieve all transactions in a specific block
- **Block Withdrawals**: Access withdrawal data for specific blocks
- **Main Page Blocks**: Get blocks optimized for main page display

### 🏠 Address Analysis
- **Address Details**: Get comprehensive address information
- **Address Transactions**: Access all transactions for specific addresses
- **Token Balances**: Check token balances for any address
- **Balance History**: Track coin balance changes over time
- **NFT Management**: Access NFT data and collections for addresses
- **Address Counters**: Get transaction and activity counters
- **Validated Blocks**: See blocks validated by specific addresses
- **Withdrawal History**: Track withdrawal activities

### 💰 Token Operations
- **Token Management**: Complete token lifecycle management
- **Token Details**: Get comprehensive token information
- **Token Transfers**: Access all token transfer data
- **Token Holders**: Analyze token distribution and holders
- **Token Instances**: Manage token instances and metadata
- **Token Counters**: Track token activity statistics
- **Metadata Refresh**: Update token instance metadata

### 📜 Smart Contract Analysis
- **Contract Details**: Get comprehensive smart contract information
- **Contract Lists**: Browse all smart contracts
- **Contract Counters**: Track smart contract activity
- **Contract Analysis**: Analyze contract interactions and usage

### 📈 Statistics & Charts
- **Blockchain Stats**: Get comprehensive blockchain statistics
- **Transaction Charts**: Access transaction volume and activity data
- **Market Charts**: Retrieve price and volume visualization data

### 🔧 Internal Operations
- **Internal Transactions**: Access internal transaction data
- **Indexing Status**: Monitor blockchain indexing progress

## 🚀 What's New

### Complete API Coverage
- **56+ MCP Tools** covering all BlockScout API v2 endpoints
- **Advanced Transaction Analysis** with logs, traces, and state changes
- **Comprehensive Address Analysis** including NFT and balance history
- **Full Token Management** with instances and metadata refresh
- **Smart Contract Analysis** with detailed contract information
- **Deep Block Analysis** including withdrawals and transaction details

### Enhanced Capabilities
- **No Authentication Required** - Works out of the box
- **Type-Safe Implementation** - Full Pydantic validation
- **Comprehensive Error Handling** - User-friendly error messages
- **Async Performance** - Fast, non-blocking operations
- **Modular Design** - Easy to extend and maintain

## Prerequisites

- **Smithery API key**: Get yours at [smithery.ai/account/api-keys](https://smithery.ai/account/api-keys)
- Python 3.10 or higher

## Supported Networks

DuckChain supports all BlockScout-compatible networks including:

- **Ethereum Mainnet** (`blockscout.com/eth/mainnet`)
- **Polygon** (`blockscout.com/matic/mainnet`)
- **BSC** (`blockscout.com/bsc/mainnet`)
- **Arbitrum** (`blockscout.com/arbitrum/mainnet`)
- **Optimism** (`blockscout.com/optimism/mainnet`)
- **Avalanche** (`blockscout.com/avax/mainnet`)
- **Fantom** (`blockscout.com/ftm/mainnet`)
- **Gnosis Chain** (`blockscout.com/gnosis/mainnet`)
- **POA Core** (`blockscout.com/poa/core`) - Default

## Getting Started

1. **Install dependencies**:
   ```bash
   uv sync
   ```

2. **Run the server**:
   ```bash
   uv run dev
   ```

3. **Test interactively**:
   ```bash
   uv run playground
   ```

## Configuration

Configure DuckChain by setting these parameters in your MCP client:

```json
{
  "timeout": 30
}
```

### Configuration Options

- **`timeout`**: Request timeout in seconds (default: 30)

### No Authentication Required

- **Free and public access** - Most BlockScout instances are free and public
- **No API key needed** - DuckChain works without any authentication
- **Simple setup** - Just configure the server URL and you're ready to go

## Usage Examples

### Search Operations
```
Search for USDT token information
Search for address 0x1234...
Find block 12345678
```

### Transaction Analysis
```
Get transaction details for 0xabc123...
Get token transfers for transaction 0xdef456...
Get internal transactions for transaction 0xdef456...
Get transaction logs for 0xdef456...
Get raw trace for transaction 0xdef456...
Get state changes for transaction 0xdef456...
Get transaction summary for 0xdef456...
Filter transactions by method "transfer"
```

### Block Analysis
```
Get block details for block 12345678
Get all transactions in block 12345678
Get withdrawals for block 12345678
Get blocks with type filtering
```

### Address Analysis
```
Get address details for 0x1234...
Get all transactions for address 0x1234...
Get token balances for address 0x1234...
Get coin balance history for address 0x1234...
Get NFT collections for address 0x1234...
Get blocks validated by address 0x1234...
```

### Token Management
```
Get token details for 0xabc123...
Get token holders for 0xabc123...
Get token transfers for 0xabc123...
Get token instances for 0xabc123...
Refetch token instance metadata
```

### Smart Contract Analysis
```
Get smart contract details for 0xdef456...
Get smart contracts list
Get smart contract counters
```

### Market Research
```
Get blockchain statistics
Show transaction chart data
Display market chart for price analysis
```

## Available Tools

### Search Tools
- `search_blockchain`: Search for addresses, tokens, blocks, or transactions
- `check_search_redirect`: Check if search should redirect to specific page

### Transaction Tools
- `get_transactions`: Get transactions with filtering options
- `get_transaction_details`: Get detailed transaction information
- `get_transaction_token_transfers`: Get token transfers for a transaction
- `get_transaction_internal_transactions`: Get internal transactions for a transaction
- `get_transaction_logs`: Get logs for a transaction
- `get_transaction_raw_trace`: Get raw trace for a transaction
- `get_transaction_state_changes`: Get state changes for a transaction
- `get_transaction_summary`: Get summary for a transaction

### Block Tools
- `get_blocks`: Get blocks with optional type filtering
- `get_block_details`: Get specific block details by number or hash
- `get_block_transactions`: Get transactions for a specific block
- `get_block_withdrawals`: Get withdrawals for a specific block

### Address Tools
- `get_addresses_list`: Get addresses list
- `get_address_details`: Get address details by hash
- `get_address_counters`: Get address counters
- `get_address_transactions`: Get transactions for a specific address
- `get_address_token_transfers`: Get token transfers for a specific address
- `get_address_internal_transactions`: Get internal transactions for a specific address
- `get_address_logs`: Get logs for a specific address
- `get_address_blocks_validated`: Get blocks validated by a specific address
- `get_address_token_balances`: Get token balances for a specific address
- `get_address_tokens`: Get tokens for a specific address
- `get_address_coin_balance_history`: Get coin balance history for a specific address
- `get_address_coin_balance_history_by_day`: Get coin balance history by day for a specific address
- `get_address_withdrawals`: Get withdrawals for a specific address
- `get_address_nft`: Get NFT for a specific address
- `get_address_nft_collections`: Get NFT collections for a specific address

### Token Tools
- `get_token_transfers`: Get all token transfers
- `get_tokens_list`: Get tokens list
- `get_token_details`: Get token details by address hash
- `get_token_transfers_by_token`: Get transfers for a specific token
- `get_token_holders`: Get holders for a specific token
- `get_token_counters`: Get counters for a specific token
- `get_token_instances`: Get instances for a specific token
- `get_token_instance_details`: Get specific token instance details
- `get_token_instance_transfers`: Get transfers for a specific token instance
- `get_token_instance_holders`: Get holders for a specific token instance
- `get_token_instance_transfers_count`: Get transfers count for a specific token instance
- `refetch_token_instance_metadata_tool`: Refetch metadata for a specific token instance

### Smart Contract Tools
- `get_smart_contracts_list`: Get smart contracts list
- `get_smart_contracts_counters`: Get smart contracts counters
- `get_smart_contract_details`: Get smart contract details by address hash

### Internal Tools
- `get_internal_transactions`: Get internal transactions

### Main Page Tools
- `get_main_page_transactions`: Get transactions for main page
- `get_main_page_blocks`: Get blocks for main page
- `get_indexing_status`: Get blockchain indexing status

### Statistics Tools
- `get_blockchain_stats`: Get blockchain statistics
- `get_transactions_chart`: Get transaction chart data
- `get_market_chart`: Get market chart data

## Resources

- `duckchain://api-docs`: Complete API documentation
- `duckchain://supported-chains`: List of supported blockchain networks

## Prompts

- `analyze_transaction`: Generate analysis prompts for transactions
- `explore_address`: Generate exploration prompts for addresses
- `research_token`: Generate research prompts for tokens

## Development

The server code is located in `src/duckchain/server.py`. The implementation follows the BlockScout API v2 specification and provides comprehensive error handling and type safety.

### Key Components

- **DuckChainAPI**: Async HTTP client for BlockScout API with 56+ endpoints
- **ConfigSchema**: Pydantic model for configuration validation
- **MCP Tools**: 56+ individual tools covering all major blockchain operations
- **Resources**: Documentation and reference materials
- **Prompts**: Pre-built prompts for common blockchain analysis tasks

### API Coverage

- **Search & Discovery**: 2 tools
- **Transaction Analysis**: 8 tools (including logs, traces, state changes)
- **Block Operations**: 4 tools (including withdrawals and detailed analysis)
- **Address Analysis**: 15 tools (comprehensive address data and history)
- **Token Management**: 12 tools (including instances and metadata)
- **Smart Contract Analysis**: 3 tools
- **Statistics & Charts**: 3 tools
- **Internal Operations**: 1 tool
- **Main Page Data**: 3 tools

**Total: 56+ MCP tools covering the complete BlockScout API v2 specification**

## Deploy

Ready to deploy? Push your code to GitHub and deploy to Smithery:

1. Clone repository at [duckchain-mcp](https://github.com/demomagic/duckchain-mcp)

2. Deploy your server to Smithery at [smithery.ai/new](https://smithery.ai/new)

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For support and questions, please open an issue on GitHub or contact the DuckChain team.
