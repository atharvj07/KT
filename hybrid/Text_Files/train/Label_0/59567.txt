
import java.awt.geom.Point2D;
import java.io.*;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.Deque;
import java.util.HashMap;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.PriorityQueue;
import java.util.Scanner;
public class Main {
	static boolean[] ans;
	public static void main(String[] args) {
		
		FastScanner sc = new FastScanner();
		PrintWriter out = new PrintWriter(System.out);
		while(sc.hasNext()) {
			char[] list = sc.next().toCharArray();
			int [] sum  = new int[9];
			
			for(int i = 0; i < list.length; i++) {
				sum[list[i] - '0' - 1]++;
			}
			
			ans = new boolean[9];
			
			for(int i = 0; i < 9; i++) {
				int[] cpy = Arrays.copyOf(sum, sum.length);
				cpy[i]++;
				if(cpy[i] > 4) continue;
				if(solv(cpy,0)) {
					ans[i] = true;
				}
			}
			boolean p = true;
			for(int i = 0; i < 9; i++) {
				if(ans[i] && p) {
					out.print((i+1));
					p = false;
				}
				else if(ans[i]) {
					String a = " " + String.valueOf(i+1);
					out.print(" " + (i+1));
				}
			}
			if(p) {
				out.print("0");
			}
			out.println();
		}
		out.flush();
	}
	
	static boolean solv(int[] a, int b) {
		if(b == 4) {
			for(int i = 0; i < 9; i++) {
				if(a[i] == 2) return true;
			}
		}
		boolean ret = false;
		for(int i = 0; i < 9; i++) {
			if(a[i] >= 3) {
				int[] cpy = Arrays.copyOf(a, a.length);
				cpy[i] -= 3;
				if(solv(cpy,b+1)) {
					return true;
				}
			}
		}
		
		for(int i = 0; i < 7; i++) {
			if(a[i] > 0 && a[i+1] > 0 && a[i+2] > 0) {
				int[] cpy = Arrays.copyOf(a, a.length);
				cpy[i]--;
				cpy[i+1]--;
				cpy[i+2]--;
				
				if(solv(cpy,b+1)) {
					return true;
				}
			}
		}
		return false;
		
	}

}
		
//------------------------------//
//-----------//
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