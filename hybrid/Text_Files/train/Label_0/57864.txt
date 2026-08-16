import java.util.*;

public class Problem8a{
	
	public static String reverse(String str){
		String output = "";
		for(int i = str.length() -1; i >= 0; i--){
			output += str.charAt(i);
		}

		return output;
	}

	public static boolean check(String real, String first, String second){
		int seq1 = real.indexOf(first);
		if(seq1 == -1)
			return false;
		String afterSleep = real.substring(seq1 + first.length(), real.length());
		if(afterSleep.contains(second)){
			return true;
		}
		else
			return false;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String real = sc.nextLine();
		String first = sc.nextLine();
		String second = sc.nextLine();
		String output = "";
		
		boolean forward = check(real, first, second);
		boolean backward =check(real, reverse(second), reverse(first));
		if(forward && backward)
			System.out.println("both");
		else if(forward)
			System.out.println("forward");
		else if(backward)
			System.out.println("backward");
		else
			System.out.println("fantasy");
	}
}
