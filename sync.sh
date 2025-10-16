#!/bin/bash
# Quick Git Sync Script for Event Planner System
# This script helps you sync your work with your friends

echo "🔄 Event Planner System - Git Sync Tool"
echo "========================================"
echo ""

# Pull latest changes
echo "📥 Pulling latest changes from GitHub..."
git pull origin main

if [ $? -eq 0 ]; then
    echo "✅ Successfully pulled latest changes!"
    echo ""

    # Show status
    echo "📊 Current status:"
    git status
    echo ""

    # Ask if user wants to push changes
    read -p "Do you want to commit and push your changes? (y/n): " answer

    if [ "$answer" = "y" ] || [ "$answer" = "Y" ]; then
        read -p "Enter commit message: " message

        git add .
        git commit -m "$message"
        git push origin main

        echo ""
        echo "✅ Changes pushed to GitHub!"
        echo "🎉 Your friends can now pull your changes!"
    else
        echo "ℹ️  No changes pushed. Run this script again when ready."
    fi
else
    echo "❌ Error pulling changes. Please resolve conflicts manually."
    echo "Run: git status"
fi

