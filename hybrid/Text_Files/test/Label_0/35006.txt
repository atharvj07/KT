


import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintStream;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

/**
 * @author Ivan Pryvalov (ivan.pryvalov@gmail.com)
 */
public class Codeforces_Round86_Div2_D implements Runnable{
	
	int N;
	//static int MOD = 1000000007;
	static long MOD = 0xFfffFfffFfffL;

	/*
	 * scanner.nextInt()
	 * new ByteScanner(scanner.nextLineAsArray()).nextInt();
	 */
	private void solve() throws IOException {
		
		scanner.readToken((byte)0x21);
		char[] t = new char[scanner.totalBytes];
		for (int i = 0; i < t.length; i++) {
			t[i] = (char) scanner.byteBuf[i];
		}
		
		//String tStr = scanner.nextToken();
		//String str1 = scanner.nextToken();
		//String str2 = scanner.nextToken();
		
		scanner.readToken((byte)0x21);
		char[] s1 = new char[scanner.totalBytes];
		for (int i = 0; i < s1.length; i++) {
			s1[i] = (char) scanner.byteBuf[i];
		}
		
		scanner.readToken((byte)0x21);
		char[] s2 = new char[scanner.totalBytes];
		for (int i = 0; i < s2.length; i++) {
			s2[i] = (char) scanner.byteBuf[i];
		}
		
		N = t.length;
		
		if (s1.length > t.length || s2.length > t.length){
			out.println(0);
			return;
		}
		
		long s1hash = hashcode(s1);
		long s2hash = hashcode(s2);
		
		long[][] hh = new long[N+1][];
		hh[1] = createHash(t, 1);
		for (int i = 2; i <= N; i++) {
			hh[i] = new long[hh[i-1].length-1];
			for (int j = 0; j < hh[i].length; j++) {
				hh[i][j] = ((hh[i-1][j] * 31L + t[j+i-1]) & MOD); 				
			}
		}
		
		int diff = Math.max(s1.length-s2.length,0);
		
		
		int answer = 0;
		for (int len = Math.max(s1.length, s2.length); len<=N; len++) {
			Set<Long> set = new HashSet<Long>();
			for (int i1 = 0; i1+s1.length-1 < N; i1++) {
				int i2 = i1 + len - s2.length;
				if (i2+s2.length-1 < N){
				//for (int i2 = i1 + diff; i2+s2.length-1 < N; i2++) {
					if (hh[s1.length][i1]==s1hash && hh[s2.length][i2]==s2hash){
						set.add(hh[i2+s2.length-i1][i1]);
					}
				//}			
				}
			}
			answer += set.size();
		}
		
		out.println(answer);
	}
	
	public long hashcode(char[] s){
		long h = 0;
		for (int i = 0; i < s.length; i++) {
			h = (h*31 + s[i]) & MOD;
		}
		return h;
	}
	
	public long[] createHash(char[] t, int subSize){
		long n1 = 1;
		for (int i = 0; i < subSize-1; i++) {
			n1 = (n1 * 31) & MOD;			
		}
		long[] hash1 = new long[N-subSize+1];
		long h = 0;
		for (int i = 0; i < subSize; i++) {
			h = (h*31 + t[i]) & MOD;						
		}
		hash1[0] = (int)h;
		for (int i = 1; i < N-subSize+1; i++) {
			h = hash1[i-1] - ((n1*t[i-1]) % MOD);
			
			if (h<0) 
				h += MOD;
			if (h<0)
				throw new RuntimeException();
			
			h = (h*31 + t[i+subSize-1]) & MOD;
			hash1[i] = h;
		}
		return hash1;
	}

	/////////////////////////////////////////////////
	final int BUF_SIZE = 1024 * 1024 * 2;//important to read long-string tokens properly
	final int INPUT_BUFFER_SIZE = 1024 * 1024 * 2 ;
	final int BUF_SIZE_INPUT = 1024;
	
	final int BUF_SIZE_OUT = 1024;
	
	boolean inputFromFile = false;
	String filenamePrefix = "A-small-attempt0";
	String inSuffix = ".in";
	String outSuffix = ".out";
	
	//InputStream bis;
	//OutputStream bos;
	PrintStream out;
	ByteScanner scanner;
	ByteWriter writer;
	
	@Override
	public void run() {
		try{
			InputStream bis = null;
			OutputStream bos = null;
			//PrintStream out = null;
			if (inputFromFile){
				File baseFile = new File(getClass().getResource("/").getFile());
				bis = new BufferedInputStream(
						new FileInputStream(new File(
								baseFile, filenamePrefix+inSuffix)),
								INPUT_BUFFER_SIZE);
				bos = new BufferedOutputStream(
						new FileOutputStream(
								new File(baseFile, filenamePrefix+outSuffix)));
				out = new PrintStream(bos);
			}else{
				bis = new BufferedInputStream(System.in, INPUT_BUFFER_SIZE);
				bos = new BufferedOutputStream(System.out);
				out = new PrintStream(bos);
			}
			scanner = new ByteScanner(bis, BUF_SIZE_INPUT, BUF_SIZE);
			writer = new ByteWriter(bos, BUF_SIZE_OUT);
			
			solve();
			out.flush();
		}catch (Exception e) {
			e.printStackTrace();
			System.exit(1);
		}
	}
	
	public interface Constants{
		final static byte ZERO = '0';//48 or 0x30
		final static byte NINE = '9';
		final static byte SPACEBAR = ' '; //32 or 0x20
		final static byte MINUS = '-'; //45 or 0x2d	
		
		final static char FLOAT_POINT = '.';
	}
	
	public static class EofException extends IOException{
	}
	
	public static class ByteWriter implements Constants {
		
		int bufSize = 1024;
		byte[] byteBuf = new byte[bufSize];
		OutputStream os;
		
		public ByteWriter(OutputStream os, int bufSize){
			this.os = os;
			this.bufSize = bufSize;
		}
		
		public void writeInt(int num) throws IOException{
	         int byteWriteOffset = byteBuf.length;
	         if (num==0){
	        	 byteBuf[--byteWriteOffset] = ZERO;
	         }else{
	        	 int numAbs = Math.abs(num);
	        	 while (numAbs>0){
	        		 byteBuf[--byteWriteOffset] = (byte)((numAbs % 10) + ZERO);
	        		 numAbs /= 10;
	        	 }
	        	 if (num<0)
	        		 byteBuf[--byteWriteOffset] = MINUS;
	         }
	         os.write(byteBuf, byteWriteOffset, byteBuf.length - byteWriteOffset);
		}
		
		/**
		 * Please ensure ar.length <= byteBuf.length!
		 * 
		 * @param ar
		 * @throws IOException
		 */
		public void writeByteAr(byte[] ar) throws IOException{
			for (int i = 0; i < ar.length; i++) {
				byteBuf[i] = ar[i];
			}
			os.write(byteBuf,0,ar.length);
		}
		
		public void writeSpaceBar() throws IOException{
			byteBuf[0] = SPACEBAR;
			os.write(byteBuf,0,1);
		}
		
	}
	
	public static class ByteScanner implements Constants{
		
		InputStream is;
		
		public ByteScanner(InputStream is, int bufSizeInput, int bufSize){
			this.is = is;
			this.bufSizeInput = bufSizeInput;
			this.bufSize = bufSize;
			
			byteBufInput = new byte[this.bufSizeInput];
			byteBuf = new byte[this.bufSize];
		}
		
		public ByteScanner(byte[] data){
			byteBufInput = data;
			bufSizeInput = data.length;
			bufSize = data.length;
			byteBuf = new byte[bufSize];
			byteRead = data.length;
			bytePos = 0;
		}
		
		private int bufSizeInput;
		private int bufSize;
		
		byte[] byteBufInput;
		byte by=-1;
		int byteRead=-1;
		int bytePos=-1;

		byte[] byteBuf;
		int totalBytes;
		
		boolean eofMet = false;
		
		private byte nextByte() throws IOException{
			
			if (bytePos<0 || bytePos>=byteRead){
				byteRead = is==null? -1: is.read(byteBufInput);
				bytePos=0;
				if (byteRead<0){
					byteBufInput[bytePos]=-1;//!!!
					if (eofMet)
						throw new EofException();
					eofMet = true;
				}
			}
			return byteBufInput[bytePos++];
		}
		
		/**
		 * Returns next meaningful character as a byte.<br>
		 * 
		 * @return
		 * @throws IOException
		 */
		public byte nextChar() throws IOException{
			while ((by=nextByte())<=0x20);
			return by;
		}
		
		/**
		 * Returns next meaningful character OR space as a byte.<br>
		 * 
		 * @return
		 * @throws IOException
		 */
		public byte nextCharOrSpacebar() throws IOException{
			while ((by=nextByte())<0x20);
			return by;
		}
		
	    /**
	     * Reads line.
	     * 
	     * @return
	     * @throws IOException
	     */
	    public String nextLine() throws IOException {
            readToken((byte)0x20);
            return new String(byteBuf,0,totalBytes);
	    }
	    
	    public byte[] nextLineAsArray() throws IOException {
            readToken((byte)0x20);
            byte[] out = new byte[totalBytes];
            System.arraycopy(byteBuf, 0, out, 0, totalBytes);
            return out;
	    }
	    
		
	    /**
	     * Reads token. Spacebar is separator char.
	     * 
	     * @return
	     * @throws IOException
	     */
	    public String nextToken() throws IOException {
            readToken((byte)0x21);
            return new String(byteBuf,0,totalBytes);
	    }
	    
	    /**
	     * Spacebar is included as separator char
	     * 
	     * @throws IOException
	     */
	    private void readToken() throws IOException {	    	
            readToken((byte)0x21);
	    }
	    
	    private void readToken(byte acceptFrom) throws IOException {
            totalBytes = 0;
            while ((by=nextByte())<acceptFrom);
            byteBuf[totalBytes++] = by;
            while ((by=nextByte())>=acceptFrom){
                byteBuf[totalBytes++] = by;
            }
	    }
		
	    public int nextInt() throws IOException{
			readToken();
			int num=0, i=0;
			boolean sign=false;
			if (byteBuf[i]==MINUS){
				sign = true;
				i++;
			}
			for (; i<totalBytes; i++){
				num*=10;
				num+=byteBuf[i]-ZERO;
			}
			return sign?-num:num;
		}
		
		public long nextLong() throws IOException{
			readToken();
			long num=0;
			int i=0;
			boolean sign=false;
			if (byteBuf[i]==MINUS){
				sign = true;
				i++;
			}
			for (; i<totalBytes; i++){
				num*=10;
				num+=byteBuf[i]-ZERO;
			}
			return sign?-num:num;
		}
		
		/*
		//TODO test Unix/Windows formats
		public void toNextLine() throws IOException{
			while ((ch=nextChar())!='\n');
		}
		*/
		
		public double nextDouble() throws IOException{
			readToken();
			char[] token = new char[totalBytes];
			for (int i = 0; i < totalBytes; i++) {
				token[i] = (char)byteBuf[i];
			}
			return Double.parseDouble(new String(token));
		}
	    
	}
	
	public static void main(String[] args) {
		new Codeforces_Round86_Div2_D().run();
	}
	
}
