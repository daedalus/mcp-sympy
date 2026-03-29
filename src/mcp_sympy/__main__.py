"""Main entry point for the MCP server."""


from mcp_sympy import tools


def main() -> int:
    """Run the MCP server."""
    tools.mcp.run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
