import java.io.*;
import java.util.*;

public class Solution {
	
	static String solve(long a, long b, long n, long S) {
		if (a * n + b < S) {
			return "NO";
		} else {
			if (a * n > S) {
				if (S % n <= b) {
					return "YES";
				} else {
					return "NO";
				}
			} else {
				return "YES";
			}
		}
	}

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        int q = Integer.valueOf(scanner.nextLine());
        for (int i = 0; i < q; i++) {
        	String[] strs = scanner.nextLine().split(" ");
        	int a = Integer.valueOf(strs[0]);
        	int b = Integer.valueOf(strs[1]);
        	int n = Integer.valueOf(strs[2]);
        	int S = Integer.valueOf(strs[3]);
        	System.out.println(solve(a, b, n, S));
        }
        scanner.close();
    }
}
