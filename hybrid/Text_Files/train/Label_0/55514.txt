import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		int N = sc.nextInt();
		int R = sc.nextInt();
		R = Math.min(R, N - R);
		int[] P = new int[N];
		for (int i = 0; i < N; i++) {
			P[i] = Integer.parseInt(sc.next()) - 1;
		}
		int one = 0;
		ArrayList<Integer> len = new ArrayList<>();
		boolean[] used = new boolean[N];
		for (int i = 0; i < N; i++) {
			if (used[i]) continue;
			int cur = i;
			int l = 1;
			used[cur] = true;
			while (P[cur] != i) {
				cur = P[cur];
				++l;
				used[cur] = true;
			}
			if (l == 1) {
				one++;
			} else {
				len.add(l);
			}
		}
		Bits bs = new Bits(R + 1);
		bs.bits[0] = 1L;
		for (int i = 0; i < len.size(); i++) {
			bs.shiftLOr(len.get(i));
		}
		boolean ans = false;
		for (int i = 0; i <= one && i <= R; i++) {
			if (bs.get(R - i)) {
				ans = true;
				break;
			}
		}
		System.out.println(ans ? "Yes" : "No");

	}

	static class Bits {
		long[] bits;

		Bits(int size) {
			bits = new long[(size + 63) / 64];
		}

		void shiftLOr(int shift) {
			int m1 = shift >> 6;
			int m2 = shift & 63;
			if (m2 == 0) {
				for (int i = bits.length - 1 - m1; i >= 0; i--) {
					bits[i + m1] |= bits[i];
				}
			} else {
				for (int i = bits.length - 1 - m1; i >= 0; i--) {
					int p1 = i + m1 + 1;
					int p2 = i + m1;
					long v1 = bits[i] >>> (64 - m2);
					long v2 = bits[i] << m2;
					if (p1 < bits.length) {
						bits[p1] |= v1;
					}
					bits[p2] |= v2;
				}
			}
		}

		boolean get(int pos) {
			return ((bits[pos >> 6] >>> (pos & 63)) & 1) != 0;
		}

		void set(int pos) {
			bits[pos >> 6] |= (1L << (pos & 63));
		}
	}

}

