 
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;


public class RobinKarp {

	
	public static void main(String[] args) throws IOException {
	
		Scanner in = new Scanner(System.in);

		
		char[] org = in.nextLine().toCharArray();
		
		String t = in.nextLine();
		
		int[] freq = new int[27];
		
		for(char c : org) {
			if(c == '?') {
				freq[26]++;
			}
			else {
				freq[c - 'a']++;	
			}
		}
		
		
		List<Character> need = new ArrayList<>();

	mug:while(true) {
			
			
			for(int i=0; i<t.length(); i++) {
				
				int cur = (char) (t.charAt(i) - 'a');
				
				if(freq[cur] <= 0) {
					
					if(freq[26] == 0){
						break mug;
					}
					else {
						need.add((char) (cur  + 'a'));
						freq[26]--;
					}
				}
				else {
					freq[cur]--;
				}
				
			}
			
		}
		
		PrintWriter out = new PrintWriter(System.out);
		List<Character> sd = new ArrayList<>();
		
		for(int i=0; i<org.length; i++) {
			
			if(org[i] == '?') {
				out.print(need.get(need.size()-1));
				need.remove(need.size()-1);
			}
			else {
				out.print(org[i]);
			}
		}
		
		out.close();

		
		
	}

}