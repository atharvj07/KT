import java.util.*;
 
public class Main {
	public static void main (String[] args) {
		Scanner in = new Scanner(System.in);
		
		int n = in.nextInt();
      	int nam = 0;
      	int sum = 0;
      	int nam1[] = new int[n];
      	int nam2[] = new int[n-1];
      
      for(int i = 0;i < n;i++){
       nam1[i] = in.nextInt();
      }
     
      for(int i = 0;i < n;i++){
       sum += in.nextInt();
      }   

      for(int i = 0;i < n-1;i++){
       nam2[i] = in.nextInt();
      }
      
      for(int i = 0; i < n-1;i++){
      nam = nam1[i] +1;
      if(nam==nam1[i+1]){
      sum += nam2[nam-2];
      }
      }
      System.out.print(sum);
	}
}