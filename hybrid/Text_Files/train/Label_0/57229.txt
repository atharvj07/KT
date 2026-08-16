import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) {
		try {
			BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
			String str;
			while (null != (str = in.readLine())) {
				String[] sp = str.split(" ");
				printTree(sp[0].charAt(0), sp[1], sp[2]);
				System.out.println();
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	static void printTree(char iu, String t1, String t2) {
		// System.out.println("[" + t1 + "][" + t2 + "]");
		if (iu == 'i' ?
				t1.length() == 0 || t2.length() == 0 :
					t1.length() == 0 && t2.length() == 0) {
			return;
		}
		String l1 = "", l2 = "", r1 = "", r2 = "";
		if (t1.length() > 0) {
			if (t1.charAt(1) == '(') {
				int level = 1;
				int i;
				for (i = 2; level > 0; i++) {
					if (t1.charAt(i) == '(') {
						level++;
					} else if (t1.charAt(i) == ')') {
						level--;
					}
				}
				l1 = t1.substring(1, i);
			} else {
				l1 = "";
			}
			r1 = t1.substring(1 + l1.length() + 1, t1.length() - 1);
		}
		if (t2.length() > 0) {
			if (t2.charAt(1) == '(') {
				int level = 1;
				int i;
				for (i = 2; level > 0; i++) {
					if (t2.charAt(i) == '(') {
						level++;
					} else if (t2.charAt(i) == ')') {
						level--;
					}
				}
				l2 = t2.substring(1, i);
			} else {
				l2 = "";
			}
			r2 = t2.substring(1 + l2.length() + 1, t2.length() - 1);
		}
		System.out.print("(");
		printTree(iu, l1, l2);
		System.out.print(",");
		printTree(iu, r1, r2);
		System.out.print(")");
	}
}