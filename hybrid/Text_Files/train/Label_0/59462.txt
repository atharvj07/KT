import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) {
		new BinSearchTree1().run();
	}
}

class BinSearchTree1 {

	Node root;

	public void run() {

		root = null;

		try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {

			int m = Integer.parseInt(br.readLine());
			for (int i = 0; i < m; i++) {

				String line = br.readLine();

				if(line.charAt(0) == 'i') {
					int val = Integer.parseInt(line.substring(7));
					insert(val);
				} else {
					print();
				}

			}

		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	private void insert(int val) {

		Node y = null;
		Node x = root;

		Node z = new Node();
		z.key = val;
		z.left = null;
		z.right = null;

		while (x != null) {
			y = x;
			if (val < x.key) {
				x = x.left;
			} else {
				x = x.right;
			}
		}
		z.parent = y;

		if (y == null) {
			root = z;
		} else {
			if (val < y.key) {
				y.left = z;
			} else {
				y.right = z;
			}
		}
	}

	private void print() {

		pByInOrder(root);
		System.out.println();
		pByPreOrder(root);
		System.out.println();

	}

	private void pByInOrder(Node node) {

		if(node == null) return;

		pByInOrder(node.left);
		System.out.print(" " + node.key);
		pByInOrder(node.right);

	}

	private void pByPreOrder(Node node) {

		if(node == null) return;

		System.out.print(" " + node.key);
		pByPreOrder(node.left);
		pByPreOrder(node.right);

	}

}

class Node {

	int key;
	Node left, right, parent;

}