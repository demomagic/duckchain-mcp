# DuckChain MCP Server

A comprehensive Model Context Protocol (MCP) server that provides access to blockchain data via the BlockScout API v2 specification. DuckChain enables AI assistants to interact with blockchain data, search transactions, analyze addresses, and retrieve market statistics.

## Features

### 🔍 Search & Discovery
- **Blockchain Search**: Search for addresses, tokens, blocks, or transactions
- **Search Redirects**: Check if queries should redirect to specific pages

### 📊 Transaction Analysis
- **Transaction Details**: Get comprehensive transaction information by hash
- **Transaction Filtering**: Filter transactions by status, type, or method
- **Token Transfers**: Retrieve token transfer details for specific transactions

### 🧱 Block Operations
- **Block Data**: Access block information with optional type filtering
- **Main Page Blocks**: Get blocks optimized for main page display

### 💰 Token Operations
- **Token Transfers**: Access all token transfer data
- **Token Analysis**: Research token contracts, holders, and market data

### 📈 Statistics & Charts
- **Blockchain Stats**: Get comprehensive blockchain statistics
- **Transaction Charts**: Access transaction volume and activity data
- **Market Charts**: Retrieve price and volume visualization data

### 🔧 Internal Operations
- **Internal Transactions**: Access internal transaction data
- **Indexing Status**: Monitor blockchain indexing progress

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
  "server_url": "blockscout.com/poa/core",
  "timeout": 30
}
```

### Configuration Options

- **`server_url`**: BlockScout server URL (default: `blockscout.com/poa/core`)
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
Filter transactions by method "transfer"
```

### Market Research
```
Get blockchain statistics
Show transaction chart data
Display market chart for price analysis
```

### Address Exploration
```
Analyze address 0x1234... for activity patterns
Get all transactions for address 0x5678...
```

## Available Tools

### Search Tools
- `search_blockchain`: Search for addresses, tokens, blocks, or transactions
- `check_search_redirect`: Check if search should redirect to specific page

### Transaction Tools
- `get_transactions`: Get transactions with filtering options
- `get_transaction_details`: Get detailed transaction information
- `get_transaction_token_transfers`: Get token transfers for a transaction

### Block Tools
- `get_blocks`: Get blocks with optional type filtering

### Token Tools
- `get_token_transfers`: Get all token transfers

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

- **DuckChainAPI**: Async HTTP client for BlockScout API
- **ConfigSchema**: Pydantic model for configuration validation
- **MCP Tools**: Individual tools for each API endpoint
- **Resources**: Documentation and reference materials
- **Prompts**: Pre-built prompts for common blockchain analysis tasks

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
