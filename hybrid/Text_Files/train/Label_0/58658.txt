import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		int i, j = 0, n;
		try (Scanner sc = new Scanner(System.in)) {
			n = sc.nextInt();
			int[] a = new int[n];
			int[] b = new int[n];
			for(i = 0; i < n; i++) {
				a[i] = sc.nextInt();
			}
			for(i = 0; i < n - 1; i++) {
				if(a[i] == a[i + 1]) {
					continue;
				}
				b[j] = a[i];
				j++;
			}
			b[j] = a[n - 1];
			for(i = 0; i < j; i++){
				System.out.print(b[i] + " ");
			}
			System.out.println(b[j]);
		}
	}
}

