import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {

	public static final int BIG_NUM = 2000000000;
	public static final int MOD = 1000000007;
	public static final long HUGE_NUM = 99999999999999999L;
	public static final double EPS = 0.000000001;



	@SuppressWarnings("unchecked")
	public static void main(String[] args) {

		//BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Scanner scanner = new Scanner(System.in);

		int N = scanner.nextInt();

		Boolean dp[][][] = new Boolean[N][N][10];

		for(int left = 0; left < N; left++){
			for(int right = left; right < N; right++){
				for(int i = 0; i < 10; i++){

					dp[left][right][i] = false;
				}
			}
		}

		int tmp;

		for(int loc = 0; loc < N; loc++){

			tmp = scanner.nextInt();
			dp[loc][loc][tmp] = true;
		}

		for(int length = 2; length <= N; length++){
			for(int left = 0; left+length <= N; left++){
				int right = left+length-1;

				for(int mid = left; mid <= right-1; mid++){
					for(int num = 0; num <= 9; num++){

						//その区間を消せるか
						if((dp[left][mid][0] == true && dp[mid+1][right][0] == true) || //消え&消え
								(dp[left][mid][num] == true && dp[mid+1][right][num] == true)){ //2個以上の同じ数字

							dp[left][right][0] = true;
						}

						if(num == 0)continue;

						//その区間をnumだけにできるか(同じ数字が1個だけの場合あり)
						if((dp[left][mid][0] == true && dp[mid+1][right][num] == true) ||
								(dp[left][mid][num] == true && dp[mid+1][right][0] == true) ||
								(dp[left][mid][num] == true && dp[mid+1][right][num] == true)){

							dp[left][right][num] = true;
						}
					}
				}
			}
		}

		if(dp[0][N-1][0]){

			System.out.println("yes");

		}else{

			System.out.println("no");
		}

	}
}

class UTIL{

	//最大公約数
	public static long gcd(long x,long y){

		x = Math.abs(x);
		y = Math.abs(y);

		if(x < y){

			long tmp = y;
			y = x;
			x = tmp;
		}

		if(y == 0){

			return x;
		}else{

			return gcd(y,x%y);
		}
	}

	//最小公倍数
	public static long lcm(long x,long y){

		return (x*y)/gcd(x,y);
	}

	//String→intへ変換
    public static int getNUM(String tmp_str){

        return Integer.parseInt(tmp_str);
    }

    //文字が半角数字か判定する関数
    public static boolean isNumber(String tmp_str){

        if(tmp_str == null || tmp_str.length() == 0){

            return false;
        }

        Pattern pattern = Pattern.compile("\\A[0-9]+\\z");
        Matcher matcher = pattern.matcher(tmp_str);
        return matcher.matches();
    }
}
