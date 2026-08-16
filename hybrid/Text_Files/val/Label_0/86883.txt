import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] limit = new int[n];
		for (int i=0;i<n;i++) {
			limit[i] = sc.nextInt();
		}
		int[] apples = new int[n];
		int q = sc.nextInt();
		boolean breakFlag = false;
		for (int i=0;i<q;i++) {
			int t = sc.nextInt();
			int x = sc.nextInt() - 1;
			int d = sc.nextInt();
			if (t == 1) {
				apples[x] += d;
				if (apples[x] > limit[x]) {
					System.out.println(x + 1);
					breakFlag = true;
					break;
				}
			} else {
				apples[x] -= d;
				if (apples[x] < 0) {
					System.out.println(x + 1);
					breakFlag = true;
					break;
				}
			}
		}
		if (!breakFlag) System.out.println(0);
	}
}
