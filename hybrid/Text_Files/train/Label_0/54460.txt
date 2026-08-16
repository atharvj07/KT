import java.util.Scanner;

public class Main{
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int n;

		n = sc.nextInt();
		for (int i = 0; i < n; i++) {
			String snake = sc.next();
			String answer = "NA";
			int index = 0;
			if (6 <= snake.length()) {
				if (snake.charAt(0) == '>' && snake.charAt(snake.length() - 1) == '~') {
					snake = snake.substring(1, snake.length() - 1);
					if (snake.charAt(0) == '\'') {
						snake = snake.substring(1);
						if (snake.length() % 2 == 1) {
							answer = "A";
							for (int j = 0; j < snake.length(); j++) {
								if (j == snake.length() / 2 && snake.charAt(j) != '#') {
									answer = "NA";
								} else if (j != snake.length() / 2 && snake.charAt(j) != '=') {
									answer = "NA";
								}
							}
						}
					} else if (snake.charAt(0) == '^' && snake.charAt(snake.length() - 1) == '~') {
						snake = snake.substring(1, snake.length() - 1);
						if (snake.length() % 2 == 0) {
							answer = "B";
							for (int j = 0; j < snake.length(); j++) {
								if (j % 2 == 0 && snake.charAt(j) != 'Q') {
									answer = "NA";
								} else if (j % 2 == 1 && snake.charAt(j) != '=') {
									answer = "NA";
								}
							}
						}
					}
				}
			}
			System.out.println(answer);
		}
	}
}