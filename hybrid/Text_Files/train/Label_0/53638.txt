import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		// TODO 自動生成されたメソッド・スタブ
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String[] tmpArray = br.readLine().split(" ");

		int n = Integer.parseInt(tmpArray[0]);
		int h = Integer.parseInt(tmpArray[1]);
		int w = Integer.parseInt(tmpArray[2]);

		int input[] = new int[n];
		tmpArray = br.readLine().split(" ");

		for(int i = 0; i < n;i++){
			input[i] = Integer.parseInt(tmpArray[i]);
		}

		int x[] = new int[n];
		//それぞれのpaneの左の座標を確定させる
		for(int i = 0; i < n; i++){
			if(i%2 == 0){
				x[i] = i*w + input[i];
			}
			else {
				x[i] = i*w - input[i];
			}
		}

		boolean closed[] = new boolean[n*w];
		for(int i = 0; i < n; i++){
			for(int j = 0; j < w; j++){
				closed[x[i] + j] = true;
			}
		}

		int result = 0;
		for(int i = 0; i < closed.length; i++){
			if(!closed[i]){
				result += h;
			}
		}

		System.out.println(result);
	}

}

