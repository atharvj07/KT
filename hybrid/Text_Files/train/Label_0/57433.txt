import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int x = sc.nextInt();
		int[] d = new int[n];
		int[] c = new int[n];
		for(int i=0;i<n;i++) {
			d[i] = sc.nextInt();
			c[i] = sc.nextInt();
		}
		Queue<Long> q = new PriorityQueue<Long>();
		q.offer(0L);
		int[] dist = new int[200001];
		Arrays.fill(dist, 1 << 29);
		while(!q.isEmpty()) {
			long cx = q.poll();
			int bx = (int) cx;
			int bc = (int) (cx >>> 32);
//			System.out.println(bx + "," + bc);
			if (bx == x) {
				System.out.println(bc);
				return;
			}
			for(int i=0;i<n;i++) {
				for(int dir=-1;dir<=1;dir+=2) {
					int nx = bx + d[i] * dir;
					int nc = bc + c[i];
					if (nx < 0 || nx > 200000) {
						continue;
					}
					if (dist[nx] > nc) {
						dist[nx] = nc;
						q.offer(((long) nc << 32) | nx);
					}
				}
			}
		}
		System.out.println(-1);
	}

}
