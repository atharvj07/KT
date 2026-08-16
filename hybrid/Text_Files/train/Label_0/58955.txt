import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {

	static final HashMap<Character, Integer> roman = new HashMap<Character, Integer>() {
		{
			put('I', 1);
			put('V', 5);
			put('X', 10);
			put('L', 50);
			put('C', 100);
			put('D', 500);
			put('M', 1000);
		}
	};

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line = "";

		StringBuilder sb = new StringBuilder();
		while ((line = br.readLine()) != null) {

			int result = 0;
			char next, prev = 'I';
			for (int i = line.length() - 1; i >= 0; i--) {
				next = line.charAt(i);
				if (roman.get(next) < roman.get(prev)) {
					result -= roman.get(next);
				} else {
					result += roman.get(next);
				}
				prev = next;
			}
			sb.append(result + "\n");
		}
		System.out.print(sb.toString());
	}
}