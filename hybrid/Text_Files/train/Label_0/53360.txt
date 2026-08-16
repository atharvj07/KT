import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.next();
		s = s.replaceAll("eraser", "").replaceAll("erase", "").replaceAll("dreamer", "").replaceAll("dream", "");
		if(s.equals("")) {
			System.out.println("YES");
		} else {
			System.out.println("NO");
		}
	}
}
