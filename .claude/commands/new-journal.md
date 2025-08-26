---
allowed-tools: Bash(date:*), LS, Read, Edit
description: Create a new journal entry with today's date in format: month-dd-yyyy-day.md
---

Create a new journal entry file in the `_journal/` directory using today's date in the format: `month-dd-yyyy-day.md`

Current date info: !`date '+%B-%d-%Y-%a' | tr '[:upper:]' '[:lower:]'`

## Requirements:

1. **Create the journal file** with a basic header structure including the date and a useful daily template
2. **Review previous journal entries** to find the most recent entry (check for the last working day, skipping weekends if no entries exist)
3. **Reference relevant information** from the previous entry, specifically:
   - "Tomorrow's Priorities" or "Tomorrow's Plan" section - carry these forward to today's priorities
   - Any "In Progress" items that should continue
   - Important projects or tasks that were mentioned for follow-up
   - Evening tasks or future project notes that are relevant to today
4. **Update today's priorities** section to include carried-forward items from the previous entry
5. **Maintain context** by referencing previous research, ideas, or ongoing work where relevant

## Process:
- First check what journal entries exist in `_journal/` directory
- Read the most recent journal entry (usually the previous working day)
- Extract "Tomorrow's Plan/Priorities", "In Progress", and other forward-looking items
- Create today's journal with those items properly referenced and carried forward
- Structure the new entry to maintain continuity and ensure nothing important gets lost between days