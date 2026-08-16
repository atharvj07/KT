import java.util.Scanner;


public class C_132A {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int a[] = new int [n];
		for (int i = 0; i < a.length; i++) {
			a[i] = sc.nextInt();
		}
		int m = sc.nextInt();
		int b[] = new int [m];
		for (int i = 0; i < b.length; i++) {
			b[i] = sc.nextInt();
		}
		int max = -1;
		for (int i = 0; i < b.length; i++) {
			for (int j = 0; j < a.length; j++) {
				if(b[i] % a[j] == 0) max = Math.max(max, b[i]/a[j]);
			}
		}
		int ans = 0;
		for (int i = 0; i < b.length; i++) {
			for (int j = 0; j < a.length; j++) {
				if((double) b[i] / a[j] ==  max)  ans++;
			}
		}
		System.out.println(ans);
	}
}
