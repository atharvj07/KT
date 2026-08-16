import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main {
	private	static	BufferedReader	br = null;

	static {
		br = new BufferedReader(new InputStreamReader(System.in));
	}
 
    /**
     * @param args
     */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int	map[] = new int[2001];
		int	num   = -1;

		for(int a = 0; a <= 1000; a++) {
			for(int b = 0; b <= 1000; b++) {
				// 0から2000までの組み合わせをカウント
				map[a+b]++;
			}
		}

		while((num = parseNum()) != -1) {
			long	cnt = 0;
			for(int a = 0; a <= 2000; a++) {
				if (a > num) {
					// 数値Aが目的値を超えたらこれ以上カウントしない
					break;
				}
				for(int b = 0; b <= 2000; b++) {
					if (a + b == num) {
						cnt += (long)map[a]*(long)map[b];
					} else if (a + b > num || num - a > 2000) {
						// 合計が目的値を超えたらこれ以上カウントしない
						// 数値Aに2000を足しても目的値に届かない場合はこれ以上カウントしない
						break;
					}
				}
			}

			System.out.println(cnt);
		}

	}

	private static int parseNum() {
		int		param = -1;
		String	strin = null;

		if ((strin = parseStdin()) != null) {
			param = Integer.parseInt(strin);
		}
 
		return param;
	}

	private static String parseStdin() {
        String  stdin = null;
        
        try {
        	String  tmp = br.readLine();
        	if (tmp != null) {
            	if (!tmp.isEmpty()) {
            		stdin = tmp;
            	}
        	}
        }
        catch (IOException e) {}
 
        return stdin;
	}
}