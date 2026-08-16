import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] inputArr = sc.nextLine().split(" ");
		sc.close();
		char input1 = inputArr[0].charAt(0);
		char input2 = inputArr[1].charAt(0);
		      
		if(input1 < input2) {
			System.out.println("<");
		}else if(input1 > input2) {
			System.out.println(">");
		}else {
			System.out.println("=");
		}
	}

}