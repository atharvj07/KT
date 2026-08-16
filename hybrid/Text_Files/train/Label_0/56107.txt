import java.util.*;
import static java.lang.System.*;
import static java.lang.Math.*;

public class Main {

	Scanner sc = new Scanner(in);
	
	void reverse(long[] a) {
		int i = 0, j = a.length-1;
		long temp;
		while (i < j) {
			temp = a[i];
			a[i] = a[j];
			a[j] = temp;
			i++; j--;
		}
	}
	
	void run() {
		int n = sc.nextInt();
		long[] h = new long[n];
		for (int i = 0; i < n; i++)
			h[i] = sc.nextLong();
		Arrays.sort(h);
		reverse(h);
		
		int count = -1;
		long ans = 0;
		for (int i = 0; i < n; i++) {
			if (i % 4 == 0) count++;
			ans += h[i] - min(h[i], count);
		}
		
		out.println(ans+1);
	}
	
	public static void main(String[] args) {
		new Main().run();
	}

}