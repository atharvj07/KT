import java.util.*;
import java.io.*;
import java.math.BigInteger;
import com.sun.jmx.remote.internal.ArrayQueue;

public class Main implements Runnable {
	// haha, you won't challenge my randomization with fixed seed!!!
	// static Random rm = new Random(31);
	static Random rm = new Random();

	static class Tree {
		int key;
		int prior;
		int count;
		long sum;
		Tree left;
		Tree right;

		public Tree(int key, int prior) {
			this.key = key;
			this.prior = prior;
			update();
		}

		public Tree() {
		}

		public void update() {
			count = (left == null ? 0 : left.count) + 1 + (right == null ? 0 : right.count);
			sum = (long) (left == null ? 0 : left.sum) + key + (long) (right == null ? 0 : right.sum);
		}

		public static Tree add(Tree head, Tree node) {
			if (head == null) {
				return node;
			} else if (head.prior >= node.prior) {
				if (node.key < head.key) {
					head.left = add(head.left, node);
				} else {
					head.right = add(head.right, node);
				}
				head.update();
				return head;
			} else {
				split(head, node, node.key);
				node.update();
				return node;
			}
		}

		public static void split(Tree head, Tree res, int key) {
			if (head == null) {
				res.left = res.right = null;
			} else if (key <= head.key) {
				split(head.left, res, key);
				head.left = res.right;
				res.right = head;
				head.update();
			} else {
				split(head.right, res, key);
				head.right = res.left;
				res.left = head;
				head.update();
			}
		}

		public static Tree remove(Tree head, int key) {
			if (head != null) {
				if (key < head.key) {
					head.left = remove(head.left, key);
					head.update();
				} else if (key > head.key) {
					head.right = remove(head.right, key);
					head.update();
				} else {
					head = merge(head.left, head.right);
				}
			}
			return head;
		}

		public static Tree merge(Tree left, Tree right) {
			if (left == null) {
				return right;
			} else if (right == null) {
				return left;
			} else if (left.prior >= right.prior) {
				left.right = merge(left.right, right);
				left.update();
				return left;
			} else {
				right.left = merge(left, right.left);
				right.update();
				return right;
			}
		}

		public static boolean contains(Tree head, int key) {
			if (head == null) {
				return false;
			} else {
				if (key < head.key) {
					return contains(head.left, key);
				} else if (key > head.key) {
					return contains(head.right, key);
				} else {
					return true;
				}
			}
		}

		public String toString() {
			List<Integer> res = new ArrayList<Integer>();
			toString(this, res);
			return res.toString();
		}

		private void toString(Tree tree, List<Integer> res) {
			if (tree != null) {
				toString(tree.left, res);
				res.add(tree.key);
				toString(tree.right, res);
			}
		}
	}

	private void solution() throws IOException {
		Tree[] tree = new Tree[5];
		int q = in.nextInt();
		for (int it = 0; it < q; ++it) {
			String command = in.next();
			if (command.equals("sum")) {
				out.println(getSum(tree[2]));
			} else if (command.equals("add")) {
				int key = in.nextInt();
				int index = 0;
				Tree[] parts = new Tree[5];
				for (int i = 0; i < parts.length; ++i) {
					parts[i] = new Tree();
					Tree.split(tree[i], parts[i], key);
					index += getCount(parts[i].left);
				}
				index %= 5;
				parts[index].left = Tree.merge(parts[index].left, new Tree(key, rm.nextInt()));
				for (int i = 0; i < tree.length; ++i) {
					tree[i] = Tree.merge(parts[i].left, parts[(i - 1 + 5) % 5].right);
				}
			} else if (command.equals("del")) {
				int key = in.nextInt();
				Tree[] parts = new Tree[5];
				for (int i = 0; i < parts.length; ++i) {
					parts[i] = new Tree();
					Tree.split(tree[i], parts[i], key);
				}
				for (int index = 0; index < parts.length; ++index) {
					if (Tree.contains(parts[index].right, key)) {
						parts[index].right = Tree.remove(parts[index].right, key);
						for (int i = 0; i < tree.length; ++i) {
							tree[i] = Tree.merge(parts[i].left, parts[(i + 1) % 5].right);
						}
						break;
					}
				}
			} else {
				throw new RuntimeException("What the hell is that?");
			}
		}
	}

	private int getCount(Tree tree) {
		if (tree == null) {
			return 0;
		} else {
			return tree.count;
		}
	}

	private long getSum(Tree tree) {
		if (tree == null) {
			return 0;
		} else {
			return tree.sum;
		}
	}

	private void debug(Object... objects) {
		System.out.println(Arrays.deepToString(objects));
	}

	public void run() {
		try {
			// try {
			// String fileName = "";
			// in = new Scanner(new FileReader(fileName + ".in"));
			// out = new PrintWriter(fileName + ".out");
			// } catch (Exception e) {
			// }
			solution();
			in.reader.close();
			out.close();
		} catch (Throwable e) {
			e.printStackTrace();
			System.exit(1);
		}
	}

	private static class Scanner {
		private BufferedReader reader;
		private StringTokenizer tokenizer;

		public Scanner(Reader reader) {
			this.reader = new BufferedReader(reader);
			this.tokenizer = new StringTokenizer("");
		}

		public boolean hasNext() throws IOException {
			while (!tokenizer.hasMoreTokens()) {
				String line = reader.readLine();
				if (line == null) {
					return false;
				}
				tokenizer = new StringTokenizer(line);
			}
			return true;
		}

		public String next() throws IOException {
			hasNext();
			return tokenizer.nextToken();
		}

		public int nextInt() throws IOException {
			return Integer.parseInt(next());
		}

		public double nextDouble() throws IOException {
			return Double.parseDouble(next());
		}

		public long nextLong() throws IOException {
			return Long.parseLong(next());
		}

		public String nextLine() throws IOException {
			tokenizer = new StringTokenizer("");
			return reader.readLine();
		}

		public int[] nextInts(int n) throws IOException {
			int[] res = new int[n];
			for (int i = 0; i < n; ++i) {
				res[i] = nextInt();
			}
			return res;
		}

		public long[] nextLongs(int n) throws IOException {
			long[] res = new long[n];
			for (int i = 0; i < n; ++i) {
				res[i] = nextLong();
			}
			return res;
		}

		public double[] nextDoubles(int n) throws IOException {
			double[] res = new double[n];
			for (int i = 0; i < n; ++i) {
				res[i] = nextDouble();
			}
			return res;
		}

		public String[] nextStrings(int n) throws IOException {
			String[] res = new String[n];
			for (int i = 0; i < n; ++i) {
				res[i] = next();
			}
			return res;
		}
	}

	public static void main(String[] args) throws Exception {
		new Thread(null, new Main(), "Main", 1 << 28).start();
	}
	private Scanner in = new Scanner(new InputStreamReader(System.in));
	private PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
}
