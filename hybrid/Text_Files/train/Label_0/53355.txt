
import java.io.*;
import java.util.*;
import java.math.*;
import static java.lang.Math.*;
import static java.lang.Integer.parseInt;
import static java.lang.Long.parseLong;
import static java.lang.Double.parseDouble;
import static java.lang.String.*;


public class Main {

    static StringBuilder a = new StringBuilder();

    public static void main(String[] args) throws IOException {
        //BufferedReader in = new BufferedReader(new InputStreamReader(System.in));                                    //(new FileReader("input.in"));
        //StringBuilder out = new StringBuilder();
        //StringTokenizer tk;
        // Scanner Reader = new Scanner(System.in);
        Reader.init(System.in);
        StringBuilder a = new StringBuilder(Reader.next());
            StringBuilder b = new StringBuilder();
            if(a.charAt(0)=='@'||a.charAt(a.length()-1)=='@'||a.indexOf("@@")!=-1||a.indexOf("@")==-1){
                System.out.println("No solution");
                System.exit(0);
            }
        while(a.indexOf("@")!=-1){
        b.append(a.substring(0, a.indexOf("@")+2));
        a.delete(0, a.indexOf("@")+2);
        if(a.indexOf("@")!=-1)
            b.append(",");
        }
        b.append(a);
        if(b.indexOf(",@")!=-1||b.charAt(b.length()-1)=='@'){
        System.out.println("No solution");
                System.exit(0);
        }
        System.out.println(b+"");
        
        
       }

    }



//class Point implements Comparable<Point> {
//
//    int x, y;
//
//    public Point(int a, int b) {
//        x = a;
//        y = b;
//
//    }
//
//    @Override
//    public boolean equals(Object object) {
//        boolean sameSame = false;
//
//        if (object != null && object instanceof Point) {
//            sameSame = this.x == ((Point) object).x;
//        }
//     
//
//        return sameSame;
//    }
//
// 
//    @Override
//    public int compareTo(Point o) {
//        return this.y-o.y;
//    }
//}

//class Book {
//
//    String a;
//    int b, c,ind;
//
//    public Book(String x, int y) {
//        a = x;
//        b = y;
//        
//
//    }
//
//    @Override
//    public boolean equals(Object object) {
//        boolean sameSame = false;
//
//        if (object != null && object instanceof Book) {
//            sameSame = (this.a == null ? ((Book) object).a == null : this.a.equals(((Book) object).a));
//        }
//        if (object != null && object instanceof Book) {
//            sameSame = this.b == ((Book) object).b;
//        }
//
//        return sameSame;
//    }
//}
//


class Reader {

    static StringTokenizer tokenizer;
    static BufferedReader reader;

    public static void init(InputStream input) throws UnsupportedEncodingException {
        reader = new BufferedReader(new InputStreamReader(input, "UTF-8"));
        tokenizer = new StringTokenizer("");
    }

    public static String next() throws IOException {
        while (!tokenizer.hasMoreTokens()) {
            tokenizer = new StringTokenizer(reader.readLine());
        }
        return tokenizer.nextToken();
    }

    public static String nextLine() throws IOException {
        return reader.readLine();
    }

    public static int nextInt() throws IOException {
        return Integer.parseInt(next());
    }

    public static double nextDouble() throws IOException {
        return Double.parseDouble(next());
    }

    public static long nextLong() throws IOException {
        return Long.parseLong(next());
    }
}
