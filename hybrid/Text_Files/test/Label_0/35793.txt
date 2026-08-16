import java.util.*;
import java.io.*;
import java.awt.*;
import java.awt.geom.Point2D;
import static java.lang.Math.*;
public class Main {
   public static void main(String[] $) {
       int n=sc.nextInt();
       long[] a=new long[n];
       for (int i = 0; i < n; i++) {
           a[i]=sc.nextLong();
       }
       int m=sc.nextInt();
       long[] b=new long[m];
       for (int i = 0; i < m; i++) {
           b[i]=sc.nextLong();
       }
       int temp=0;
       for (int i = 0; i < m; i++) {
           if(Arrays.binarySearch(a,b[i])>=0)temp++;
       }
       out.println(temp==m?1:0);
       out.close();
   }

   static PrintWriter out = new PrintWriter(System.out);

   static class sc {
       static Scanner s = new Scanner(System.in);

       static String next() {
           return s.next();
       }

       static String nextLine() {
           return s.nextLine();
       }

       static int nextInt() {
           return Integer.parseInt(s.next());
       }

       static long nextLong() {
           return Long.parseLong(s.next());
       }

       static double nextDouble() {
           return Double.parseDouble(s.next());
       }

       static boolean hasNext() {
           return s.hasNext();
       }
   }
}
