import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		boolean[] painted = new boolean[n];
		for(int i=0;i<m;i++) {
			int a = sc.nextInt();
			int l = sc.nextInt();
			for(int j=0;j<l;j++) {
				painted[(a+j)%n] = true;
			}
		}
		int start = 0;
		for(int i=0;i<n;i++) {
			if (!painted[i]) {
				start = i;
				break;
			}
		}
//		System.out.println(Arrays.toString(painted));
		boolean[] p2 = new boolean[n+1];
		for(int i=0;i<n;i++) {
			p2[i] = painted[(start+i)%n];
		}
		int[] count = new int[n+1];
		int len = 0;
		for(int i=0;i<=n;i++) {
			if (p2[i]) {
				len++;
			}else{
				count[len]++;
				len = 0;
			}
		}
		for(int i=n;i>=1;i--) {
			if (count[i] >= 1) {
				System.out.println(i + " " + count[i]);
			}
		}
	}
}
