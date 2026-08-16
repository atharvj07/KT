import java.util.*;
 
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int A = sc.nextInt();
        int B = sc.nextInt();
        int K = sc.nextInt();
  
      int a[] = new int[100];
      int n = 0;
      for(int i=1; i<=Math.min(A,B); i++){
      if(A%i==0 && B%i==0){
        n+=1;
        a[n] =i;
        }
      }
     System.out.println(a[n-K+1]);
    }
}
        