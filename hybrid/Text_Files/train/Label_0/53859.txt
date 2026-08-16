import java.util.*;

public class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		long max = (1L << n);
		int k = sc.nextInt();
		long base = 0;
		for (int i = 0; i < k; i++) {
		    base += (1L << sc.nextInt());
		}
		StringBuilder sb = new StringBuilder();
		for (long i = 0; i < max; i++) {
		    if ((base & i) != base) {
		        continue;
		    }
		    sb.append(i).append(":");
		    long x = i;
		    for (int j = 0; j <= 18 && x > 0; j++) {
		        if (x % 2 == 1) {
		            sb.append(" ").append(j);
		        }
		        x >>= 1;
		    }
		    sb.append("\n");
		}
		System.out.print(sb);
	}
}

