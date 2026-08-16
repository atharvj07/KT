import java.util.*;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] h = new int[N];
		for (int i = 0; i < N; i++) {
			h[i] = sc.nextInt();
		}
		int count = 1, max = h[0];
		for (int i = 1; i < N; i++) {
			if (h[i] >= max) {
				max = h[i];
				count++;
			}
		}
		System.out.println(count);
	}
}
