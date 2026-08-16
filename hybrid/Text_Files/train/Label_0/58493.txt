import java.util.Arrays;
import java.util.Scanner;
 
public class Main{
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(true) {
        	int n = Integer.parseInt(sc.nextLine());
        	if(n == 0) break;
        	String vote = sc.nextLine();
        	int[] kouho = new int[26];
        	int[] sokuhou = new int[26];
        	boolean flag = true;
        	for(int i = 0; i < n; i++) {
        		char c = vote.charAt(2 * i);
        		kouho[c - 'A'] += 1;
        		for(int j = 0; j < 26; j++) {
        			sokuhou[j] = kouho[j];
        		}
        		Arrays.sort(sokuhou);
        		if(sokuhou[25] > sokuhou[24] + (n - i - 1)) {
        			int k = 0;
        			while(kouho[k] != sokuhou[25]) {
        				k++;
        			}
        			System.out.printf("%c %d\n", 'A' + k, i + 1);
        			flag = false;
        			break;
        		}
        		
        	}
        	if(flag) {
        		System.out.println("TIE");
        	}
        }
    }
}

