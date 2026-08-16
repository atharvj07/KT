import java.util.*;
public class Main {
	static String S;
	static int p;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		S = sc.next();
		boolean ok = cat();
		if(ok) {
			System.out.println("Cat");
		}
		else {
			System.out.println("Rabbit");
		}
		
		
		
	}
	static boolean cat() {
		return m() &&p == S.length();
	}
	
	static boolean m() {
		//System.out.println(p);
		if(S.length() <= p) return false;
		if(S.charAt(p) != 'm') return false;
		p++;
		return e();
	}
	static boolean e() {
		//System.out.println(p);
		if(S.length() <= p) return false;
		while(S.charAt(p) != 'e') {
			if(!m()) return false;
		}
		p++;
		
		return w();
	}
	static boolean w() {
		//System.out.println(p);
		if(S.length() <= p) return false;
		while(S.charAt(p) != 'w') {
			if(!m()) return false;
		}
		p++;
		return true;
	}

}