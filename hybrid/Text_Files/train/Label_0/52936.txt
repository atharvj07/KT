

import java.util.Scanner;

public class hello64 {
	// String s;
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		String s = input.next();
		boolean hasAn = false;
		for (int j = 0; j <= s.length(); j++) {
			String newS = "";
			for (int i = 0; i < 26; i++) {
				// System.out.println((char)(i+97));
				newS = s.substring(0, j);
				// System.out.println(newS);
				newS += (char) (i + 97);
				newS += s.substring(j);
				// System.out.println(newS);
				// System.out.println(newS);
				// System.out.println("");
				// System.out.println(isPalind(newS);
				if (isPalind(newS)) {
					System.out.println(newS);
					hasAn = true;
					break;
				}
			}
			if(hasAn) break;
		}
		if (!hasAn) {
			System.out.println("NA");
		}

	}

	public static boolean isPalind(String s) {
		int startIndex = 0;
		if (s.length() % 2 != 0) {
			startIndex = s.length() / 2;
			// System.out.println(s);
			// int dis = 1;
			for (int dis = 1; dis <= s.length() - s.length() / 2 - 1; dis++) {
				if (s.charAt(startIndex + dis) != s.charAt(startIndex - dis)) {
					return false;
				}
			}
			return true;
		} else {
			for (int dis = 0; dis <= s.length() / 2; dis++) {
				if (s.charAt(startIndex + dis) != s.charAt(s.length() - dis-1)) {
					return false;
				}
			}
			return true;
		}
		// return false;
	}
}
