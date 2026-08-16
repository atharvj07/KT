import java.util.*;
import java.io.*;

class Main {

	static Node[] node = null;

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());
		node = new Node[n];

		for (int i=0; i<n; i++) {
			node[i] = new Node();
		}

		for (int i=0; i<n; i++) {
			String line = br.readLine();
			String[] str = line.split(" ");
			int id = Integer.parseInt(str[0]);
			int left = Integer.parseInt(str[1]);
			int right = Integer.parseInt(str[2]);
			if (left != -1 && right != -1) {
				node[id].degree = 2;
				node[id].left = node[right].sibling = left;
				node[id].right = node[left].sibling = right;
				node[left].parent = node[right].parent = id;
				node[id].type = "internal node";
			}else if (left != -1) {
				node[id].degree = 1;
				node[id].left = left;
				node[id].right = node[left].sibling = -1;
				node[left].parent = id;
				node[id].type = "internal node";
			}else if (right != -1) {
				node[id].degree = 1;
				node[id].right = right;
				node[id].left = node[right].sibling = -1;
				node[right].parent = id;
				node[id].type = "internal node";
			}else {
				node[id].degree = 0;
				node[id].left = node[id].right = -1;
				node[id].type = "leaf";
			}
		}

		for (int i=0; i<n; i++) {
			if (node[i].parent == -1) {
				setDH(node[i],0);
				node[i].type = "root";
				node[i].sibling = -1;
				break;
			}
		}

		for (int i=0; i<n; i++) {
			StringBuilder sb = new StringBuilder();
			sb.append("node ").append(i).append(": parent = ").append(node[i].parent).append(", sibling = ");
			sb.append(node[i].sibling).append(", degree = ").append(node[i].degree).append(", depth = ");
			sb.append(node[i].depth).append(", height = ").append(node[i].height).append(", ").append(node[i].type);
			System.out.println(sb);
		}

		br.close();
	}

	static int setDH(Node nd,int depth){
		nd.depth = depth;
		if (nd.left != -1 && nd.right != -1) {
			int lh = setDH(node[nd.left],depth+1);
			int rh = setDH(node[nd.right],depth+1);
			nd.height = lh > rh ? lh : rh;
		}else if (nd.left != -1) {
			nd.height = setDH(node[nd.left],depth+1);
		}else if (nd.right != -1) {
			nd.height = setDH(node[nd.right],depth+1);
		}else {
			nd.height = 0;
		}
		return nd.height+1;
	}

	static class Node{
		int parent = -1;
		int sibling;
		int degree;
		int depth;
		int height;
		String type;
		int right;
		int left;
	}
}