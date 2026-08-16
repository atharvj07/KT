/**
 * 
 */
import java.util.Scanner;

/**
 * @author Neeraj
 *
 */
 class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int k=sc.nextInt();
		String s=sc.next();
		
		if(s.length()<=k)
			System.out.println(s);
		else
			System.out.println(s.substring(0,k)+"...");
	}

}
