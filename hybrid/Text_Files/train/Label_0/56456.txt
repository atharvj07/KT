import java.util.Scanner;

public class Main {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int A = sc.nextInt();
		int B = sc.nextInt();
		int[] P = new int[N];

		for (int i = 0; i < N; i++) {
			P[i] = sc.nextInt();
		}

		int a = 0;
		int b = 0;
		int c = 0;
		for (int Pi : P) {
			if (Pi <= A) {
				a++;
			}
			if (A+1 <= Pi && Pi <= B) {
				b++;
			}
			if (B+1 <= Pi) {
				c++;
			}
		}

		int result = Math.min(a, b);
		result = Math.min(result, c);

		System.out.println(result);
	}
}