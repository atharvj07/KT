
//package codeTrainingLeetcode;

import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

public class C466D2E {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int n = scanner.nextInt();
		int c = scanner.nextInt();
		int[] a = new int[n];
		long[] dp = new long[n + 1];
		PriorityQueue<int[]> pQueue = new PriorityQueue<>(new Comparator<int[]>() {
			@Override
			public int compare(int[] a1, int[] a2) {
				return a1[0] - a2[0];
			}
		});
		for (int i = 0; i < n; i++)
			a[i] = scanner.nextInt();
		long cRangeSum = 0;
		for (int i = 0; i < n; i++) {
			if (i - c >= 0) {
				cRangeSum += (long) a[i] - a[i - c];
			} else {
				cRangeSum += (long) a[i];
			}
			pQueue.add(new int[] { a[i], i });
			while (pQueue.peek()[1] <= i - c)
				pQueue.poll();
			if (i == c - 1) {
				dp[i] = cRangeSum - (long) pQueue.peek()[0];
			} else if (i > c - 1) {
				dp[i] = Math.min(dp[i - 1] + (long) a[i], dp[i - c] + (long) cRangeSum - (long) pQueue.peek()[0]);
			} else {
				dp[i] = cRangeSum;
			}
		}
		// System.out.println(Arrays.toString(dp));
		System.out.println(dp[n - 1]);
	}
}
