
import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		new Main().run();
	}

	private void run() throws IOException {
		Scanner scanner = new Scanner(System.in);
		int pre = 4280;
		while (true) {
			int cost = scanner.nextInt();
			if (cost == -1)
				break;
			int ans = 1150;
			if (cost > 10)
				ans += (cost - 10) * 125;
			if (cost > 20)
				ans += (cost - 20) * 15;
			if (cost > 30)
				ans += (cost - 30) * 20;
			System.out.println(pre - ans);
		}
	}
}