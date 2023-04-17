//Encoding program originally by Logan DesRochers
import java.lang.Math;
import java.util.ArrayList;
import java.util.Scanner; 

public class numericalEncoder{ 
	public static void main(String[] args){ 
		String alphabet = "abcdefghijklmnopqrstuvwxyz";
		Scanner sc = new Scanner(System.in); 
		System.out.println("Enter string to be encoded: ");
		String m = sc.nextLine(); 
		m = m.toLowerCase(); 
		System.out.println("Enter int block size: ");
		int r = sc.nextInt();  

		//padding to variable block size 
		if(m.length() % r != 0){ 
			while(m.length() % r != 0){ 
				m = m + "x";
			}
		}
		System.out.println("M after padding: " + m);
		
		//Variable block size 
		ArrayList<Integer> encodedBlocks = new ArrayList<Integer>();
		int numBlocks = m.length() / r; 
		for(int i = 0; i < numBlocks; i++){ 
			String block = m.substring(i * r, r + i * r); 
			System.out.println(block);
			int power = block.length() - 1;
			int representation = 0;
			for(int j = 0; j < block.length(); j ++){
                        	String currentLetter = block.substring(j,j+1);
                        	int letterValue = alphabet.indexOf(currentLetter);
                        	representation += letterValue * Math.pow(26, power);
                        	power--;
                	} 
			encodedBlocks.add(representation);
		}
	        System.out.println("Encoded blocks are as follows: ");	
		for(int num : encodedBlocks){
			System.out.println(num);
		}
	}
}
