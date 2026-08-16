import java.util.*;
public class Main {
   static Scanner sc = new Scanner(System.in);

   public static void main(String[] args) {
      int N = sc.nextInt();
      int M = sc.nextInt();
      int X = sc.nextInt();
      int Y = sc.nextInt();
      int Z;
      String msg = "War";
      int[] xAr = new int[N];
      int[] yAr = new int[M];


      for (int i = 0; i < N; i++) {
         xAr[i] = sc.nextInt();
      }
      Arrays.sort(xAr);
      for (int i = 0; i < M; i++) {
         yAr[i] = sc.nextInt();
      }
      Arrays.sort(yAr);

      for (Z = X + 1; Z <= Y; Z++) {
         if (Z > xAr[N - 1] && Z <= yAr[0]) {
            msg = "No War";
            break;
         }
      }

      System.out.println(msg);
   }
}