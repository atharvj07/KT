import java.util.*;
import static java.lang.System.*;

public class Main {
	
	static Scanner sc = new Scanner(System.in);
	
	public static void main(String[] args) {
		int num = 0;
		while (sc.hasNext()) {
			if (isPalindrome(sc.next())) {num++;}
		}
		out.println(num);
	}
	
	static boolean isPalindrome (String s) {
		int n = s.length();
		for (int i=0; i<n/2; i++) {
			if (s.charAt(i)!=s.charAt(n-i-1)) {return false;}
		}
		return true;
	}
	
}
