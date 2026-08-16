import java.util.Scanner;

class Main{
 public static void main(String args[]){
   Scanner sc = new Scanner(System.in);
   int N = sc.nextInt();
   int R = sc.nextInt();

   int C=0;
   if(N>=10){
     C=R;
   }
  else if(N<10){
     C=R+(100*(10-N));
   }
 System.out.println(C);
 }
}
