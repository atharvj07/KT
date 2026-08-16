import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;

public class Main {
	
	
	
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		String k = s.next();
		String m = s.next();
		
		int n = k.length(),ctr=0;
		for(int i=0;i<n;i++) {
			if(k.charAt(i)!=m.charAt(i)) {
				ctr++;
			}
		}
		System.out.println(ctr);
	}

}
