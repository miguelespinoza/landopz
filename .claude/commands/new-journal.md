---
allowed-tools: Bash(date:*)
description: Create a new journal entry with today's date in format: month-dd-yyyy-day.md
---

Create a new journal entry file in the `_journal/` directory using today's date in the format: `month-dd-yyyy-day.md`

Current date info: !`date '+%B-%d-%Y-%a' | tr '[:upper:]' '[:lower:]'`

Create the file with a basic header structure including the date and any initial content or template you think would be useful for a daily journal entry.