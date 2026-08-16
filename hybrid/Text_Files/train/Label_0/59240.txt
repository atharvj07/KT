import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.Scanner;
import java.util.Set;

public class Main {
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		while (true) {
			String init = sc.next();
			if (init.equals("0"))
				break;
			Queue<String> q = new LinkedList<String>();
			Map<String, Integer> nodes = new HashMap<String, Integer>();
			Set<String> visited = new HashSet<String>();
			nodes.put(init, 0);
			q.add(init);
			String anss[] = { init.replaceAll(".", "r"),
					init.replaceAll(".", "g"), init.replaceAll(".", "b") };
			String ans = "";
			boolean flag = false;
			while (q.peek() != null) {
				String bug = q.poll();
				for (int i = 0; i < 3; i++) {
					if (bug.equals(anss[i])) {
						flag = true;
						ans = anss[i];
						break;
					}
				}
				if (flag)
					break;
				if (visited.contains(bug))
					continue;
				visited.add(bug);

				for (int i = 0; i < bug.length() - 1; i++) {
					char a = bug.charAt(i);
					char b = bug.charAt(i + 1);
					if (a != b) {
						char[] cs = bug.toCharArray();
						if (a != 'r' && b != 'r') {
							cs[i] = cs[i + 1] = 'r';
						} else if (a != 'g' && b != 'g') {
							cs[i] = cs[i + 1] = 'g';
						} else {
							cs[i] = cs[i + 1] = 'b';
						}
						String nbug = (new StringBuilder()).append(cs)
								.toString();
						q.add(nbug);
						nodes.put(nbug, nodes.get(bug) + 1);
					}
				}
			}

			System.out.println(flag ? nodes.get(ans) : "NA");
		}
	}
}