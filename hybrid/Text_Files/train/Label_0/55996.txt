import java.io.IOException;
import java.math.BigInteger;
import java.util.Locale;
import java.util.Scanner;

public class A {

	private void processInput() throws IOException {
		Scanner in = new Scanner(System.in);

		String str = in.next();
		String res = go(str);

		System.out.printf(Locale.ENGLISH, "%s\n", res);

		in.close();
	}

	private String go(String str) {

		String res = "";
		
		int idx = str.indexOf('.');
		String integer = str.substring(0, idx);
		
		if (str.charAt(idx - 1) == '9') {
			return "GOTO Vasilisa.";
		}
		char c = str.charAt(idx + 1);
		if (c >= '5') {
			res = new BigInteger(integer).add(BigInteger.valueOf(1)).toString();
		} else {
			res = new BigInteger(integer).toString();
		}

		return res;
	}

	public static void main(String[] args) throws Exception {
		A a = new A();
		a.processInput();
	}
}