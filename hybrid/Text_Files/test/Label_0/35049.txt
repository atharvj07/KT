import java.util.*;

public class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int h = sc.nextInt();
		int w = sc.nextInt();
		long total = 0;
		for (long i = 0; i < h; i++) {
		    for (long j = 0; j < w; j++) {
		        long x = sc.nextInt();
		        total += x * (i + 1) * (h - i) * (j + 1) * (w - j);
		    }
		}
	    System.out.println(total);
	}
}

