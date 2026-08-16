import java.util.Scanner;
import java.util.Stack;

public class Main {
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		while(sc.hasNextLine()){
			String s = sc.nextLine();
      if(s.equals(".")) break;

			Stack<Character> count = new Stack<>(); 
			boolean flag = true;
			LABEL:
				for(int i = 0; i < s.length(); i++) {
					char c = s.charAt(i);
					switch(c) {
					case '(':
						count.push(')');
						break;
					case '[':
						count.push(']');
						break;
					case ')':
					case ']':
						if(count.isEmpty() || count.peek() != c) {
							flag = false;
							break LABEL;
						}else {
							count.pop();
						}
					}
				}

					if(count.isEmpty() && flag) {
						System.out.println("yes");
					}
					else {
						System.out.println("no");
					}
				}
		}	
	}
