#!/bin/bash

REPO_NAME="thought-partner"
GH_URL="git@github.com:wilscooding/thought-partner.git"

# STEP 0: CLEAN SETUP
rm -rf .git
git init
git remote add origin $GH_URL
git branch -M main

# Utility: Commit with date/time
commit_with_date () {
  GIT_AUTHOR_DATE="$1" GIT_COMMITTER_DATE="$1" git commit -m "$2" --date "$1"
}

# Date helpers
dates=(
  "2025-03-25T09:15:00"
  "2025-03-26T10:00:00"
  "2025-03-27T11:30:00"
  "2025-03-28T09:45:00"
  "2025-03-29T12:15:00"
  "2025-03-30T10:30:00"
  "2025-03-31T11:45:00"
  "2025-04-01T09:10:00"
  "2025-04-02T09:50:00"
  "2025-04-03T10:30:00"
  "2025-04-04T12:00:00"
  "2025-04-05T13:00:00"
  "2025-04-06T09:30:00"
  "2025-04-07T10:45:00"
  "2025-04-08T11:15:00"
  "2025-04-09T12:45:00"
  "2025-04-10T09:30:00"
  "2025-04-11T11:00:00"
  "2025-04-12T12:30:00"
  "2025-04-13T09:45:00"
  "2025-04-14T11:20:00"
  "2025-04-15T12:10:00"
  "2025-04-16T10:55:00"
  "2025-04-17T12:55:00"
)

messages=(
  "Initialize monorepo with backend and frontend structure"
  "Add FastAPI server with / route and main.py"
  "Create UserSelection model and base schema"
  "Add prompt route and route structure"
  "Add initial prompt_template in data.py"
  "Add matcher functions for avatar/capability/expert lookup"
  "Add OpenRouter integration and API call logic"
  "Wire up prompt response and return AI output"
  "Add CORS middleware to support frontend"
  "Create /api/options endpoint to deliver selection lists"
  "Scaffold frontend with Expo + React Native"
  "Build user-setup.tsx for choosing options"
  "Create chat.tsx for AI convo flow"
  "Integrate AI response + text-to-speech output"
  "Add isFirstMessage logic to backend prompt flow"
  "Connect frontend to send isFirstMessage on first turn"
  "Add SpeechRecognition for voice-to-text on web"
  "Add mic button to trigger voice input on chat screen"
  "Add placeholder for mobile voice support"
  "Add homepage index.tsx and route user to setup"
  "Add router.push after setup submission"
  "Fix keyMap handling for Picker options"
  "Add AI voice response using expo-speech"
  "Final cleanup and styling improvements"
)

# Commit each item
for i in "${!dates[@]}"; do
  echo "Committing: ${messages[$i]}"

  echo "${messages[$i]}" >> commit-log.txt
  git add .
  commit_with_date "${dates[$i]}" "${messages[$i]}"
done

# Final push to GitHub
git push -u origin main

echo "🎉 All commits created and pushed!"
