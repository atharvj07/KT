import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
 
public class Main {
	private	static	BufferedReader	br = null;
	private	static	char[][]		wt = { { 'a', 'b', 'c', 'd', 'e' }, { 'f', 'g', 'h', 'i', 'j' }, { 'k', 'l', 'm', 'n', 'o' }, { 'p', 'q', 'r', 's', 't' }, { 'u', 'v', 'w', 'x', 'y' }, { 'z', '.', '?', '!', ' ' } };

	static {
		br = new BufferedReader(new InputStreamReader(System.in));
	}
 
    /**
     * @param args
     */
	public static void main(String[] args) {
		String  stdin = null;
		while ((stdin = parseStdin()) != null) {
			int		i = 0;
			int		l = stdin.length();
			boolean	f = (l % 2 == 0 && stdin.equals(stdin.replaceAll("[^1-6]", "")));
			String	o = "";

			while (f && i < l) {
				int	j = (stdin.charAt(i)-'1');
				int	k = (stdin.charAt(i+1)-'1');

				if ((f = (0 <= j && j <= 5 && 0 <= k && k <= 4))) {
					o += wt[j][k];
					i+=2;
				}
			}

			System.out.println((f) ? o: "NA");
		}
	}

	private static String parseStdin() {
		String  stdin = null;

		try {
			String  tmp = br.readLine();
			if (tmp != null) {
				if (!tmp.isEmpty()) stdin = tmp;
			}
		}
		catch (IOException e) {}

		return stdin;
	}
}