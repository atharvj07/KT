import java.io.*;
import java.util.*;
import java.math.*;
public class Bracket {
	public static void main(String[] args) {
		Stack<String> p = new Stack<String>();
		Scanner sc = new Scanner(System.in);
		String entry = sc.nextLine();
		int ans = entry.length();
		for(int i = 0; i < entry.length(); i++) {
			if(entry.charAt(i) == ')')
				if(p.isEmpty()) ans--;
				else p.pop();
			else
				p.push("(");
		}
		while(!p.isEmpty()) {
			ans--;
			p.pop();
		}
		System.out.println(ans);
	}
}
