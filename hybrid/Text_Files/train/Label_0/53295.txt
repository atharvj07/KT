import java.util.Scanner;

public class Main {
	public static void main(String args[]) {
		Scanner scn = new Scanner(System.in);
		int N, M, ans;
		boolean loop;
		while ((N = scn.nextInt()) != 0) {
			M = scn.nextInt();
			int[] tile = new int[N * M];
			boolean[] through = new boolean[N * M];
			String buf = scn.nextLine();
			for (int i = 0; i < N * M; i++) {
				
				if (i % M == 0) {
					buf = scn.nextLine();
				}
				switch (buf.charAt(i % M)) {
				case '.':
					break;
				case '>':
					tile[i] = 1;
					break;
				case '<':
					tile[i] = -1;
					break;
				case 'v':
					tile[i] = M;
					break;
				case '^':
					tile[i] = -M;
					break;
				default:
					break;
				}
			}
			ans = 0;
			loop = false;
			while (tile[ans] != 0) {
				if (through[ans]) {
					loop = true;
					break;
				}
				through[ans] = true;
				ans += tile[ans];
			}
			System.out.println(loop ? "LOOP" : ans % M + " " + ans / M);
		}
		scn.close();
	}
}

