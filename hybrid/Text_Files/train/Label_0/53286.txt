import java.util.HashMap;
import java.util.Scanner;

public class Main {

	static Scanner sc = new Scanner(System.in);
	static double[] x, y, z;

	public static void main(String[] args) {
		while (true) {
			int N = sc.nextInt();
			if (N == 0) break;
			int M = sc.nextInt();
			HashMap<String, Node> map = new HashMap<String, Node>();
			Node cur = new Node(null);
			map.put(sc.next(), cur);
			int depth = 0;
			sc.nextLine();
			for (int i = 1; i < N; ++i) {
				String line = sc.nextLine();
				int d = 0;
				while (line.charAt(d) == ' ') {
					++d;
				}
				String name = line.substring(d);
				for (int j = 0; j <= depth - d; ++j) {
					cur = cur.parent;
				}
				Node node = new Node(cur);
				map.put(name, node);
				cur = node;
				depth = d;
			}
			for (int i = 0; i < M; ++i) {
				String X = sc.next();
				sc.next();
				sc.next();
				char query = sc.next().charAt(0);
				sc.next();
				String Y = sc.next();
				Y = Y.substring(0, Y.length() - 1);
				Node xn = map.get(X);
				Node yn = map.get(Y);
				boolean yes = false;
				if (query == 'c') {
					yes = xn.parent == yn;
				} else if (query == 'p') {
					yes = yn.parent == xn;
				} else if (query == 's') {
					yes = xn.parent == yn.parent;
				} else if (query == 'd') {
					Node node = xn;
					while (node != null) {
						if (node == yn) {
							yes = true;
							break;
						}
						node = node.parent;
					}
				} else if (query == 'a') {
					Node node = yn;
					while (node != null) {
						if (node == xn) {
							yes = true;
							break;
						}
						node = node.parent;
					}
				}
				System.out.println(yes ? "True" : "False");
			}
			System.out.println();
		}
	}

	static class Node {
		Node parent;

		Node(Node parent) {
			this.parent = parent;
		}
	}

}