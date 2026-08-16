import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int N = in.nextInt();
		String[] S = new String[N];
		int[] t = new int[N];
		for (int i = 0; i < N; i++) {
			S[i] = in.next();
			t[i] = in.nextInt();
		}
		String X = in.next();
		int index = -1;
		for (int i = 0; i < N; i++) {
			if (X.equals(S[i])) {
				index = i;
				break;
			}
		}
		index++;
		int ans = 0;
		for (int i = index; i < N; i++) {
			ans += t[i];
		}
		System.out.println(ans);
		in.close();
	}
}