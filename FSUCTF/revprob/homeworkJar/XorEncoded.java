public class XorEncoded {
    public static char[] getPart() {
        // Direct representation of the XOR-ed string "0\`7w`k2md"
        String encoded = "0\\`7w`k2md";
        char[] encodedChars = new char[encoded.length()];
        for (int i = 0; i < encoded.length(); i++) {
            encodedChars[i] = encoded.charAt(i);
        }
        return encodedChars;
    }
}
