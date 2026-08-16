import java.util.Arrays;
import java.util.Scanner;


public class Main{

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		while(true){
		String[] firstLine = s.nextLine().split(" ");
		int raw = Integer.parseInt(firstLine[0]);
		int column = Integer.parseInt(firstLine[1]);
		if(raw == 0 && column == 0)
			return;
		int[][] senbeiyakiki = new int[raw][column];
		for(int i=0 ; i<raw ; i++) {
			String[] line = s.nextLine().split(" ");
			for(int j=0 ; j<line.length ; j++) {
				senbeiyakiki[i][j] = Integer.parseInt(line[j]);
			}
		}
		System.out.println(solve(senbeiyakiki, raw, column, 0));
		}
	}

	public static int solve(int[][] senbeiyakiki, int raw, int column, int current) {
		if(current == raw) {
			int result = 0;
				int omo = 0;
				int ura = 0;
				for(int j=0 ; j<column ; j++) {
					for(int i=0 ; i<raw ; i++) {
						if(senbeiyakiki[i][j] == 1)
							omo++;
						if(senbeiyakiki[i][j] == 0)
							ura++;
					}
					if(omo >= ura)
						result += omo;
					else
						result += ura;
					omo = 0;
					ura = 0;
				}
			return result;
		}

		int[][] toggle = Arrays.copyOf(senbeiyakiki, senbeiyakiki.length);
		for(int i=0 ; i<column ; i++) {
			toggle[current][i] = toggle[current][i]==0 ? 1 : 0;
		}
		return Math.max(solve(senbeiyakiki, raw, column, current+1), solve(toggle, raw, column, current+1));
	}
}