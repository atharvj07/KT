import java.util.*;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
    
		// 文字列の入力
		ArrayList<String> list = new ArrayList<>();
        for(int i = 0; i < 4; i++) {
          list.add(sc.next());
        }
    
		// 出力
		System.out.println(list.contains("1") 
                           && list.contains("9")
                           && list.contains("7")
                           && list.contains("4") ? "YES" : "NO");
	}
}