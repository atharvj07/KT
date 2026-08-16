import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		char[] S = sc.next().toCharArray();
		int N = S.length;
		long K = sc.nextLong();
		int[][] minApp = new int[N + 1][N + 1];
		for (int len = 2; len <= N; ++len) {
			for (int i = 0; i + len <= N; ++i) {
				minApp[i][i + len] = Math.min(minApp[i + 1][i + len] + 1, minApp[i][i + len - 1] + 1);
				if (S[i] == S[i + len - 1]) minApp[i][i + len] = Math.min(minApp[i][i + len], minApp[i + 1][i + len - 1]);
			}
		}
		long[][] count = new long[N + 1][N + 1];
		for (int i = 0; i < N; ++i) {
			count[i][i] = 1;
			count[i][i + 1] = 1;
		}
		count[N][N] = 1;
		for (int len = 2; len <= N; ++len) {
			for (int i = 0; i + len <= N; ++i) {
				if (S[i] == S[i + len - 1]) {
					count[i][i + len] = count[i + 1][i + len - 1];
				} else if (minApp[i + 1][i + len] > minApp[i][i + len - 1]) {
					count[i][i + len] = count[i][i + len - 1];
				} else if (minApp[i + 1][i + len] < minApp[i][i + len - 1]) {
					count[i][i + len] = count[i + 1][i + len];
				} else {
					count[i][i + len] = count[i + 1][i + len] + count[i][i + len - 1];
					if (count[i][i + len] > K) count[i][i + len] = K + 1;
				}
			}
		}
		StringBuilder ans = new StringBuilder();
		if (count[0][N] < K) {
			ans.append("NONE");
		} else {
			int left = 0;
			int right = N;
			while (true) {
				if (left == right) {
					ans.append(new StringBuilder(ans).reverse());
					break;
				}
				if (left + 1 == right) {
					StringBuilder rev = new StringBuilder(ans).reverse();
					ans.append(S[left]).append(rev);
					break;
				}
				if (S[left] == S[right - 1]) {
					ans.append(S[left]);
					left++;
					right--;
				} else if (minApp[left + 1][right] > minApp[left][right - 1]) {
					ans.append(S[right - 1]);
					right--;
				} else if (minApp[left + 1][right] < minApp[left][right - 1]) {
					ans.append(S[left]);
					left++;
				} else {
					if (S[left] < S[right - 1]) {
						if (count[left + 1][right] >= K) {
							ans.append(S[left]);
							left++;
						} else {
							K -= count[left + 1][right];
							ans.append(S[right - 1]);
							right--;
						}
					} else {
						if (count[left][right - 1] >= K) {
							ans.append(S[right - 1]);
							right--;
						} else {
							K -= count[left][right - 1];
							ans.append(S[left]);
							left++;
						}
					}
				}
			}
		}
		System.out.println(ans.toString());
	}
}