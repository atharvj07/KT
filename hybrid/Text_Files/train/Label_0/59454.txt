import java.util.*;
public class SuperHeroTransformation {
	static boolean isVow(char c) {
		if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u')return true;
		else return false;
	}

	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		String s=sc.nextLine();
		String t=sc.nextLine();
		if(s.length()!=t.length())System.out.println("No");
		else {
		boolean match=true;
		for(int i=0;i<s.length();i++) {
			 if((isVow(s.charAt(i)) && isVow(t.charAt(i))) || (isVow(s.charAt(i)) == false && isVow(t.charAt(i)) == false)) continue;
		        match = false;
		        break;
		}
		if(match)System.out.println("Yes");
		else System.out.println("No");
		}

	}

}
