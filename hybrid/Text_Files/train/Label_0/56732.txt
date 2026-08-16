import java.io.InputStream;
import java.io.PrintWriter;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.math.BigInteger;
import java.util.*;
import java.util.stream.Stream;

/**
 *
 * @author Pradyumn Agrawal coderbond007
 */

public class Codeforces{
    public static InputStream inputStream = System.in;
    public static FastReader in = new FastReader(inputStream);
    public static PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static int MOD = (int)1e9 + 9;
    public static void main(String[] args)throws java.lang.Exception
    {
        new Codeforces().run();
        out.close();
    }
    void run() throws java.lang.Exception
    {
        String s = ns();
		s = rem0(s);
		int ind = s.indexOf('.');
		if(ind == -1){
			pint(s);
		}else{
			s = reml0(s);
			if(s.charAt(s.length()-1) == '.'){
				s = s.substring(0, s.length()-1);
				pint(s);
			}else{
				ind = s.indexOf('.');
				int nz = 0;
				for(int i = 0;i < s.length();i++){
					if(s.charAt(i) != '0' && s.charAt(i) != '.'){
						nz = i;
						break;
					}
				}
				int e = nz < ind ? ind-nz-1 : ind-nz;
				s = s.substring(0, ind) + s.substring(ind+1); // erase dot
				String t = reml0(rem0(s));
				if(e == 0){
					if(t.length() == 1){
						out.printf("%c\n", t.charAt(0));
					}else{
						out.printf("%c.%s\n", t.charAt(0), t.substring(1));
					}
				}else{
					if(t.length() == 1){
						out.printf("%cE%d\n", t.charAt(0), e);
					}else{
						out.printf("%c.%sE%d\n", t.charAt(0), t.substring(1), e);
					}
				}
			}
		}
    }
    void pint(String s)
	{
		if(s.length() == 1){
			out.println(s);
		}else{
			String t = reml0(s);
			if(t.length() == 1){
				out.printf("%cE%d\n", t.charAt(0), s.length()-1);
			}else{
				out.printf("%c.%sE%d\n", t.charAt(0), t.substring(1), s.length()-1);
			}
		}
	}
	
	String reml0(String s)
	{
		for(int i = s.length()-1;i >= 0;i--){
			if(s.charAt(i) != '0'){
				return s.substring(0, i+1);
			}
		}
		return "";
	}
	
	String rem0(String s)
	{
		for(int i = 0;i < s.length();i++){
			if(s.charAt(i) != '0'){
				return s.substring(i);
			}
		}
		return "";
	}
    private static int ni(){
        return in.nextInt();
    }
    private static long nl(){
        return in.nextLong();
    }
    private static String ns(){
        return in.nextString();
    }
    private static char nc(){
        return in.nextCharacter();
    }
    private static double nd(){
        return in.nextDouble();
    }

    private static char[] ns(int n)
    {
        char[] a = new char[n];
        for(int i=0;i<n;i++) a[i] = nc();
        return a;
    }

    private static char[][] nm(int n, int m)
    {
        char[][] map = new char[n][];
        for(int i=0;i<n;i++) map[i] = ns(m);
        return map;
    }

    private static int[] na(int n)
    {
        int[] a = new int[n];
        for(int i=0;i<n;i++) a[i] = ni();
        return a;
    }

    private static long[] nal(int n)
    {
        long[] a = new long[n];
        for(int i=0;i<n;i++) a[i] = nl();
        return a;
    }
    //private void tr(Object... o) { if(o.length() > 0)System.out.println(Arrays.deepToString(o)); }
}

class FastReader{
    private boolean finished = false;

    private InputStream stream;
    private byte[] buf = new byte[1024];
    private int curChar;
    private int numChars;
    private SpaceCharFilter filter;

    public FastReader(InputStream stream){
        this.stream = stream;
    }

    public int read(){
        if (numChars == -1){
            throw new InputMismatchException ();
        }
        if (curChar >= numChars){
            curChar = 0;
            try{
                numChars = stream.read (buf);
            } catch (IOException e){
                throw new InputMismatchException ();
            }
            if (numChars <= 0){
                return -1;
            }
        }
        return buf[curChar++];
    }

    public int peek(){
        if (numChars == -1){
            return -1;
        }
        if (curChar >= numChars){
            curChar = 0;
            try{
                numChars = stream.read (buf);
            } catch (IOException e){
                return -1;
            }
            if (numChars <= 0){
                return -1;
            }
        }
        return buf[curChar];
    }

    public int nextInt(){
        int c = read ();
        while (isSpaceChar (c))
            c = read ();
        int sgn = 1;
        if (c == '-'){
            sgn = -1;
            c = read ();
        }
        int res = 0;
        do{
            if(c==','){
                c = read();
            }
            if (c < '0' || c > '9'){
                throw new InputMismatchException ();
            }
            res *= 10;
            res += c - '0';
            c = read ();
        } while (!isSpaceChar (c));
        return res * sgn;
    }

    public long nextLong(){
        int c = read ();
        while (isSpaceChar (c))
            c = read ();
        int sgn = 1;
        if (c == '-'){
            sgn = -1;
            c = read ();
        }
        long res = 0;
        do{
            if (c < '0' || c > '9'){
                throw new InputMismatchException ();
            }
            res *= 10;
            res += c - '0';
            c = read ();
        } while (!isSpaceChar (c));
        return res * sgn;
    }

    public String nextString(){
        int c = read ();
        while (isSpaceChar (c))
            c = read ();
        StringBuilder res = new StringBuilder ();
        do{
            res.appendCodePoint (c);
            c = read ();
        } while (!isSpaceChar (c));
        return res.toString ();
    }

    public boolean isSpaceChar(int c){
        if (filter != null){
            return filter.isSpaceChar (c);
        }
        return isWhitespace (c);
    }

    public static boolean isWhitespace(int c){
        return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
    }

    private String readLine0(){
        StringBuilder buf = new StringBuilder ();
        int c = read ();
        while (c != '\n' && c != -1){
            if (c != '\r'){
                buf.appendCodePoint (c);
            }
            c = read ();
        }
        return buf.toString ();
    }

    public String nextLine(){
        String s = readLine0 ();
        while (s.trim ().length () == 0)
            s = readLine0 ();
        return s;
    }

    public String nextLine(boolean ignoreEmptyLines){
        if (ignoreEmptyLines){
            return nextLine ();
        }else{
            return readLine0 ();
        }
    }

    public BigInteger nextBigInteger(){
        try{
            return new BigInteger (nextString());
        } catch (NumberFormatException e){
            throw new InputMismatchException ();
        }
    }

    public char nextCharacter(){
        int c = read ();
        while (isSpaceChar (c))
            c = read ();
        return (char) c;
    }

    public double nextDouble(){
        int c = read ();
        while (isSpaceChar (c))
            c = read ();
        int sgn = 1;
        if (c == '-'){
            sgn = -1;
            c = read ();
        }
        double res = 0;
        while (!isSpaceChar (c) && c != '.'){
            if (c == 'e' || c == 'E'){
                return res * Math.pow (10, nextInt ());
            }
            if (c < '0' || c > '9'){
                throw new InputMismatchException ();
            }
            res *= 10;
            res += c - '0';
            c = read ();
        }
        if (c == '.'){
            c = read ();
            double m = 1;
            while (!isSpaceChar (c)){
                if (c == 'e' || c == 'E'){
                    return res * Math.pow (10, nextInt ());
                }
                if (c < '0' || c > '9'){
                    throw new InputMismatchException ();
                }
                m /= 10;
                res += (c - '0') * m;
                c = read ();
            }
        }
        return res * sgn;
    }

    public boolean isExhausted(){
        int value;
        while (isSpaceChar (value = peek ()) && value != -1)
            read ();
        return value == -1;
    }

    public String next(){
        return nextString();
    }

    public SpaceCharFilter getFilter(){
        return filter;
    }

    public void setFilter(SpaceCharFilter filter){
        this.filter = filter;
    }

    public interface SpaceCharFilter{
        public boolean isSpaceChar(int ch);
    }
}