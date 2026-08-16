import java.io.*;
import java.util.*;

public class B {
	public static void main(String[]args) throws IOException {
		BufferedReader x = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(x.readLine());
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		int[]arr = new int[n];
		st = new StringTokenizer(x.readLine());
		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		int cur = 0;
		int ans = 0;
		for (int i = 1; i < n; i++) {
			int temp = k - (arr[i] + arr[i-1]);
			temp = Math.max(temp, 0);
			arr[i] += temp;
			ans += temp;
		}
		System.out.println(ans);
		for (int i = 0; i < n; i++) {
			System.out.print(arr[i]+" ");
		}
		System.out.println();
	}
}