import java.io.*;
import java.util.*;
import java.math.*;

public class C {
	public static void main(String[] args) throws IOException {

		/**/
		Scanner sc = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
		/*/
		Scanner sc = new Scanner(new BufferedReader(new InputStreamReader(new FileInputStream("src/c.in"))));
		/**/
		
		int n = sc.nextInt();
		int m = sc.nextInt();
		int[] starts = new int[m+1];
		int[] ends = new int[m+1];
		for (int i = 0; i < n; i++) {
			starts[sc.nextInt()]++;
			ends[sc.nextInt()]++;
		}
		int[] counts = new int[m+1];
		for (int i = 1; i <= m; i++) {
			counts[i] = counts[i-1]+starts[i]-ends[i-1];
		}
		
		int[] lisp = new int[m+1];
		int[] lism = new int[m+1];
		int[] sublens = new int[m+1];
		
		int l = 0;
		for (int i = 1; i <= m; i++) {
			int lo = 1;
			int hi = l;
			while (lo <= hi) {
				int mid = (lo+hi+1)/2;
				if (counts[lism[mid]]<=counts[i]) {
					lo = mid+1;
				} else {
					hi = mid-1;
				}
			}
			int newl = lo;
			lisp[i] = lism[newl-1];
			lism[newl] = i;
			
			if (newl > l)
				l = newl;
			sublens[i] = newl;
		}
		
		lisp = new int[m+1];
		lism = new int[m+1];
		int[] sublens2 = new int[m+1];
		int[] cr = new int[m+1];
		for (int i = 0; i <= m; i++) {
			cr[m-i] = counts[i];
		}
		
		l = 0;
		for (int i = 0; i <= m; i++) {
			int lo = 1;
			int hi = l;
			while (lo <= hi) {
				int mid = (lo+hi+1)/2;
				if (cr[lism[mid]]<=cr[i]) {
					lo = mid+1;
				} else {
					hi = mid-1;
				}
			}
			int newl = lo;
			lisp[i] = lism[newl-1];
			lism[newl] = i;
			
			if (newl > l)
				l = newl;
			sublens2[i] = newl;
		}
		
		int ans = 0;
		for (int i = 1; i <= m; i++) {
			ans = Math.max(ans, sublens[i-1]+sublens2[m-i]);
		}
		System.out.println(ans);
	}
}