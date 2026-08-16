import java.util.*;
import java.lang.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.next();
		int year = Integer.parseInt(s.substring(0, 4));
		int month = Integer.parseInt(s.substring(5, 7));
		int day = Integer.parseInt(s.substring(8, 10));
		if (year > 2019 || (year == 2019 && month > 4)) {
			System.out.println("TBD");;
		} else {
			System.out.println("Heisei");
		}
	}
}