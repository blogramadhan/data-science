#!/bin/bash

# Script untuk mengonversi semua Markdown slides ke PDF dan PPTX
# Menggunakan Marp CLI

set -e

echo "🎨 Converting Marp Markdown slides..."
echo ""

# Buat folder output jika belum ada
mkdir -p pdf ppt

# Counter
converted=0
total=$(ls -1 *.md 2>/dev/null | wc -l)

if [ $total -eq 0 ]; then
    echo "❌ Tidak ada file .md ditemukan!"
    exit 1
fi

# Loop semua file .md
for file in *.md; do
    if [ -f "$file" ]; then
        filename="${file%.md}"
        echo "📄 Converting: $file"

        # Convert to PDF
        echo "   → PDF..."
        marp "$file" --pdf -o "pdf/${filename}.pdf" --allow-local-files 2>&1 | grep -v "^\[" || true

        # Convert to PPTX
        echo "   → PPTX..."
        marp "$file" --pptx -o "ppt/${filename}.pptx" --allow-local-files 2>&1 | grep -v "^\[" || true

        ((converted++))
        echo "   ✅ Done"
        echo ""
    fi
done

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✨ Conversion completed!"
echo "📊 Total converted: $converted/$total files"
echo ""
echo "📁 Output folders:"
echo "   PDF:  $(pwd)/pdf/"
echo "   PPTX: $(pwd)/ppt/"
echo ""

# Show file sizes
echo "📦 File sizes:"
echo "   PDF:  $(du -sh pdf/ | cut -f1)"
echo "   PPTX: $(du -sh ppt/ | cut -f1)"
echo ""

# List files
echo "📄 Generated files:"
echo "PDF:"
ls -1 pdf/*.pdf | sed 's/^/   - /'
echo ""
echo "PPTX:"
ls -1 ppt/*.pptx | sed 's/^/   - /'
