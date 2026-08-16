import java.util.*;
import java.io.*;
import java.nio.charset.StandardCharsets;

public class Main {

	public static void main(String[] args) throws IOException {
		InputStreamReader reader = new InputStreamReader(System.in, StandardCharsets.UTF_8);
		BufferedReader in = new BufferedReader(reader);
		Main ins = new Main(in);
		ins.calc();
		ins.showResult();
	}

	int N, M;
	int[] A, B;
	Node[] nodes;

	static class Node {
		int id;
		int groupId;
		Set<Integer> conns;

		Node(int id) {
			this.id = id;
			this.groupId = -1;
			this.conns = new HashSet<>();
		}
	}

	Main(BufferedReader in) throws IOException {
		String[] tokens = in.readLine().split(" ");
		N = Integer.parseInt(tokens[0]);
		M = Integer.parseInt(tokens[1]);
		A = new int[M];
		B = new int[M];
		for (int i = 0; i < M; ++i) {
			tokens = in.readLine().split(" ");
			A[i] = Integer.parseInt(tokens[0]) - 1;
			B[i] = Integer.parseInt(tokens[1]) - 1;
		}
		nodes = new Node[N];
		for (int i = 0; i < N; ++i) {
			nodes[i] = new Node(i);
		}
		for(int i=0; i <M; ++i) {
			nodes[A[i]].conns.add(B[i]);
			nodes[B[i]].conns.add(A[i]);
		}
	}

	void mark(int id, int gId, int parent) {
		if (nodes[id].groupId >= 0) {
			return;
		}
		nodes[id].groupId = gId;
		for (Integer i : nodes[id].conns) {
			if (i != parent) {
				mark(i, gId, id);
			}
		}
	}

	void calc() {
		int gid = 0;
		for (int i = 0; i < N; ++i) {
			if (nodes[i].groupId < 0) {
				mark(i, gid, -1);
				++gid;
			}
		}
		int[] counts = new int[gid];
		for (int i = 0; i < N; ++i) {
			counts[nodes[i].groupId]++;
		}
		int max = -1;
		for (int i = 0; i < counts.length; ++i) {
			max = Math.max(max, counts[i]);
		}
		System.out.println(max);
	}

	void showResult() {
	}
}