import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		int n = sc.nextInt();
		int[] a = new int[n];
		for (int i = 0; i < n; i++) {
			a[i] = sc.nextInt();
		}
		if (n % 2 == 0) {
			for (int i = n - 1; i >= 0; i = i - 2) {
				sb.append(a[i] + " ");
			}
			for (int i = 0; i < n; i = i + 2) {
				sb.append(a[i] + " ");
			}
		}else {
			for (int i = n - 1; i >= 0; i = i - 2) {
				sb.append(a[i] + " ");
			}
			for (int i = 1; i < n; i = i + 2) {
				sb.append(a[i] + " ");
			}
		}
		sb.deleteCharAt(sb.length()-1);
		System.out.println(sb);

	}
}
