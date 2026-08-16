import java.util.Scanner;
import java.util.Arrays;

public class Main3{
   public static void main(String[] Args){
      
	   Scanner sc = new Scanner(System.in);
	   
	   int n = sc.nextInt();
	   int median = sc.nextInt();
  
       int[] a = new int[n + 1];
       for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
       }
       a[n] = Integer.MAX_VALUE;
       Arrays.sort(a);
	
       int pos = 0, count = 0, cur_median = ((n + 1) / 2 - 1);
       //1. Find the position of the median in the array
       for (int i = 0; i < n; i++) {
    	   if (a[i] < median && a[i + 1] > median) {
		        count++;
		        n++;
		        pos = i + 1;
		   }
    	   else {
               if (a[i] == median) {
                   pos = i;
                   if (i >= cur_median) {
                       break;
                   }
               }
           }
		}
       //edge case to add to the beggining
		if (pos == 0 && a[0] != median) {
		    n++;
		    count++;
		}
	    // Figure out how many more we need to add to the set
		while (pos != (cur_median = ((n + 1) / 2 - 1))){
		    if (pos < cur_median) {
		        pos++;
		    }
		    count++;
		    n++;
		}
		System.out.println(count);
               // :(
   }
 
}