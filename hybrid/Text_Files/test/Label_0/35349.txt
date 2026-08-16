
import java.util.Scanner;

public class Main {

     static Scanner scanner;

     public static void main(String[] args) {
         scanner = new Scanner(System.in);

         int N=gi();
         long K=gl();
         long[] P=new long[N];
         long[] C=new long[N];
         for (int i=0; i<N;i++) {
        	 P[i]=gl()-1;
         }
         for (int i=0; i<N;i++) {
        	 C[i]=gl();
         }

         long ans=Long.MIN_VALUE;

         for (int s=0; s<N;s++) {
        	 long pos=s;
        	 long tmp=0;
        	 long roop=0;
        	 long max=C[(int)P[s]];
        	 do {
        		 roop++;
        		 pos=P[(int)pos];
        		 tmp+=C[(int)pos];
        		 max=Math.max(max, tmp);
        	 } while(pos!=s && roop<K);

        	 if(tmp>0 && roop!=K) {
        		 long r=Math.floorDiv(K, roop);
        		 long z=K%roop;
        		 z+=roop;
        		 long mm=tmp*(r-1);
        		 pos=s;
        		 tmp=0;
        		 max=0;
        		 for (int i=0; i<z;i++) {
        			 pos=P[(int)pos];
        			 tmp+=C[(int)pos];
        			 max=Math.max(max, tmp);
        		 }
        		 max+=mm;
        	 }
        	 ans=Math.max(ans, max);
         }

         System.out.println(ans);
     }

     // 文字列として入力を取得
     public static String gs() {
          return scanner.next();
     }

     // intとして入力を取得
     public static int gi() {
          return Integer.parseInt(scanner.next());
     }

     // longとして入力を取得
     public static long gl() {
          return Long.parseLong(scanner.next());
     }

     // doubleとして入力を取得
     public static double gd() {
          return Double.parseDouble(scanner.next());
     }
}