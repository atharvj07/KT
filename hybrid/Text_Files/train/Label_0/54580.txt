import java.util.Arrays;
import java.util.Scanner;

public class Main{
	static class Team implements Comparable<Team>{
		String name;
		int score;

		Team(String name) {
			this.name = name;
			this.score = 0;
		}

		public int compareTo(Team t) {
			return t.score - this.score;
		}
	}

	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int n;
		Team t[];
		String enter = "";

		while (true) {
			n = sc.nextInt();
			if (n == 0) {
				break;
			}
			t = new Team[n];
			for (int i = 0; i < n; i++) {
				String name = sc.next();
				int win = sc.nextInt();
				int lose = sc.nextInt();
				int draw = sc.nextInt();
				t[i] = new Team(name);
				t[i].score = win * 3 + draw;
			}
			Arrays.sort(t);
			System.out.print(enter);
			for (int i = 0; i < n; i++) {
				System.out.println(t[i].name + "," + t[i].score);
			}
			enter = "\n";
		}
	}
}