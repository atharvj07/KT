import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

/**
 * Rooted Tree for Misawa-san
 */
public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line;
		String[] words;

		Node tree1, tree2, tree;
		tree1 = Node.parseNode(br.readLine());
		tree2 = Node.parseNode(br.readLine());
		tree = Node.merge(tree1, tree2);

		System.out.println(tree.toString());

	} //end main
}

class Node {
	Node parent, left, right;
	int value = -1;

	public static Node parseNode(String str) {

		if (str.isEmpty()) {
			return null;
		}

		Node node = new Node();

		Deque<Character> stack = new ArrayDeque<>();

		int i, j, v = 0;
		for (i = 0; i < str.length(); i++) {
			char c = str.charAt(i);
			switch (c) {
				case '(':
					stack.push(c);
					for (j = i + 1; j < str.length(); j++) {
						char _c = str.charAt(j);
						if (_c == '(') {
							stack.push(_c);
						}
						if (_c == ')') {
							stack.pop();
						}
						if (stack.isEmpty()) {
							if (node.value < 0) {
								node.left = Node.parseNode(str.substring(i + 1, j));
							} else {
								node.right = Node.parseNode(str.substring(i + 1, j));
							}
							i = j;
							break;
						}
					}
					break;
				case ')':
					break;
				case '[':
					break;
				case ']':
					node.value = v;
					break;
				default:
					v *= 10;
					v += c - '0';
			}
		}

		return node;
	}

	public static Node merge(Node t1, Node t2) {

		if (t1 == null || t2 == null) {
			return null;
		}

		Node node = new Node();

		node.value = t1.value + t2.value;
		node.left = Node.merge(t1.left, t2.left);
		node.right = Node.merge(t1.right, t2.right);

		return node;
	}

	public String toString() {

		String ls = "";
		String rs = "";

		if (left != null) ls = left.toString();
		if (right != null) rs = right.toString();

		return String.format("(%s)[%d](%s)", ls, value, rs);
	}
}