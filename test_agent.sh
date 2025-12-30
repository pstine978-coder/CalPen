#!/bin/bash

echo "============================================================"
echo "Testing PentestAgent (GHOSTCREW)"
echo "============================================================"
echo ""
echo "Starting the agent in test mode..."
echo ""
echo "Note: The agent will start interactively. Type 'quit' to exit."
echo "============================================================"
echo ""

cd /home/kali/Desktop/PentestAgent
.venv/bin/python main.py
