import java.util.*;
public class Main{
   public static void main(String[] args) {
     Scanner sc = new Scanner(System.in);
     int N = sc.nextInt();
     int M = sc.nextInt();
     int L,R,lhold,rhold,ans;
     L = 0;
     R = N;
     for(int i = 0;i<M;i++){
       lhold = sc.nextInt();
       rhold = sc.nextInt();
       if(L<lhold){
         L = lhold;
       }
       if(R>rhold){
         R = rhold;
       }
     }
     if(L<=R){
       ans = R-L+1;
     }else{
       ans = 0;
     }
     System.out.println(ans);


   }
}
