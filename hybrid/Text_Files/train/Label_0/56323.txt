import java.io.*;
import java.util.*;

public class Towers {
    public static void main(String args[]) {
      Scanner input = new Scanner(System.in);
      long  n = input.nextLong();
      
      long count = 0;
      boolean is_prime = true;
	  
	  int temp = 0;
      for ( int i = 2; i <= Math.sqrt(n); i++){ 
	     if ( n % i == 0 ){
			 temp = i;
			 is_prime = false;
			 break;
	  }
      }
	  
	  if ( is_prime ){
		  count = 1;
	  }
	  else {
	      count =  1 + ( n - (long)temp ) / 2;
	  }
	  
      System.out.println(count);
   }
}
