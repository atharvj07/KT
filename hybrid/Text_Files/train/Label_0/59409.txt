import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.Scanner;

public class Main {

	static Scanner sc = new Scanner(System.in);
	static ArrayList<Group> preset = new ArrayList<Group>();
	static Group U;

	public static void main(String[] args) throws Exception {
		while (sc.hasNext()) {
			preset.clear();
			for (int i = 0; i < 5; ++i) {
				preset.add(new Group());
			}
			while (true) {
				String label = sc.next();
				int N = sc.nextInt();
				if (label.equals("R")) break;
				for (int i = 0; i < N; ++i) {
					preset.get(label.charAt(0) - 'A').set.add(sc.nextInt());
				}
			}
			U = new Group();
			for (int i = 0; i < preset.size(); ++i) {
				U.set.addAll(preset.get(i).set);
			}
			Parser parser = new Parser(sc.next());
			Group result = parser.parse();
			ArrayList<Integer> ans = new ArrayList<Integer>(result.set);
			Collections.sort(ans);
			if (ans.isEmpty()) {
				System.out.println("NULL");
			} else {
				for (int i = 0; i < ans.size(); ++i) {
					if (i != 0) System.out.print(" ");
					System.out.print(ans.get(i));
				}
				System.out.println();
			}
		}
	}

	static class Parser {
		String expr;
		int pos = 0;

		Parser(String expr) {
			this.expr = expr;
		}

		Group parse() {
			Group left = term();
			while (pos < expr.length()) {
				char op = expr.charAt(pos);
				++pos;
				if (op == ')') break;
				Group right = term();
				switch (op) {
				case 'u':
					left.set.addAll(right.set);
					break;
				case 'i':
					left.set.retainAll(right.set);
					break;
				case 'd':
					left.set.removeAll(right.set);
					break;
				case 's':
					HashSet<Integer> intersect = new HashSet<Integer>(left.set);
					intersect.retainAll(right.set);
					left.set.removeAll(intersect);
					right.set.removeAll(intersect);
					left.set.addAll(right.set);
					break;
				}
			}
			return left;
		}

		Group term() {
			char c = expr.charAt(pos);
			++pos;
			if (c == '(') {
				return parse();
			}
			if (c == 'c') {
				Group g = term();
				Group ret = new Group();
				ret.set.addAll(U.set);
				ret.set.removeAll(g.set);
				return ret;
			}
			Group ret = new Group();
			ret.set.addAll(preset.get(c - 'A').set);
			return ret;
		}
	}

	static class Group {
		HashSet<Integer> set = new HashSet<Integer>();;
	}

}