import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String line = br.readLine();

		String str[] = line.split("");

		long ans = 0;
		long tmp = 0;

		for (int i = 0; i < (1 << (line.length() - 1)); i++) {
			tmp = Integer.parseInt(str[0]);
			for (int j = 0; j < (line.length() - 1); j++) {
				if ((i & (1 << j)) != 0) {
					ans += tmp;
					tmp = 0;
				}

				tmp = tmp * 10 + (Integer.parseInt(str[j + 1]));
			}
			ans += tmp;
		}
		System.out.println(ans);
	}
}