
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.NoSuchElementException;
import java.util.Scanner;
public class Main {
	static PrintWriter out = new PrintWriter(System.out);
	static Scanner stdIn = new Scanner(System.in);
	static FastScanner sc = new FastScanner();

	
	public static void main(String[] args) {
		while(true) {
			int m = sc.nextInt();
			int n = sc.nextInt();
			if(m == 0 && n == 0) break;
			int[] a = new int[n];
			for(int i = 0; i < n; i++) {
				a[i] = sc.nextInt();
			}
			
			ArrayList<ArrayDeque<Data>> queue = new ArrayList<ArrayDeque<Data>>();
			int[] status = new int[m];
			for(int i = 0; i < m; i++) {
				queue.add(new ArrayDeque<Data>());
			}
			
			for(int i = 0; i < n; i++) {
				status[0] += a[i];
				queue.get(0).add(new Data(i,a[i]));
			}
			int min = Integer.MAX_VALUE;
			while(true) {
				int max = 0;
				int id = 0;
				for(int i = 0; i < m; i++) {
					if(max < status[i]) {
						max = status[i];
						id = i;
					}
				}
				min = Math.min(min, max);
				
				if(id == m-1) break;
				
				Data pp = queue.get(id).poll();
				queue.get(id+1).add(pp);
				status[id] -= pp.a;
				status[id+1] += pp.a;
				
			}
			
			out.println(min);
			
			
			
		}
		out.flush();
	}
	
	static class Data {
		int id;
		int a;
		Data(int c, int d) {
			id = c;
			a = d;
		}
	}

}

class FastScanner {
    private final InputStream in = System.in;
    private final byte[] buffer = new byte[1024];
    private int ptr = 0;
    private int buflen = 0;
    private boolean hasNextByte() {
        if (ptr < buflen) {
            return true;
        }else{
            ptr = 0;
            try {
                buflen = in.read(buffer);
            } catch (IOException e) {
                e.printStackTrace();
            }
            if (buflen <= 0) {
                return false;
            }
        }
        return true;
    }
    private int readByte() { if (hasNextByte()) return buffer[ptr++]; else return -1;}
    private static boolean isPrintableChar(int c) { return 33 <= c && c <= 126;}
    private void skipUnprintable() { while(hasNextByte() && !isPrintableChar(buffer[ptr])) ptr++;}
    public boolean hasNext() { skipUnprintable(); return hasNextByte();}
    public String next() {
        if (!hasNext()) throw new NoSuchElementException();
        StringBuilder sb = new StringBuilder();
        int b = readByte();
        while(isPrintableChar(b)) {
            sb.appendCodePoint(b);
            b = readByte();
        }
        return sb.toString();
    }
    public long nextLong() {
        if (!hasNext()) throw new NoSuchElementException();
        long n = 0;
        boolean minus = false;
        int b = readByte();
        if (b == '-') {
            minus = true;
            b = readByte();
        }
        if (b < '0' || '9' < b) {
            throw new NumberFormatException();
        }
        while(true){
            if ('0' <= b && b <= '9') {
                n *= 10;
                n += b - '0';
            }else if(b == -1 || !isPrintableChar(b)){
                return minus ? -n : n;
            }else{
                throw new NumberFormatException();
            }
            b = readByte();
        }
    }
     
    public int nextInt() {
        return (int)nextLong();
    }
     
    public double nextDouble() {
        return Double.parseDouble(next());
    }
     
 
}