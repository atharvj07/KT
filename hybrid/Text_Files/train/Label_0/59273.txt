import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.next();
		int f = s.indexOf("A");
		int l = s.lastIndexOf("Z");
		
		System.out.println(l-f+1);
	}
}
