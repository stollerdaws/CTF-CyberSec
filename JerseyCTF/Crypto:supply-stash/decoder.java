import java.lang.Math;
import java.util.ArrayList;
import java.util.Scanner;

public class decoder {
    public static void main(String[] args) {
        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the number of encoded blocks: ");
        int blockCount = sc.nextInt();
        ArrayList<Integer> encodedBlocks = new ArrayList<Integer>();

        for (int i = 0; i < blockCount; i++) {
            System.out.println("Enter encoded block #" + (i + 1) + ":");
            int block = sc.nextInt();
            encodedBlocks.add(block);
        }

        System.out.println("Enter int block size: ");
        int r = sc.nextInt();

        StringBuilder decodedMessage = new StringBuilder();
        for (int num : encodedBlocks) {
            int power = r - 1;
            StringBuilder block = new StringBuilder();
            while (power >= 0) {
                int letterValue = num / (int) Math.pow(26, power);
                block.append(alphabet.charAt(letterValue));
                num -= letterValue * Math.pow(26, power);
                power--;
            }
            decodedMessage.append(block);
        }

        // Remove padding
        String decoded = decodedMessage.toString().replaceAll("x+$", "");
        System.out.println("Decoded message: " + decoded);
    }
}