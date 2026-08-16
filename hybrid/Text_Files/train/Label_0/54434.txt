import java.util.Scanner;

public class Main {
	private static final long MAX = 1000000000000000000L;
	public static void main(final String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		long[] A = new long[N];
		int zero = -1;
		for(int i = 0; i < N; i++) {
			A[i] = sc.nextLong();
			if(A[i] == 0) zero = i;
		}
		sc.close();
		if(zero > -1) {
			prtln(0);
			return;
		}
		long answer = 1L;
		for(int i = 0; i < N; i++) {
			try {
				answer = Math.multiplyExact(answer, A[i]);
			} catch(ArithmeticException e) {
				prtln(-1);
				return;
			}
			if(answer > MAX) {
				prtln(-1);
				return;
			}
		}
		prtln(answer);
	}

	public static <T> void prtln(T t) { System.out.println(t); }
}