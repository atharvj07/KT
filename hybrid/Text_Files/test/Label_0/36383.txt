import java.util.*;

// ARC 86-D
// https://beta.atcoder.jp/contests/arc086/tasks/arc086_b

public class Main {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		int N = in.nextInt();
		int[] cost = new int[N];
		int[] start = new int[N];
		int[] freq = new int[N];
		
		for (int i = 0; i < N - 1; i++) {
			cost[i] = in.nextInt();
			start[i] = in.nextInt();
			freq[i] = in.nextInt();
		}
		
		long[] answer = new long[N];
		for (int i = 0; i < N - 1; i++) {
			long sec = start[i] + cost[i];
			for (int j = i + 1; j < N - 1; j++) {
				if (sec <= start[j]) {
					sec = start[j] + cost[j];
				} else {
					int n = 1;
					while (start[j] + n * freq[j] < sec) {
						n++;
					}
					sec = start[j] + n * freq[j];
					sec += cost[j];
				}
			}
			answer[i] = sec;
		}
		
//		int[] distance = new int[N];
//		for (int i = N - 2; i >= 0; i--) {
//			if (i == N - 2) {
//				distance[i] = cost[i];
//			} else {
//				int sec = cost[i];
//				// Check how long it has to wait at the next station
//				while (sec % freq[i + 1] != 0) {
//					sec++;
//				}
//				distance[i] = sec + distance[i + 1];
//			}
//		}
//		
//		System.out.println("distance");
//		for (int i = 0; i < N; i++) {
//			System.out.printf("%d => %d: %d\n", i + 1, N, distance[i]);
//		}
//		
////		int[] answer = new int[N];
//		
//		for (int i = N - 2; i >= 0; i--) {
//			if (i == N - 2) {
//				answer[i] = cost[i] + start[i];
//			} else {
//				if (start[i] + cost[i] <= start[i + 1]) {
//					answer[i] = answer[i + 1];
//				} else {
//					int a = start[i] + cost[i];
//					int n = 1;
//					while (start[i + 1] + n * freq[i + 1] < a) {
//						n++;
//					}
//					answer[i] = start[i + 1] + n * freq[i + 1] + distance[i + 1];
//				}
//			}
//		}
		
		for (int i = 0; i < N; i++) {
			System.out.println(answer[i]);
		}
	}
}
