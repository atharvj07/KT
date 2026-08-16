
import java.util.Arrays;
import java.util.Scanner;

public class Beecola {
public static void main(String[] args) {
   Scanner sc=new Scanner (System.in);
   int n=sc.nextInt();
   int ar[]=new int[n];
   for(int i=0;i<n;i++)
   {
       ar[i]=sc.nextInt();
   }
   Arrays.sort(ar);
   int m=sc.nextInt();
   int arr[]=new int[m];
    for(int i=0;i<m;i++)
    {
        arr[i]=sc.nextInt();
    }
    
        
           for(int i=0;i<m;i++)
   {
       int low = 0, high = n;
			while (low < high) {
				int mid = (int) Math.ceil((low + high) / 2);
				if (ar[mid] <=arr[i]) {
					low = mid + 1;
				} else {
					high = mid;
				}
           
       }
           System.out.println(low);
   }
}
    
}
