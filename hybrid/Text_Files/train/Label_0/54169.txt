
import java.util.Scanner;

public class PolycarpsPockets {
	public static void main(String[] args) {
		int[] arr= new int[101];
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int x,mx=0;
		for(int i=0;i<n;i++) {
			x = sc.nextInt();
			arr[x]++;
			mx = Math.max(mx, arr[x]);
		}
		System.out.println(mx);
	}
}
