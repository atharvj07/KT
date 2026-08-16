import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class C {
	static long nCk(long n, long k) {
		if (k > n)
			return 0;
		if (k * 2 > n)
			k = n - k;
		if (k == 0)
			return 1;

		long result = n;
		for (int i = 2; i <= k; ++i) {
			result *= (n - i + 1);
			result /= i;
		}
		return result;
	}

	static int numOfBits;
	static long sum, x;
	static long dp[][][][];

	static long count(int currBit, int carry, int bit, int bit2) {
		if (currBit > numOfBits)
			return carry == 0 && bit == 1 && bit2 == 1 ? 1 : 0;
		if (dp[carry][bit][bit2][currBit] != -1)
			return dp[carry][bit][bit2][currBit];
		long ans = 0;
		if (((1L << currBit) & x) == 0) {
			// xor must be 0
			if (carry == 1) {
				// carry with 0+0 = 1 c =0
				// carry with 1+1 = 1 c =1
				if (((1L << currBit) & sum) > 0) {
					ans += count(currBit + 1, 0, bit, bit2);
					ans += count(currBit + 1, 1, 1, 1);
				}
			} else {
				// no carry with 0+0 = 0 c =0
				// no carry with 1+1 = 0 c =1
				if (((1L << currBit) & sum) == 0) {
					ans += count(currBit + 1, 0, bit, bit2);
					ans += count(currBit + 1, 1, 1, 1);
				}
			}
		} else {
			// xor must be 1
			if (carry == 1) {
				// carry 1+0 = 1 c=1
				// carry 0+1 = 1 c=1
				if (((1L << currBit) & sum) == 0) {
					ans += count(currBit + 1, 1, 1, bit2);
					ans += count(currBit + 1, 1, bit, 1);
				}
			} else {
				// no carry 1+0 = 1 c=0
				// no carry 0+1 = 1 c=0
				if (((1L << currBit) & sum) > 0) {
					ans += count(currBit + 1, 0, 1, bit2);
					ans += count(currBit + 1, 0, bit, 1);
				}
			}
		}
		return dp[carry][bit][bit2][currBit] = ans;
	}

	public static void main(String[] args) throws Exception {

		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String l[] = bf.readLine().split(" ");
		sum = Long.parseLong(l[0]);
		x = Long.parseLong(l[1]);
		numOfBits = 0;
		int c1 = 0;
		long xx = x;
		while (xx > 0) {
			xx /= 2;
			c1++;
		}
		int c2 = 0;
		xx = sum;
		while (xx > 0) {
			xx /= 2;
			c2++;
		}
		numOfBits = Math.max(c1, c2);
		dp = new long[2][2][2][numOfBits + 1];
		for (int i = 0; i < 2; i++) {
			for (int j = 0; j < 2; j++) {
				for (int j2 = 0; j2 < 2; j2++) {
					Arrays.fill(dp[i][j][j2], -1);
				}
			}
		}
		System.out.println(count(0, 0, 0, 0));
	}
}