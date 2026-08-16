import java.util.Scanner;

public class Main {

	static Scanner sc = new Scanner(System.in);
	static int MOD = 100000;

	public static void main(String[] args) {
		while (true) {
			int N = sc.nextInt();
			if (N == 0) break;
			int M = sc.nextInt();
			int P = sc.nextInt() - 1;
			int Q = sc.nextInt() - 1;
			int R = sc.nextInt();
			Node EDGE = new Node(0, 0);
			Node top = new Node(1, N);
			top.prev = top.next = EDGE;
			EDGE.next = EDGE.prev = top;
			for (int i = 0; i < M; ++i) {
				int x = sc.nextInt();
				int y = sc.nextInt();
				Node sy = walk(EDGE.next, x);
				Node sz = walk(sy, y - x);
				exchange(EDGE.next, sy.prev, sz, EDGE.prev);
			}
			int count = 0;
			for (Node cur = EDGE.next; cur != EDGE; count += cur.len, cur = cur.next) {
				if (count > Q) break;
				if (count + cur.len <= P) continue;
				if (count < P) {
					cur.divide(P - count);
					continue;
				}
				if (count + cur.len > Q + 1) {
					cur.divide(Q - count + 1);
					break;
				}
			}
			count = 0;
			int ans = 0;
			for (Node cur = EDGE.next; cur != EDGE; count += cur.len, cur = cur.next) {
				if (count > Q) break;
				if (count + cur.len <= P) continue;
				if (cur.start > R) continue;
				if (cur.start + cur.len - 1 <= R) {
					ans += cur.len;
				} else {
					ans += R - cur.start + 1;
				}

			}
			System.out.println(ans);
		}
	}

	static Node walk(Node cur, int count) {
		int sum = 0;
		while (true) {
			sum += cur.len;
			if (sum == count) {
				return cur.next;
			}
			if (sum > count) {
				return cur.divide(cur.len - (sum - count));
			}
			cur = cur.next;
		}
	}

	static void exchange(Node xs, Node xe, Node zs, Node ze) {
		Node xp = xs.prev;
		Node xn = xe.next;
		Node zp = zs.prev;
		Node zn = ze.next;
		xp.next = zs;
		zs.prev = xp;
		xn.prev = ze;
		ze.next = xn;
		zp.next = xs;
		xs.prev = zp;
		zn.prev = xe;
		xe.next = zn;
	}

	static class Node {
		Node prev, next;
		int start, len;

		Node(int start, int len) {
			this.start = start;
			this.len = len;
		}

		Node divide(int ns) {
			Node nn = new Node(start + ns, len - ns);
			this.len = ns;
			this.next.prev = nn;
			nn.next = this.next;
			nn.prev = this;
			this.next = nn;
			return nn;
		}
	}
}