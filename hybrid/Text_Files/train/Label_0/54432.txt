import java.util.*;

public class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = Integer.parseInt(sc.nextLine());
		char[] arr = sc.nextLine().toCharArray();
		boolean prev = arr[0] == 'T';
		for (int i = 2; i < arr.length; i += 2) {
		    prev = check(prev, arr[i] == 'T');
		}
		String ans;
		if (prev) {
		    ans = "T";
		} else {
		    ans = "F";
		}
		System.out.println(ans);
	}
	
	static boolean check(boolean a, boolean b) {
	    if (a && !b) {
	        return false;
	    } else {
	        return true;
	    }
	}
}

