import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.InputMismatchException;
import java.util.PriorityQueue;


public class CF {
	static int cmp;
	public static void main(String[] args) {
		FasterScanner sc = new FasterScanner();
		PrintWriter out = new PrintWriter(System.out);
		int H = sc.nextInt();
		int W = sc.nextInt();
		int X = sc.nextInt()%4;
		int Y = sc.nextInt()%2;
		int Z = sc.nextInt()%4;
		int Q = sc.nextInt();
		while(Q-->0){
			int xx = sc.nextInt()-1;
			int yy = sc.nextInt()-1;
			int[] pos = {yy,xx};
			int ch = H;
			int cw = W;
			for(int a=0;a<X;a++){
				pos = clock(pos,ch,cw);
				ch^=cw;
				cw^=ch;
				ch^=cw;
			}
			for(int a=0;a<Y;a++)
				pos = horiz(pos,ch,cw);
			for(int a=0;a<Z;a++){
				pos = counter(pos,ch,cw);
				ch^=cw;
				cw^=ch;
				ch^=cw;
			}
			pos[0]++;
			pos[1]++;
			out.println(pos[1]+" "+pos[0]);
		}
		out.close();
	}
	

	private static int[] clock(int[] pos, int h, int w) {
		return new int[] {h-pos[1]-1,pos[0]};
	}


	private static int[] horiz(int[] pos, int h, int w) {
		return new int[] {w-pos[0]-1,pos[1]};
	}


	private static int[] counter(int[] pos, int h, int w) {
		return new int[] {pos[1], w-pos[0]-1};
	}


	static class FasterScanner{
		private InputStream stream;
		private byte[] buf = new byte[1024];
		private int curChar;
		private int numChars;
		
		public FasterScanner(){
			stream = System.in;
			//stream = new FileInputStream(new File("dec.in"));

		}
		int read(){
			if(numChars==-1)
				throw new InputMismatchException();
			if(curChar>=numChars){
				curChar = 0;
				try{
					numChars = stream.read(buf);
				} catch (IOException e){
					throw new InputMismatchException();
				}
				if(numChars <= 0)
					return -1;
			}
			return buf[curChar++];
		}
		
		boolean isSpaceChar(int c){
			return c==' '||c=='\n'||c=='\r'||c=='\t'||c==-1;
		}
		boolean isEndline(int c){
			return c=='\n'||c=='\r'||c==-1;
		}
		int nextInt(){
			return Integer.parseInt(next());
		}
		long nextLong(){
			return Long.parseLong(next());
		}
		double nextDouble(){
			return Double.parseDouble(next());
		}
		String next(){
			int c = read();
			while(isSpaceChar(c))
				c=read();
			StringBuilder res = new StringBuilder();
			do{
				res.appendCodePoint(c);
				c=read();
			} while(!isSpaceChar(c));
			return res.toString();
		}
		String nextLine(){
			int c = read();
			while(isEndline(c))
				c=read();
			StringBuilder res = new StringBuilder();
			do{
				res.appendCodePoint(c);
				c = read();
			}while(!isEndline(c));
			return res.toString();
		}
		
	}

}