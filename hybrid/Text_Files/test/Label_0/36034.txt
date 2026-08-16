import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.NoSuchElementException;
public class Main implements Runnable{
	char[] S;
	int K,N;

	int[][] dp1,dp2;

	public int max(int a,int b){
		if(Math.abs(a) < Math.abs(b)){
			return b;
		}
		return a;
	}

    public void solve() {
    	S = next().toCharArray();
    	K = nextInt();
    	N = S.length;

    	dp1 = new int[N+1][K+1];
    	dp2 = new int[N+1][K+1];



    	//???DP
    	for(int i = 0;i < N;i++){
    		for(int j = 0;j < K+1;j++){
    			if(S[i]=='U'){
    				if((j&1) == 0)dp1[i+1][j] = max(dp1[i+1][j],dp1[i][j]+1);
    				else dp1[i+1][j] = max(dp1[i+1][j],dp1[i][j]-1);

    				if(j < K && (j+1&1) == 1){
    					dp1[i+1][j+1] = max(dp1[i+1][j+1],dp1[i][j]-1);
    				}
    				if(j < K && (j+1&1) == 0){
    					dp1[i+1][j+1] = max(dp1[i+1][j+1],dp1[i][j]+1);
    				}
    			}else if(S[i] == 'D'){
    				if((j&1) == 0)dp1[i+1][j] = max(dp1[i+1][j],dp1[i][j]-1);
    				else dp1[i+1][j] = max(dp1[i+1][j],dp1[i][j]+1);

    				if(j < K && (j+1&1) == 1){
    					dp1[i+1][j+1] = max(dp1[i+1][j+1],dp1[i][j]+1);
    				}

    				if(j < K && (j+1&1) == 0){
    					dp1[i+1][j+1] = max(dp1[i+1][j+1],dp1[i][j]-1);
    				}
    			}else{
    				dp1[i+1][j] = max(dp1[i+1][j],dp1[i][j]);
    			}
    		}
    	}

    	//?¨?DP
    	for(int i = 0;i < N;i++){
    		for(int j = 0;j < K+1;j++){
    			if(S[i]=='R'){
    				if((j&1) == 0)dp2[i+1][j] = max(dp2[i+1][j],dp2[i][j]+1);
    				else dp2[i+1][j] = max(dp2[i+1][j],dp2[i][j]-1);

    				if(j < K && (j+1&1) == 1){
    					dp2[i+1][j+1] = max(dp2[i+1][j+1],dp2[i][j]-1);
    				}
    				if(j < K && (j+1&1) == 0){
    					dp2[i+1][j+1] = max(dp2[i+1][j+1],dp2[i][j]+1);
    				}
    			}else if(S[i] == 'L'){
    				if((j&1) == 0)dp2[i+1][j] = max(dp2[i+1][j],dp2[i][j]-1);
    				else dp2[i+1][j] = max(dp2[i+1][j],dp2[i][j]+1);

    				if(j < K && (j+1&1) == 1){
    					dp2[i+1][j+1] = max(dp2[i+1][j+1],dp2[i][j]+1);
    				}

    				if(j < K && (j+1&1) == 0){
    					dp2[i+1][j+1] = max(dp2[i+1][j+1],dp2[i][j]-1);
    				}
    			}else{
    				dp2[i+1][j] = max(dp2[i+1][j],dp2[i][j]);
    			}
    		}
    	}

    	int ans = 0;

    	for(int i = 0;i <= K;i++){
    		for(int j = 0;j <= K-i;j++){
    			//out.println(dp1[N][i] + " " + dp2[N][j]);
    			ans = Math.max(ans,Math.abs(dp1[N][i]) + Math.abs(dp2[N][j]));
    		}
    	}

    	out.println(ans);
    }

    public static void main(String[] args) {
        new Thread(null,new Main(),"",64 * 1024 * 1024).start();
    }

    /* Input */
    private static final InputStream in = System.in;
    private static final PrintWriter out = new PrintWriter(System.out);
    private final byte[] buffer = new byte[2048];
    private int p = 0;
    private int buflen = 0;

    private boolean hasNextByte() {
        if (p < buflen)
            return true;
        p = 0;
        try {
            buflen = in.read(buffer);
        } catch (IOException e) {
            e.printStackTrace();
        }
        if (buflen <= 0)
            return false;
        return true;
    }

    public boolean hasNext() {
        while (hasNextByte() && !isPrint(buffer[p])) {
            p++;
        }
        return hasNextByte();
    }

    private boolean isPrint(int ch) {
        if (ch >= '!' && ch <= '~')
            return true;
        return false;
    }

    private int nextByte() {
        if (!hasNextByte())
            return -1;
        return buffer[p++];
    }

    public String next() {
        if (!hasNext())
            throw new NoSuchElementException();
        StringBuilder sb = new StringBuilder();
        int b = -1;
        while (isPrint((b = nextByte()))) {
            sb.appendCodePoint(b);
        }
        return sb.toString();
    }

    public int nextInt() {
        return Integer.parseInt(next());
    }

    public long nextLong() {
        return Long.parseLong(next());
    }

    public double nextDouble() {
        return Double.parseDouble(next());
    }

    @Override
    public void run() {
        out.flush();
        new Main().solve();
        out.close();

    }
}