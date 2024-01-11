import fontforge

# Access the font that is currently open
font = fontforge.activeFont()

# Open a file to write the output
with open('/home/ubuntusfs/Downloads/not-just-media/output.txt', 'w') as output_file:
    # Loop over each glyph in the font and write out its codepoint and glyph name
    for glyph in font:
        output_file.write('Unicode: {} Name: {}\n'.format(glyph.unicode, glyph.glyphname))
