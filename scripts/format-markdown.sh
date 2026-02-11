#!/usr/bin/env bash
#
# Format markdown files for consistency and correctness.
#
# This script performs the following formatting operations:
# - Removes trailing whitespace
# - Ensures consistent line breaks (max 2 consecutive)
# - Validates code block language identifiers
# - Checks for placeholder links
# - Ensures proper heading spacing
#
# Usage:
#   bash format-markdown.sh <file-path>
#

set -euo pipefail

# Check arguments
if [ $# -lt 1 ]; then
    echo "Usage: bash format-markdown.sh <file-path>"
    exit 1
fi

FILE="$1"

# Check if file exists
if [ ! -f "$FILE" ]; then
    echo "Error: File not found: $FILE"
    exit 1
fi

echo "Formatting markdown file: $FILE"

# Create backup
BACKUP="${FILE}.backup"
cp "$FILE" "$BACKUP"
echo "Created backup: $BACKUP"

# 1. Remove trailing whitespace from all lines
echo "  [1/6] Removing trailing whitespace..."
sed -i 's/[[:space:]]*$//' "$FILE"

# 2. Ensure single blank line between paragraphs (max 2 consecutive newlines)
echo "  [2/6] Normalizing paragraph spacing..."
perl -i -pe 's/\n{3,}/\n\n/g' "$FILE"

# 3. Ensure blank line before headings (except at start of file)
echo "  [3/6] Adding spacing before headings..."
perl -i -pe 's/([^\n])\n(#{1,6}\s)/$1\n\n$2/g' "$FILE"

# 4. Ensure blank line after headings
echo "  [4/6] Adding spacing after headings..."
perl -i -pe 's/(^#{1,6}\s+.+)\n([^#\n])/$1\n\n$2/mg' "$FILE"

# 5. Fix code blocks without language identifiers
echo "  [5/6] Checking code block language identifiers..."
# This is a warning, not an auto-fix, since we don't know the intended language
if grep -q '^```$' "$FILE"; then
    echo "  ⚠️  Warning: Found code blocks without language identifiers"
    echo "     Consider specifying languages (javascript, python, typescript, etc.)"
fi

# 6. Check for broken/placeholder links
echo "  [6/6] Checking for placeholder links..."
if grep -q '\[.*\](#)' "$FILE" || grep -q '\[.*\]()' "$FILE"; then
    echo "  ⚠️  Warning: Found placeholder or empty links"
    echo "     Replace with actual URLs or remove"
fi

# Check for TODO markers
if grep -qi 'TODO\|FIXME\|XXX' "$FILE"; then
    echo "  ⚠️  Warning: Found TODO/FIXME markers"
fi

# Check for unfilled template variables
if grep -q '{{.*}}' "$FILE"; then
    echo "  ⚠️  Warning: Found unfilled template variables ({{variable}})"
fi

echo ""
echo "✅ Formatting complete!"
echo "   Original saved to: $BACKUP"
echo "   Formatted file: $FILE"
echo ""

# Optional: Show diff
if command -v diff &> /dev/null; then
    echo "Changes made (showing first 20 lines):"
    diff -u "$BACKUP" "$FILE" | head -n 20 || true
fi

exit 0
