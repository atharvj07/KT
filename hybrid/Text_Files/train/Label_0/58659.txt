import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
	public static class Edge {
		public int src, dst, length;

		public Edge(int src, int dst, int length) {
			this.src = src;
			this.dst = dst;
			this.length = length;
		}
	}

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int L = Integer.parseInt(in.nextLine());
		int nodeNum = getNodeNum(L);
		// System.out.println("nodeNum: " + nodeNum);
		List<Edge> edges = genEdges(nodeNum, L);
		System.out.println(nodeNum + " " + edges.size());
		for (Edge edge : edges) {
			System.out.println(edge.src + " " + edge.dst + " " + edge.length);
		}
		in.close();
	}

	public static int getNodeNum(int L) {
		int result = 0;
		for (int i = 1; i <= 20; ++i) {
			if (Math.pow(2.0, (double) i) > L) {
				result = i;
				break;
			}
		}
		return result;
	}

	public static List<Edge> genEdges(int nodeNum, int L) {
		List<Edge> result = new ArrayList<>();
		for (int i = 1; i + 1 <= nodeNum; ++i) {
			int length = (int) Math.pow(2.0, i - 1);
			result.add(new Edge(i, i + 1, length));
			result.add(new Edge(i, i + 1, 0));
		}
		int l = L;
		for (int i = nodeNum - 1; i >= 1; --i) {
			if (l - Math.pow(2, i - 1) >= Math.pow(2.0, nodeNum - 1)) {
				// System.out.println(i + ", ");
				result.add(new Edge(i, nodeNum, (int) (l - Math.pow(2, i - 1))));
				l -= Math.pow(2.0, i - 1);
			}
		}
		return result;
	}
}