import java.util.*;
// warm-up
// Not exactly correct with previous observation. Using indexOf within an
// O(n^2) block was a major slow down. Pattern mismatching is potentially
// faster than pattern match since we have to search for every possible
// pattern substring.
// Solution ripped off from a red coder just for personal reference
public class Round110ProblemA {

	static void solve() {
		Scanner sc = new Scanner(System.in);
		String s = sc.next(), t = sc.next();
		int min = 5000;
		for(int i = 0; i<2001; i++) s = "."+s+".";
		for(int i = 0; i<=s.length()-t.length(); i++) {
			int count = 0;
			for(int j = 0; j<t.length(); j++) 
				if(s.charAt(i+j)!= t.charAt(j)) count++;
			min = Math.min(min, count);
		}
		System.out.println(min);
		sc.close();			
	}

	public static void main(String args[]) {
		solve();
	}

}