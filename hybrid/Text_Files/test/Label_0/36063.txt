import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
	
	private class Node<T> {
		T value;
		Node<T> left;
		Node<T> right;
		public Node(T value) {
			this.value = value;
			left = right = null;
		}
		public String toString() {
			return value.toString();
		}
	}
	
	public static void main(String[] args) throws IOException {
		new Main().run();
	}
	
	private void run() throws IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(reader.readLine());
		int[] pre = new int[n];
		int[] in = new int[n];
		StringTokenizer st1 = new StringTokenizer(reader.readLine());
		StringTokenizer st2 = new StringTokenizer(reader.readLine());
		int rootId = 0;
		for (int i = 0; i < n; i++) {
			pre[i] = Integer.parseInt(st1.nextToken());
			in[i] = Integer.parseInt(st2.nextToken());
			if (i == 0) {
				rootId = pre[i];
			}
		}
		reader.close();
		
		Node<Integer> rootNode = new Node<Integer>(rootId);
		for (int i = 1; i < n; i++) {
			Node<Integer> current = new Node<Integer>(pre[i]);
			addNode(rootNode, current, in);
		}
		
		postOrder(rootNode);
	}

	private void postOrder(Node<Integer> rootNode) {
		StringBuilder sb = new StringBuilder();
		Stack<Node<Integer>> stack = new Stack<Node<Integer>>();
		Node<Integer> current = rootNode;
		Node<Integer> lastVisited = null;
		while (current != null || !stack.isEmpty()) {
			if (current != null) {
				stack.push(current);
				current = current.left;
			} else {
				Node<Integer> peekNode = stack.peek();
				if (peekNode.right != null && peekNode.right != lastVisited) {
					current = peekNode.right;
				} else {
					if (sb.length() == 0) {
						sb.append(peekNode);
					} else {
						sb.append(" " + peekNode);
					}
					lastVisited = stack.pop();
				}
			}			
		}
		System.out.println(sb.toString());
	}

	private void addNode(Node<Integer> rootNode, Node<Integer> newNode, int[] in) {
		int pos1 = findPos(in, newNode.value);
		Stack<Node<Integer>> stack = new Stack<Node<Integer>>();
		stack.push(rootNode);
		while (!stack.isEmpty()) {			
			Node<Integer> current = stack.pop();
			int pos2 = findPos(in, current.value);
			if (pos1 < pos2) {
				if (current.left == null) {
					current.left = newNode;
					return;
				} else {
					stack.push(current.left);
				}
			} else {
				if (current.right == null) {
					current.right = newNode;
					return;
				} else {
					stack.push(current.right);
				}
			}
		}
	}

	private int findPos(int[] in, int id) {
		for (int i = 0; i < in.length; i++) {
			if (in[i] == id) {
				return i;
			}
		}
		return -1;
	}
}

