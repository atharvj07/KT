import java.util.*;

public class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int k = sc.nextInt();
		long idx = 0;
		for (int i = 1; i < n; i++) {
		    idx += idx / (k - 1) + 1;
		}
		System.out.println(idx);
	}
}

