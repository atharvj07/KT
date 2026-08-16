import java.util.Arrays;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		while(true) {
			int l = sc.nextInt();
			if(l == 0) break;
			int n = sc.nextInt();
			int m = sc.nextInt();
			int []d = new int[n];
			int []k = new int[m];
			d[0] = 0;
			for(int i = 1; i <= n - 1; i++) {
				d[i] = sc.nextInt();
			}
			for(int i = 0; i < m; i++) {
				k[i] = sc.nextInt();
			}
			Arrays.sort(d);

			int sum = 0;
			for(int i = 0; i < m; i++) {
				int right = n;
				int left = -1;
				while(right - left > 1) {
					int mid = (right + left) / 2;
					if(d[mid] >= k[i]) {
						right = mid;
					}else {
						left = mid;
					}
				}
				//System.out.println(right);
				if(right == 0 || right == n) {
					int t1 = Math.abs(k[i] - d[0]);
					t1 = Math.min(t1, Math.abs(l - t1));
					sum += Math.min(t1, Math.abs(k[i] - d[n - 1]));
				}else {
					sum += Math.min(Math.abs(k[i] - d[right]), Math.abs(k[i] - d[right - 1]));
				}
			}
			sb.append(sum).append("\n");
		}
		sc.close();
		System.out.print(sb.toString());
	}
}
