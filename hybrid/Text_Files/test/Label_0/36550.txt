import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long H = sc.nextLong();
		long W = sc.nextLong();
		sc.close();
		if(H % 3 == 0 || W % 3 == 0) {
			System.out.println(0);
			System.exit(0);
		}
		long min = H * W;
		for(int i = 1; i < H; i++) {
			long[]S = new long[3];
			S[0] = i * W;
			S[1] = (H - i) * (W / 2);
			S[2] = (H - i)  * (W - W / 2);
			Arrays.sort(S);
			if(S[0] == 0) continue;
			min = Math.min(min, S[2] - S[0]);
		}


		for(int i = 1; i < H; i++) {
			long[]S = new long[3];
			S[0] = i * W;
			long r = H - i;
			S[1] = W * (r / 2);
			S[2] = W * (r - r / 2);
			Arrays.sort(S);
			if(S[0] == 0) continue;
			min = Math.min(min, S[2] - S[0]);
		}
		long t = H;
		H = W;
		W = t;
		for(int i = 1; i < H; i++) {
			long[]S = new long[3];
			S[0] = i * W;
			S[1] = (H - i) * (W / 2);
			S[2] = (H - i)  * (W - W / 2);
			Arrays.sort(S);
			if(S[0] == 0) continue;
			min = Math.min(min, S[2] - S[0]);
		}


		for(int i = 1; i < H; i++) {
			long[]S = new long[3];
			S[0] = i * W;
			long r = H - i;
			S[1] = W * (r / 2);
			S[2] = W * (r - r / 2);
			Arrays.sort(S);
			if(S[0] == 0) continue;
			min = Math.min(min, S[2] - S[0]);
		}

		System.out.println(min);
	}
}