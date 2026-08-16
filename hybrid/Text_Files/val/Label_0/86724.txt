
import java.util.*;
public class Main {

	public void doIt(){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		while(n-- > 0){
			int len = 8;
			char [] array = new char[len];
			String str = sc.next();
			for(int i=0; i < len; i++){
				array[i] = str.charAt(i);
			}
			Arrays.sort(array);
			//逆順の配列を作成
			char [] reverse = new char[len];
			for(int i=0 ; i < len / 2; i++){
				reverse[i] = array[len-i -1];
				reverse[len - i - 1] = array[i];
			}

			//連結する
			StringBuilder minstr = new StringBuilder();
			minstr.append(array);
			StringBuilder maxstr = new StringBuilder();
			maxstr.append(reverse);

			//整数型に直す
			int min = Integer.parseInt(minstr.toString());
			int max = Integer.parseInt(maxstr.toString());
			System.out.println(max - min);
		}

	}
	public static void main(String[] args) {
		Main obj = new Main();
		obj.doIt();

	}

}