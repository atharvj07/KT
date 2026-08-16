import java.util.Arrays;
import java.util.Scanner;

public class Main {

	static Scanner sc = new Scanner(System.in);
	static String line;

	static int index(char c) {
		if ('a' <= c && c <= 'z') return c - 'a';
		return 26 + c - 'A';
	}

	static boolean satisfy(String clause) {
		String[] vars = clause.split("&");
		boolean[][] used = new boolean[2][52];
		for (String var : vars) {
			int pos = var.length() - 1;
			int i = index(var.charAt(pos));
			if (used[1 - pos][i]) return false;
			used[pos][i] = true;
		}
		return true;
	}

	static boolean solve() {
		String[] clause = line.split("\\|");
		for (String c : clause) {
			if (satisfy(c.substring(1, c.length() - 1))) return true;
		}
		return false;
	}

	public static void main(String[] args) throws Exception {
		while (true) {
			line = sc.next();
			if (line.equals("#")) break;
			System.out.println(solve() ? "yes" : "no");
		}
	}
}