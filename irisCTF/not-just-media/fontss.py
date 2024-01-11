import fontforge

# Open the font file
font = fontforge.open('font2.ttf')

# Loop through each glyph in the font
for glyph in font.glyphs():
    # Print out the glyph's encoding and its name
    print(f"Character: {chr(glyph.unicode)}, Name: {glyph.glyphname}")
