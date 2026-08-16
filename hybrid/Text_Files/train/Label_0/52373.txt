import java.util.Deque;
import java.util.LinkedList;
import java.util.Scanner;

public class Main {
	enum Go {
		W, B;
		static Go of(String s) {
			return ("0".equals(s)) ? W : B;
		};
	};

	public static void main(String[] arg) {
		Scanner in = new Scanner(System.in);
		for (int n; (n = in.nextInt()) != 0;) {
			Deque<Integer> table = new LinkedList<Integer>();
			Go nowLast = null;
			for (int posi = 1; posi <= n; posi++) {
				Go put = Go.of(in.next());
				if (put.equals(nowLast)) {
					table.addLast(Integer.valueOf(table.removeLast() + 1));
				} else {
					if (posi % 2 == 1) {
						table.addLast(Integer.valueOf(1));
					} else {
						int add = 1 + table.removeLast().intValue();
						Integer prepre = table.pollLast();
						if (prepre != null) {
							add += prepre.intValue();
						}
						table.addLast(Integer.valueOf(add));
					}
				}
				nowLast = put;
			}
			if (nowLast.equals(Go.B)) {
				table.removeLast();
			}
			int counter = 0;
			for (; !table.isEmpty();) {
				counter += table.removeLast().intValue();
				table.pollLast();
			}
			System.out.println(counter);
		}
		in.close();
	}
}