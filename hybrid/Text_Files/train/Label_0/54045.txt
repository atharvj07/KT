import java.io.*;
import java.util.*;
 
public class Main {
	

	void howUdoin() {
		
		int n = inpi();
        int k = inpi();
        int p = inpi();
        int[] a = new int[n];
        int[] b = new int[k];
        for (int i = 0; i < n; i++){
        	a[i] = inpi();
        }
        for (int j = 0; j < k; j++) {
        	b[j] = inpi();
        }
        Arrays.sort(a);
        Arrays.sort(b);
        long ans = Long.MAX_VALUE;
        for (int i = 0; i+n <= k ; i++) {
            long temp = 0;
            for (int j = 0; j < n; j++) {
                temp = Math.max(temp, Math.abs(a[j] - b[j + i]) + Math.abs(b[j + i] - p));
            }
           ans = Math.min(ans,temp);
        }
        System.out.println(ans);
			
		
	}
 
	InputStream obj;
	PrintWriter out;
	String check = "";
 
	public static void main(String[] args) throws IOException {
		new Main().main1();
	}
 
	void main1() throws IOException {
		out = new PrintWriter(System.out);
		obj = check.isEmpty() ? System.in : new ByteArrayInputStream(check.getBytes());
		howUdoin();
		out.flush();
		out.close();
	}
	byte inbuffer[] = new byte[1024];
	int lenbuffer = 0, ptrbuffer = 0;
 
	int readByte() {
		if (lenbuffer == -1) {
			throw new InputMismatchException();
		}
		if (ptrbuffer >= lenbuffer) {
			ptrbuffer = 0;
			try {
				lenbuffer = obj.read(inbuffer);
			} catch (IOException e) {
				throw new InputMismatchException();
			}
		}
		if (lenbuffer <= 0) {
			return -1;
		}
		return inbuffer[ptrbuffer++];
	}
 
	boolean isSpaceChar(int c) {
		return (!(c >= 33 && c <= 126));
	}
 
	int skip() {
		int b;
		while ((b = readByte()) != -1 && isSpaceChar(b));
		return b;
	}
 
	String inps() {
		int b = skip();
		StringBuilder sb = new StringBuilder();
		while (!(isSpaceChar(b))) {
			sb.appendCodePoint(b);
			b = readByte();
		}
		return sb.toString();
	}
	String inpsl() {
		int b = skip();
		StringBuilder sb = new StringBuilder();
		while (b!='\n') {
			sb.appendCodePoint(b);
			b = readByte();
		}
		return sb.toString();
	}
 
	int inpi() {
		int num = 0, b;
		boolean minus = false;
		while ((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-'));
		if (b == '-') {
			minus = true;
			b = readByte();
		}
		while (true) {
			if (b >= '0' && b <= '9') {
				num = num * 10 + (b - '0');
			} else {
				return minus ? -num : num;
			}
			b = readByte();
		}
	}
 
	long inpl() {
		long num = 0;
		int b;
		boolean minus = false;
		while ((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-'));
		if (b == '-') {
			minus = true;
			b = readByte();
		}
		while (true) {
			if (b >= '0' && b <= '9') {
				num = num * 10 + (b - '0');
			} else {
				return minus ? -num : num;
			}
			b = readByte();
		}
	}
 
	float inpf() {
		return Float.parseFloat(inps());
	}
 
	double inpd() {
		return Double.parseDouble(inps());
	}
 
	char inpc() {
		return (char) skip();
	}
 
	int[] inpia(int n) {
		int a[] = new int[n];
		for (int i = 0; i < n; i++) {
			a[i] = inpi();
		}
		return a;
	}
 
	long[] inpla(int n) {
		long a[] = new long[n];
		for (int i = 0; i < n; i++) {
			a[i] = inpl();
		}
		return a;
	}
 
	String[] inpsa(int n) {
		String a[] = new String[n];
		for (int i = 0; i < n; i++) {
			a[i] = inps();
		}
		return a;
	}
	
}