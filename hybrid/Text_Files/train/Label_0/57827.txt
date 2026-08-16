import java.util.Scanner;

public class Main {
	  
	public static void main(String args[]) {
		    Scanner scanner = new Scanner(System.in);
		    
		    String S = scanner.next();
		    String T = scanner.next();
		    
		   if( S.equals(T) ) 
		   {
				System.out.println("H");   
		   }
		   else
		   {
			   System.out.println("D");
		   }
		    scanner.close(); }
		  }