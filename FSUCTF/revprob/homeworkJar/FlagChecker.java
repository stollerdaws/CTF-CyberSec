import java.util.Base64;
import java.util.Scanner;

public class FlagChecker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Enter the flag:");
        String userInput = scanner.nextLine();
        
        // Reconstruct the flag from the encoded parts
        String reconstructedFlag = reconstructFlag();

        // Check if the user input matches the reconstructed flag
        if(userInput.equals(reconstructedFlag)) {
            System.out.println("Correct flag!");
        } else {
            System.out.println("Incorrect flag. Try again.");
        }
    }

    private static String reconstructFlag() {
        // Decode each part and concatenate
        String part1 = new String(Base64.getDecoder().decode(Base64Encoded.getPart()));
        String part2 = xorDecode(XorEncoded.getPart(), 3); // Assuming the key is 123
        String part3 = new StringBuilder(PlainText.getPart()).reverse().toString(); // Reverse the string
        String part4 = longsToString(IntEncoded.getPart());
        
        return part1 + part2 + part3 + part4;
    }

    private static String xorDecode(char[] encodedChars, int key) {
    StringBuilder decoded = new StringBuilder();
    for (char c : encodedChars) {
        decoded.append((char) (c ^ key));
    }
    return decoded.toString();
}


    private static String longsToString(long[] encoded) {
        StringBuilder sb = new StringBuilder();
        for (long l : encoded) {
            sb.append((char) l);
        }
        return sb.toString();
    }
}
