#!/bin/bash

if ! command -v tmux &> /dev/null; then
    echo "❌ tmux is not installed."
    echo "Run 'bin/setup' to try installing it, or use manual start:"
    echo "  ./bin/start backend"
    echo "  ./bin/start frontend"
    exit 1
fi

SESSION="money-manager"

# Check if session exists
tmux has-session -t $SESSION 2>/dev/null

if [ $? != 0 ]; then
  # Create new session
  tmux new-session -d -s $SESSION -n "dev"

  # Set prefix to backtick (`)
  tmux set-option -t $SESSION prefix \`
  tmux unbind-key -t $SESSION C-b
  tmux bind-key -t $SESSION \` send-prefix

  # Pane 1 (Left): Backend
  # Send commands to start backend
  tmux send-keys -t $SESSION:0.0 "bin/start backend" C-m

  # Split window horizontally
  tmux split-window -h -t $SESSION:0.0

  # Pane 2 (Right Top): Frontend
  tmux send-keys -t $SESSION:0.1 "bin/start frontend" C-m

  # Split pane 2 vertically for terminal
  tmux split-window -v -t $SESSION:0.1

  # Pane 3 (Right Bottom): Terminal
  tmux send-keys -t $SESSION:0.2 "echo '🚀 Ready for commands!'" C-m

  # Select the terminal pane
  tmux select-pane -t $SESSION:0.2
fi

# Attach to session
tmux attach-session -t $SESSION
