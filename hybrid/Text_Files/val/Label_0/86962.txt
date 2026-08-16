import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.next();
		int n = s.length();
		final long MOD = 1000000007L;
		int[] sumA = new int[n + 1];
		int[] sumC = new int[n + 1];
		int[] sumX = new int[n + 1];
		for(int i = 0; i < n; i++) {
			if(s.charAt(i) == 'A') sumA[i + 1] = sumA[i] + 1;
			else sumA[i + 1] = sumA[i];
			if(s.charAt(i) == 'C') sumC[i + 1] = sumC[i] + 1;
			else sumC[i + 1] = sumC[i];
			if(s.charAt(i) == '?') sumX[i + 1] = sumX[i] + 1;
			else sumX[i + 1] = sumX[i];
		}
		long[] three = new long[n + 1];
		three[0] = 1;
		for(int i = 0; i < n; i++) three[i + 1] = (three[i] * 3) % MOD;
		long ans = 0;
		for(int i = 1; i < n; i++) {
			if(s.charAt(i) == 'B' || s.charAt(i) == '?') {
				int tailC = sumC[n] - sumC[i + 1];
				int tailX = sumX[n] - sumX[i + 1];
				long head = (sumA[i] * three[sumX[i]] + sumX[i] * (sumX[i] == 0 ? 1 : three[sumX[i] - 1])) % MOD;
				long tail = (tailC * three[tailX] + tailX * (tailX == 0 ? 1 : three[tailX - 1])) % MOD;
				ans = (ans + (head * tail) % MOD) % MOD;
			}
		}
		System.out.println(ans);
	}
}
