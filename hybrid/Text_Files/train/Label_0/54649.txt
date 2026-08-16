import java.util.Scanner;

//UTF-8
public class Main{

	String[][] p = {{"0xxxxxxx"}, 
			{"110yyyyx", "10xxxxxx"},
			{"1110yyyy", "10yxxxxx", "10xxxxxx"},
			{"11110yyy", "10yyxxxx", "10xxxxxx", "10xxxxxx"}
	};

	void run(){
		Scanner sc = new Scanner(System.in);
		int MOD = 1000000;
		for(;;){
			int n = sc.nextInt();
			if(n==0)break;
			char[][] s = new char[n][8];
			for(int i=0;i<n;i++)s[i]=sc.next().toCharArray();
			long[][] dp = new long[n+1][4];
			dp[n][0] = 1;
			for(int i=n-1;i>=0;i--)for(int L=0;L<4;L++){
				if(n<=i+L)continue;
				boolean ok = true;
				int ys = 0, xs = 0, y1 = 0;
				for(int j=0;j<=L;j++)for(int k=0;k<8;k++){
					char ch = p[L][j].charAt(k);
					if(ch=='0'){
						if(s[i+j][k]=='1')ok = false;
					}
					if(ch=='1'){
						if(s[i+j][k]=='0')ok = false;
					}
					if(ch=='x'){
						if(s[i+j][k]=='x')xs++;
					}
					if(ch=='y'){
						if(s[i+j][k]=='1')y1++;
						if(s[i+j][k]=='x')ys++;
					}
				}
				if(ok){
					long res = (1L<<xs)%MOD;
					if(0<L){
						if(y1==0){
							res = (res*((1<<ys)-1))%MOD;
						}
						else{
							res = (res*(1<<ys))%MOD;
						}
					}
					for(int j=0;j<4;j++){
						dp[i][L] = (dp[i][L]+res*dp[i+L+1][j])%MOD;
					}
				}
				else dp[i][L] = 0;
			}
			long res = 0;
			for(int j=0;j<4;j++)res+=dp[0][j];
			System.out.println(res%MOD);
		}
	}

	public static void main(String[] args) {
		new Main().run();
	}
}