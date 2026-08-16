import java.util.Scanner;
import java.util.Stack;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Stack<Integer> s = new Stack<Integer>();
		while(sc.hasNext()) {
			int a = sc.nextInt();
			if(a==0) System.out.println(s.pop());
			else s.push(a);
		}
	}
}

