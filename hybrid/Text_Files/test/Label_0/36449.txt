import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line = "";

		StringBuilder sb = new StringBuilder();
		while (!(line = br.readLine()).equals("0")) {

			int n = Integer.parseInt(line);
			String str = br.readLine();
			for (int i = n; i > 0; i--) {
				str = generate(str);
			}
			sb.append(str + "\n");
		}
		System.out.print(sb.toString());
	}

	static String generate(String str) {

		StringBuilder sb = new StringBuilder();
		char prev = str.charAt(0);
		int cnt = 1;
		for (int i = 1; i < str.length(); i++) {
			char next = str.charAt(i);
			if (next == prev) {
				cnt++;
			} else {
				sb.append(cnt).append(prev);
				prev = next;
				cnt = 1;
			}
		}
		sb.append(cnt).append(prev);
		return sb.toString();
	}
}