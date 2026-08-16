import java.util.Scanner;
import java.util.StringTokenizer;

public class CF_859C {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int n = Integer.parseInt(s.nextLine());
		StringTokenizer st = new StringTokenizer(s.nextLine());
		
		int[] pies = new int[n];
		for(int i = 0; i < n; i++) {
			pies[i] = Integer.parseInt(st.nextToken());
		}
		int[] arr = new int[n];
		arr[n-1] = pies[n-1];
		int runsum = pies[n-1];
		
		for(int i = n-2; i >= 0; i--) {
			arr[i] = Math.max(arr[i+1], pies[i]+runsum-arr[i+1]);
			runsum += pies[i];
		}
		
		System.out.println((runsum-arr[0]) + " " + arr[0]);
		
	}
}
