import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner s = new Scanner(System.in);

		while (true) {
			int N = s.nextInt();

			if (N == 0)
				break;

			int[][] graph = new int[21][21];

			for (int i = 0; i < N; i++) {
				int x = s.nextInt();
				int y = s.nextInt();
				graph[y][x] = 1;
			}

			// for (int p = 0; p < 21; p++) {
			// for (int q = 0; q < 21; q++) {
			// System.out.print(graph[p][q]);
			// }
			// System.out.println();
			// }

			int M = s.nextInt();
			int robox = 10, roboy = 10;

			for (int j = 0; j < M; j++) {
				char d = s.next().charAt(0);
				int l = s.nextInt();

				graph[roboy][robox] = 2;

				switch (d) {
				case 'N':
					for (int t = 0; t <= l; t++) {
						graph[roboy + t][robox] = 2;
					}
					roboy = roboy + l;
					break;

				case 'E':
					for (int t = 0; t <= l; t++) {
						graph[roboy][robox + t] = 2;
					}
					robox = robox + l;
					break;

				case 'W':
					for (int t = 0; t <= l; t++) {
						graph[roboy][robox - t] = 2;
					}
					robox = robox - l;
					break;

				case 'S':
					for (int t = 0; t <= l; t++) {
						graph[roboy - t][robox] = 2;
					}
					roboy = roboy - l;
					break;

				default:
					break;

				}

				// for (int p = 0; p < 21; p++) {
				// for (int q = 0; q < 21; q++) {
				// System.out.print(graph[p][q]);
				// }
				// System.out.println();
				// }

			}

			int count = 0;

			for (int p = 0; p < 21; p++) {
				for (int q = 0; q < 21; q++) {
					if (graph[p][q] == 1)
						count++;
				}
			}

			if (count == 0)
				System.out.println("Yes");
			else
				System.out.println("No");

		}
		s.close();
	}
}