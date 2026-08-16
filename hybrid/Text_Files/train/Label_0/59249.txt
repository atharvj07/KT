import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
	public static void main(String[] args) {
		@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);

		String s = sc.nextLine();
		String ptn = sc.nextLine();
		ptn = ptn.replaceAll("_", ".");

		Matcher m = Pattern.compile(ptn).matcher(s);

		if (m.find()) {
			System.out.println("Yes");
		} else {
			System.out.println("No");
		}
	}
}

