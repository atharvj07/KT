import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;


public class Main {

	public static void main(String[] args) {
		Main main = new Main();
		main.teamFormationMake();
		return;
	}
	
	private void teamFormationMake() {
		
		BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in)); //標準入力
		
		try {
			
			String inputStr = bufferedReader.readLine();
			int yearNum = Integer.parseInt(inputStr); //入力される年数
			LinkedList<LinkedList<Integer>> programmerList = new LinkedList<LinkedList<Integer>>(); //プログラマのリスト
			int teamNum = 0; //年ごとのチーム数
			
			for (int i = 0; i < yearNum; i++) {
				
				String teamStr = bufferedReader.readLine();
				String[] teamStrs = teamStr.split(" ");
				programmerList.add(new LinkedList<Integer>());
				
				for (int j = 0; j < teamStrs.length; j++) {
					programmerList.get(i).add(Integer.parseInt(teamStrs[j]));
				}
			}
			
			for (int i = 0; i < yearNum; i++) {
				
				int c = programmerList.get(i).get(0);
				int a = programmerList.get(i).get(1);
				int n = programmerList.get(i).get(2);
				
				while(true) {
					
					if (c >= 1 && a >= 1 && n >= 1) {
						teamNum++;
						c--;
						a--;
						n--;
					} else if (c >= 2 && a >= 1) {
						teamNum++;
						c = c - 2;
						a--;
					} else if (c >= 3) {
						teamNum++;
						c = c - 3;
					} else {
						break;
					}
					
				}
				
				System.out.println(teamNum);
				
				teamNum = 0;
			}
			
		} catch (IOException e) {
			// TODO 自動生成された catch ブロック
			e.printStackTrace();
		}
	}
}