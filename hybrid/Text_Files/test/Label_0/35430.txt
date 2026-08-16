import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String alpha = sc.next();
		String regex = "[A-Z]";
		if(alpha.matches(regex)){
			System.out.println("A");
		}else {
			System.out.println("a");
		}

	}
}

