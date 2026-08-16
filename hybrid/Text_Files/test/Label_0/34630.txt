import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.InputMismatchException;
import java.util.NoSuchElementException;

public class Main{

	static PrintWriter out;
	static InputReader ir;
	static int[][] d={{1,0,0},{0,1,0},{0,0,1},{1,1,0},{1,-1,0},{1,0,1},{1,0,-1},{0,1,1},{0,1,-1},{1,1,1},{1,1,-1},{1,-1,1},{1,-1,-1}};

	static void solve(){
		for(;;){
			int n=ir.nextInt();
			int m=ir.nextInt();
			int p=ir.nextInt();
			if(n==0) break;
			int[] x=new int[p];
			int[] y=new int[p];
			for(int i=0;i<p;i++){
				x[i]=ir.nextInt()-1;
				y[i]=ir.nextInt()-1;
			}
			int[][][] cl=new int[n][n][n];
			int[][] ac=new int[n][n];
			int z;
			outer:
			for(int i=0;i<p;i++){
				z=ac[x[i]][y[i]];
				cl[x[i]][y[i]][ac[x[i]][y[i]]++]=(int)Math.pow(-1, i);
				for(int j=0;j<d.length;j++){
					int seq=1;
					for(int k=1;;k++){
						int nx=x[i]+k*d[j][0];
						int ny=y[i]+k*d[j][1];
						int nz=z+k*d[j][2];
						if(!(check(nx,ny,nz,n)&&cl[nx][ny][nz]==cl[x[i]][y[i]][z]))
							break;
						seq++;
					}
					for(int k=1;;k++){
						int nx=x[i]-k*d[j][0];
						int ny=y[i]-k*d[j][1];
						int nz=z-k*d[j][2];
						if(!(check(nx,ny,nz,n)&&cl[nx][ny][nz]==cl[x[i]][y[i]][z]))
							break;
						seq++;
					}
					if(seq>=m){
						out.println((i%2==0?"Black":"White")+" "+Integer.toString(i+1));
						break outer;
					}
				}
				if(i==p-1)
					out.println("Draw");
			}
		}
	}

	static boolean check(int x,int y,int z,int n){
		return x>=0&&y>=0&&z>=0&&x<n&&y<n&&z<n;
	}

	public static void main(String[] args) throws Exception{
		ir=new InputReader(System.in);
		out=new PrintWriter(System.out);
		solve();
		out.flush();
	}

	static class InputReader {

		private InputStream in;
		private byte[] buffer=new byte[1024];
		private int curbuf;
		private int lenbuf;

		public InputReader(InputStream in) {this.in=in; this.curbuf=this.lenbuf=0;}

		public boolean hasNextByte() {
			if(curbuf>=lenbuf){
				curbuf= 0;
				try{
					lenbuf=in.read(buffer);
				}catch(IOException e) {
					throw new InputMismatchException();
				}
				if(lenbuf<=0) return false;
			}
			return true;
		}

		private int readByte(){if(hasNextByte()) return buffer[curbuf++]; else return -1;}

		private boolean isSpaceChar(int c){return !(c>=33&&c<=126);}

		private void skip(){while(hasNextByte()&&isSpaceChar(buffer[curbuf])) curbuf++;}

		public boolean hasNext(){skip(); return hasNextByte();}

		public String next(){
			if(!hasNext()) throw new NoSuchElementException();
			StringBuilder sb=new StringBuilder();
			int b=readByte();
			while(!isSpaceChar(b)){
				sb.appendCodePoint(b);
				b=readByte();
			}
			return sb.toString();
		}

		public int nextInt() {
			if(!hasNext()) throw new NoSuchElementException();
			int c=readByte();
			while (isSpaceChar(c)) c=readByte();
			boolean minus=false;
			if (c=='-') {
				minus=true;
				c=readByte();
			}
			int res=0;
			do{
				if(c<'0'||c>'9') throw new InputMismatchException();
				res=res*10+c-'0';
				c=readByte();
			}while(!isSpaceChar(c));
			return (minus)?-res:res;
		}

		public long nextLong() {
			if(!hasNext()) throw new NoSuchElementException();
			int c=readByte();
			while (isSpaceChar(c)) c=readByte();
			boolean minus=false;
			if (c=='-') {
				minus=true;
				c=readByte();
			}
			long res = 0;
			do{
				if(c<'0'||c>'9') throw new InputMismatchException();
				res=res*10+c-'0';
				c=readByte();
			}while(!isSpaceChar(c));
			return (minus)?-res:res;
		}

		public double nextDouble(){return Double.parseDouble(next());}

		public int[] nextIntArray(int n){
			int[] a=new int[n];
			for(int i=0;i<n;i++) a[i]=nextInt();
			return a;
		}

		public long[] nextLongArray(int n){
			long[] a=new long[n];
			for(int i=0;i<n;i++) a[i]=nextLong();
			return a;
		}

		public char[][] nextCharMap(int n,int m){
			char[][] map=new char[n][m];
			for(int i=0;i<n;i++) map[i]=next().toCharArray();
			return map;
		}
	}
}