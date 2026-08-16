import java.util.*;

public class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int[] arr = new int[n];
		for (int i = 0; i < n; i++) {
		    arr[i] = sc.nextInt();
		}
		int upto = lcm(n, m);
		int max = 0;
		int min = 0;
		long total = 0;
		for (int i = 0; i < upto; i++) {
		    if (i % m == 0) {
		        total += max - min;
           		max = 0;
        		min = Integer.MAX_VALUE;
		    }
		    max = Math.max(max, arr[i % n]);
		    min = Math.min(min, arr[i % n]);
		}
		total += max - min;
		System.out.println(total);
	}
	
	static int lcm(int x, int y) {
	    return x / gcd(x, y) * y;
	}
	
	static int gcd(int x, int y) {
	    if (x % y == 0) {
	        return y;
	    } else {
	        return gcd(y, x % y);
	    }
	}
}

