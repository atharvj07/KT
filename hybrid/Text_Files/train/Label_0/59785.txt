import java.io.IOException;
import java.io.InputStreamReader;
import java.util.InputMismatchException;
import java.io.PrintStream;
import java.io.BufferedReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.TreeSet;
import java.io.Reader;
import java.io.Writer;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 * @author Nipuna Samarasekara
 */
public class Main {
	public static void main(String[] args) {
		InputStream inputStream = System.in;
		OutputStream outputStream = System.out;
		FastScanner in = new FastScanner(inputStream);
		FastPrinter out = new FastPrinter(outputStream);
		TaskB solver = new TaskB();
		solver.solve(1, in, out);
		out.close();
	}
}

class TaskB {
    /////////////////////////////////////////////////////////////
    public void solve(int testNumber, FastScanner in, FastPrinter out) {
     int n=in.nextInt(),m=in.nextInt(),k=in.nextInt();
      int[][] A= new int[n][m];


     if(n>m)
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                A[i][j]=in.nextInt();

            }
        }
     else{
         int t=n;
         n=m;m=t;
         A= new int[n][m];
         for (int i = 0; i < m; i++) {
             for (int j = 0; j < n; j++) {
                 A[j][i]=in.nextInt();

             }
         }

     }

        TreeSet<String> types= new TreeSet<String>();
        String[] aa= new String[n];
        for (int i = 0; i < n; i++) {
            StringBuilder sb= new StringBuilder();
            for (int j = 0; j < m; j++) {
                sb.append(A[i][j]);
            }
            aa[i]=sb.toString();
            types.add(aa[i]);

        }
        if(types.size()>12){
            out.println(-1);
            return ;

        }
      int kk=k+10;
       if(n>10){
        for (String t1 : types) {
         StringBuilder sb= new StringBuilder();
            for (int i = 0; i < t1.length(); i++) {
                if(t1.charAt(i)=='1')sb.append('0');
                else sb.append('1');
            }
            String t2=sb.toString();
          //  System.out.println(t2);
               int score=0;
                for (int i = 0; i < n; i++) {
                  score+=Math.min(getD(aa[i],t1),getD(aa[i],t2));
                }
                kk=Math.min(kk,score);

        }  }
        else {
           for (int z = 0; z < (int) Math.pow(2, m); z++) {
           StringBuilder ss= new StringBuilder();
           int t=z;
               for (int j = 0; j < m; j++) {
                   if(t%2==1)ss.append('1') ;
                   else ss.append('0');

                   t/=2;
               }
               String t1=ss.toString();
               StringBuilder sb= new StringBuilder();
               for (int i = 0; i < t1.length(); i++) {
                   if(t1.charAt(i)=='1')sb.append('0');
                   else sb.append('1');
               }
               String t2=sb.toString();
               //  System.out.println(t2);
               int score=0;
               for (int i = 0; i < n; i++) {
                   score+=Math.min(getD(aa[i],t1),getD(aa[i],t2));
               }
               kk=Math.min(kk,score);






           }




       }

        if(kk>k){
            out.println(-1);
        }
        else
            out.println(kk);

    }
    static int getD(String A, String B){
        int ret=0;
        for (int i = 0; i < A.length(); i++) {
            if(A.charAt(i)!=B.charAt(i))ret++;
        }
       return ret;
    }
}

class FastScanner extends BufferedReader {

    public FastScanner(InputStream is) {
        super(new InputStreamReader(is));
    }

    public int read() {
        try {
            int ret = super.read();
//            if (isEOF && ret < 0) {
//                throw new InputMismatchException();
//            }
//            isEOF = ret == -1;
            return ret;
        } catch (IOException e) {
            throw new InputMismatchException();
        }
    }

    static boolean isWhiteSpace(int c) {
        return c >= 0 && c <= 32;
    }

    public int nextInt() {
        int c = read();
        while (isWhiteSpace(c)) {
            c = read();
        }
        int sgn = 1;
        if (c == '-') {
            sgn = -1;
            c = read();
        }
        int ret = 0;
        while (c >= 0 && !isWhiteSpace(c)) {
            if (c < '0' || c > '9') {
                throw new NumberFormatException("digit expected " + (char) c
                        + " found");
            }
            ret = ret * 10 + c - '0';
            c = read();
        }
        return ret * sgn;
    }

    public String readLine() {
        try {
            return super.readLine();
        } catch (IOException e) {
            return null;
        }
    }

}

class FastPrinter extends PrintWriter {

    public FastPrinter(OutputStream out) {
        super(out);
    }

    public FastPrinter(Writer out) {
        super(out);
    }


}

